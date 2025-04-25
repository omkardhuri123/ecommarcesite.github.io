from flask_wtf import FlaskForm
from wtforms import StringField,SelectField, PasswordField, SubmitField, TextAreaField, FloatField, BooleanField, IntegerField,RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange,InputRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0)])
    original_price = FloatField('Original Price', validators=[Optional(), NumberRange(min=0)])
    category_id = IntegerField('Category ID', validators=[DataRequired()])
    featured = BooleanField('Featured Product')
    stock = IntegerField('Stock', validators=[DataRequired(), NumberRange(min=0)])
    weight = StringField('Weight', validators=[Optional()])
    origin = StringField('Origin', validators=[Optional()])
    submit = SubmitField('Save Product')

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    submit = SubmitField('Save Category')



class CheckoutForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()]) # Added validator
    last_name = StringField('Last Name', validators=[DataRequired()]) # Added validator
    email = StringField('Email', validators=[DataRequired(), Email()]) # Added validators
    phone = StringField('Phone', validators=[DataRequired()]) # Added validator
    address = StringField('Address', validators=[DataRequired()]) # Added validator
    city = StringField('City', validators=[DataRequired()]) # Added validator
    state = StringField('State', validators=[DataRequired()]) # Added validator
    zip = StringField('ZIP', validators=[DataRequired()]) # Added validator
    country = SelectField('Country', choices=[
        ('', 'Select Country'),
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('UK', 'United Kingdom'),
        ('AU', 'Australia'),
        ('IN', 'India')
    ], validators=[DataRequired(message="Please select a country.")])
    notes = TextAreaField('Order Notes', validators=[Optional()])
    # Corrected payment_method field using SelectField
    payment_method = RadioField(
        'Payment Method',
        choices=[
            ('card', 'Credit/Debit Card'),
            ('upi', 'UPI Payment'),
            ('cod', 'Cash on Delivery')
        ],
        validators=[InputRequired()]
    )

    submit = SubmitField('Place Order') # Added a submit button

 
class AddToCartForm(FlaskForm):
    """Form for adding a product to the cart."""
    quantity = IntegerField(
        'Quantity',
        default=1,
        validators=[
            DataRequired(message="Please enter a quantity."),
            NumberRange(min=1, message="Quantity must be at least 1.")
            # You might add a max validation later if needed, potentially based on stock
        ]
    )
    # You might not render this submit button directly if you have a custom button,
    # but it's good practice to include it in the form definition.
    submit = SubmitField('Add to Cart')

class CartForm(FlaskForm):
    pass