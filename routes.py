from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from app import app
from extensions import db
from models import User, Category, Product, Order, OrderItem
from forms import LoginForm, RegisterForm, ProductForm, CategoryForm, CheckoutForm, AddToCartForm,CartForm
import logging
from sqlalchemy import or_


@app.route('/')
def index():
    featured_products = Product.query.filter_by(featured=True).limit(4).all()
    categories = Category.query.limit(6).all()
    
    # Handle search if query parameter exists
    query = request.args.get('search')
    search_results = []
    if query:
        search_results = Product.query.filter(
            or_(
                Product.name.ilike(f'%{query}%'),
                Product.description.ilike(f'%{query}%')
            )
        ).all()
        return render_template('shop.html', products=search_results, search_query=query)
    
    return render_template('index.html', featured_products=featured_products, categories=categories)

@app.route('/categories')
def categories():
    all_categories = Category.query.all()
    return render_template('categories.html', categories=all_categories)

@app.route('/category/<int:id>')
def category_detail(id):
    category = Category.query.get_or_404(id)
    products = Product.query.filter_by(category_id=id).all()
    form = AddToCartForm() 
    return render_template('category_detail.html', category=category, products=products, form=form)

@app.route('/shop')
def shop():
    # Handle search if query parameter exists
    query = request.args.get('search')
    if query:
        products = Product.query.filter(
            or_(
                Product.name.ilike(f'%{query}%'),
                Product.description.ilike(f'%{query}%')
            )
        ).all()
        return render_template('shop.html', products=products, search_query=query)
    else:
        products = Product.query.all()
    
    return render_template('shop.html', products=products)

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    related_products = Product.query.filter_by(category_id=product.category_id).filter(Product.id != id).limit(4).all()
    add_to_cart_form = AddToCartForm()
    return render_template('product_detail.html', product=product, related_products=related_products, form=add_to_cart_form)

@app.route('/cart')
def cart():
    form = CartForm()
    cart_items = session.get('cart', {})
    
    product_ids = cart_items.keys()
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    
    valid_products = []
    for product in products:
        if product.stock >= cart_items.get(str(product.id), 0):
            valid_products.append(product)
        else:
            cart_items[str(product.id)] = product.stock
            session.modified = True
    
    for product in products:
        product.total = product.price * cart_items.get(str(product.id), 0)
    
    total_cart_value = sum(product.total for product in valid_products)
    
    return render_template('cart.html', 
                          products=valid_products, 
                          total=total_cart_value,
                          form=form)  # Pass form to template

@app.route('/add-to-cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    form = CartForm()
    if form.validate_on_submit():
        product = Product.query.get_or_404(product_id)
        quantity = int(request.form.get('quantity', 1))
        
        if product.stock < 1:
            flash('Product is out of stock')
            return redirect(url_for('product_detail', id=product.id))
        
        session_cart = session.setdefault('cart', {})
        current_quantity = session_cart.get(str(product.id), 0)
        new_quantity = current_quantity + quantity
        
        if new_quantity > product.stock:
            new_quantity = product.stock
            flash('Maximum stock available added to cart')
        
        session_cart[str(product.id)] = new_quantity
        session.modified = True
        
        return redirect(url_for('cart'))
    return redirect(url_for('cart'))

@app.route('/update-cart/<int:product_id>/<action>', methods=['POST'])
def update_cart(product_id, action):
    form = CartForm()
    if form.validate_on_submit():
        if 'cart' not in session:
            return redirect(url_for('cart'))
        
        product = Product.query.get_or_404(product_id)
        current_quantity = session['cart'].get(str(product.id), 0)
        
        if action == 'increase':
            new_quantity = current_quantity + 1
        elif action == 'decrease':
            new_quantity = current_quantity - 1
        else:
            return redirect(url_for('cart'))
        
        new_quantity = max(1, min(new_quantity, product.stock))
        
        session['cart'][str(product.id)] = new_quantity
        session.modified = True
        
        return redirect(url_for('cart'))
    return redirect(url_for('cart'))

@app.route('/remove-from-cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    form = CartForm()
    if form.validate_on_submit():
        if 'cart' in session and str(product_id) in session['cart']:
            del session['cart'][str(product_id)]
            session.modified = True
        return redirect(url_for('cart'))
    return redirect(url_for('cart'))

@app.route('/clear-cart', methods=['POST'])
def clear_cart():
    form = CartForm()
    if form.validate_on_submit():
        session.pop('cart', None)
        return redirect(url_for('cart'))
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = CheckoutForm()
    cart_items = session.get('cart', {})
    products = Product.query.filter(Product.id.in_(cart_items.keys())).all()
    
    # Calculate totals
    for product in products:
        product.total = product.price * cart_items.get(str(product.id), 0)
    
    if form.validate_on_submit():
        # Process payment and create order
        return redirect(url_for('order_confirmation'))
    
    return render_template('checkout.html', form=form, products=products)

@app.route('/process-payment', methods=['POST'])
def process_payment():
    form = CheckoutForm()
    if not form.validate_on_submit():
        flash('Invalid form data. Please check your inputs.')
        print(form.errors)
        return redirect(url_for('checkout'))
    
    if 'user_id' not in session:
        flash('You must be logged in to place an order.', 'warning')
        print(form.errors)
        return redirect(url_for('login'))
    
    # Get cart data
    cart = session.get('cart', {})
    if not cart:
        flash('Your cart is empty')
        return redirect(url_for('shop'))
    
    # Validate stock availability
    product_ids = list(cart.keys())
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    for product in products:
        if product.stock < cart.get(str(product.id), 0):
            flash(f'Sorry, {product.name} is now out of stock')
            return redirect(url_for('cart'))
    
    # Create order
    order = Order(
        user_id=session['user_id'],
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        email=form.email.data,
        phone=form.phone.data,
        address=form.address.data,
        city=form.city.data,
        state=form.state.data,
        zip=form.zip.data,
        country=form.country.data,
        notes=form.notes.data,
        payment_method=form.payment_method.data,
        payment_status='pending',
        total=0  # Will calculate below
    )
    
    # Calculate total and create order items
    total = 0
    order_items_list = []
    for product in products:
        quantity = cart[str(product.id)]
        item_price = product.price # Price at the time of order
        item_total_for_calc = item_price * quantity # Calculate item total for overall order total

        order_item = OrderItem(
            # No need to set order_id here, relationship handles it
            product_id=product.id,
            quantity=quantity,
            price=item_price # Store the price per item
        )
        order_items_list.append(order_item) # Now this works
        total += item_total_for_calc # Add to the grand total

    order.order_items = order_items_list
    order.total = total + 5  # Add tax (ensure model uses 'total' column)
    
    # Process payment (mock)
    try:
        payment_success = True  # Replace with actual payment logic
        
        if payment_success:
            # Update stock
            for product in products:
                product.stock -= cart.get(str(product.id), 0)
            
            # Save to database
            db.session.add(order)
            db.session.commit()
            
            # Clear cart
            session.pop('cart', None)
            
            return redirect(url_for('order_confirmation', order_id=order.id))
        else:
            flash('Payment failed. Please try again')
            return redirect(url_for('checkout'))
    except Exception as e:
        db.session.rollback()
        app.logger.error(f"Payment processing error: {str(e)}")
        flash('An error occurred during payment processing')
        return redirect(url_for('checkout'))

@app.route('/order-confirmation/<int:order_id>')
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order_confirmation.html', order=order)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered', 'danger')
        else:
            new_user = User(name=name, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

@app.route('/add-to-wishlist/<int:product_id>', methods=['POST'])
def add_to_wishlist(product_id):
    product = Product.query.get_or_404(product_id)
    
    # Initialize wishlist in session if needed
    wishlist = session.get('wishlist', [])
    # Ensure all IDs are integers
    wishlist = [int(pid) for pid in wishlist]
    if int(product_id) not in wishlist:
        wishlist.append(int(product_id))
        session['wishlist'] = wishlist
        session.modified = True  # Mark session as modified
    
    return redirect(url_for('wishlist'))

@app.route('/wishlist')
def wishlist():
    wishlist_product_ids = session.get('wishlist', [])
    wishlist_products = Product.query.filter(Product.id.in_(wishlist_product_ids)).all()
    form = AddToCartForm()
    return render_template('wishlist.html', products=wishlist_products, form=form)

@app.route('/remove-from-wishlist/<int:product_id>', methods=['POST'])
def remove_from_wishlist(product_id):
    wishlist = session.get('wishlist', [])
    wishlist = [int(pid) for pid in wishlist]
    if int(product_id) in wishlist:
        wishlist.remove(int(product_id))
        session['wishlist'] = wishlist
        session.modified = True
    flash('Product removed from wishlist', 'info')
    return redirect(url_for('wishlist'))

@app.route('/account')
def account():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Get user data from database
    user = User.query.get(session['user_id'])
    if not user:
        return redirect(url_for('logout'))
    
    return render_template('myaccount.html', user=user)