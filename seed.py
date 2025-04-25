from app import app
from extensions import db
from models import User, Category, Product
from werkzeug.security import generate_password_hash
# seed.py (temporarily)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://app_user:T7m%249Lq%23V2pX%21zR%40@localhost:3306/kokani_bazaar'

def seed_data():
    # Clear existing data
    db.drop_all()
    db.create_all()
    
    # Add categories
    categories = [
        {
            'name': 'Fruits',
            'description': 'Fresh, organic fruits sourced directly from farms',
            'image': '/static/images/categories/fruits.jpg'
        },
        {
            'name': 'Dry Fruits',
            'description': 'Premium quality dry fruits and nuts',
            'image': '/static/images/categories/dry-fruits.jpg'
        },
        {
            'name': 'Spices',
            'description': 'Authentic spices to enhance your culinary experience',
            'image': '/static/images/categories/spices.jpg'
        },
        {
            'name': 'Oils',
            'description': 'Pure, cold-pressed oils for cooking and health',
            'image': '/static/images/categories/oils.jpg'
        },
        {
            'name': 'Pulp',
            'description': 'Natural fruit pulps for refreshing beverages',
            'image': '/static/images/categories/pulp.jpg'
        },
        {
            'name': 'Beverages',
            'description': 'Traditional and refreshing drinks',
            'image': '/static/images/categories/beverages.jpg'
        }
    ]
    
    for cat_data in categories:
        category = Category(
            name=cat_data['name'], 
            description=cat_data['description'], 
            image=cat_data['image']
        )
        db.session.add(category)
    
    db.session.commit()
    
    # Get category IDs
    fruits_id = Category.query.filter_by(name='Fruits').first().id
    dry_fruits_id = Category.query.filter_by(name='Dry Fruits').first().id
    spices_id = Category.query.filter_by(name='Spices').first().id
    oils_id = Category.query.filter_by(name='Oils').first().id
    pulp_id = Category.query.filter_by(name='Pulp').first().id
    beverages_id = Category.query.filter_by(name='Beverages').first().id
    
    # Add products
    products = [
        {
            'name': 'Organic Alphonso Mangoes',
            'description': 'Sweet and aromatic Alphonso mangoes, known as the king of fruits',
            'price': 1000,
            'original_price': 1100,
            'image': '/static/images/products/alphonso-mangoes.jpg',
            'category_id': fruits_id,
            'featured': True,
            'rating': 4.8,
            'stock': 1000,
            'weight': '1 kg',
            'origin': 'Devgad, Maharashtra'
        },
        {
            'name': 'Premium Cashews',
            'description': 'Large, crunchy cashews, perfect for snacking or cooking',
            'price': 1000,
            'original_price': 1200,
            'image': '/static/images/products/cashews.jpg',
            'category_id': dry_fruits_id,
            'featured': True,
            'rating': 4.6,
            'stock': 1000,
            'weight': '1 kg',
            'origin': 'vengurla,maharashtra'
        },
        {
            'name': 'Kokam',
            'description': 'Traditional fruit known for its culinary and medicinal properties',
            'price': 400,
            'image': '/static/images/products/kokam.jpg',
            'category_id': fruits_id,
            'featured': False,
            'rating': 4.3,
            'stock': 800,
            'weight': '1kg',
            'origin': 'vengurla,maharshtra'
        },
        {
            'name': 'Cold Pressed Coconut Oil',
            'description': 'Pure, cold-pressed coconut oil, ideal for cooking and skincare',
            'price': 300,
            'original_price': 350,
            'image': '/static/images/products/coconut-oil.jpg',
            'category_id': oils_id,
            'featured': True,
            'rating': 4.9,
            'stock': 500,
            'weight': '1 L',
            'origin': 'vengurla,maharshtra'
        },
        {
            'name': 'Natural Mango Pulp',
            'description': 'Sweet mango pulp, perfect for smoothies, desserts, and beverages',
            'price': 300,
            'image': '/static/images/products/mango-pulp.jpg',
            'category_id': pulp_id,
            'featured': False,
            'rating': 4.5,
            'stock': 45,
            'weight': '500 ml',
            'origin': 'vengurla,Maharashtra'
        },
        {
            'name': 'Kokam Sarbat',
            'description': 'Refreshing traditional beverage with digestive properties',
            'price': 150,
            'image': '/static/images/products/kokam-sarbat.jpg',
            'category_id': beverages_id,
            'featured': True,
            'rating': 4.4,
            'stock': 60,
            'weight': '500 ml',
            'origin': 'Konkan Region'
        },
        {
            'name': 'Amla Sarbat',
            'description': 'Vitamin C rich traditional drink made from Indian gooseberries',
            'price': 150,
            'image': '/static/images/products/amla-sarbat.jpg',
            'category_id': beverages_id,
            'featured': False,
            'rating': 4.2,
            'stock': 55,
            'weight': '500 ml',
            'origin': 'vengurla,maharashtra'
        }
    ]
    
    for prod_data in products:
        product = Product(
            name=prod_data['name'],
            description=prod_data['description'],
            price=prod_data['price'],
            original_price=prod_data.get('original_price'),
            image=prod_data['image'],
            category_id=prod_data['category_id'],
            featured=prod_data['featured'],
            rating=prod_data['rating'],
            stock=prod_data['stock'],
            weight=prod_data['weight'],
            origin=prod_data['origin']
        )
        db.session.add(product)
    
    # Add admin user
    admin = User(
        name='Omkar Dhuri',
        email='dhuri8973@gmail.com'
    )
    admin.set_password('akshy@12345')
    db.session.add(admin)
    
    db.session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    with app.app_context():
        seed_data()