# kokani Bazaar - Flask E-commerce Application

An organic product e-commerce platform built with Flask and MySQL.

## Features

- User authentication (login, registration)
- Product browsing by category
- Product details with related products
- Shopping cart functionality
- Responsive design for all devices

## Tech Stack

- **Backend**: Flask, SQLAlchemy
- **Database**: MySQL
- **Frontend**: HTML, CSS, Tailwind CSS
- **Icons**: Lucide.js

## Setup Instructions

1. Clone the repository
2. Create a virtual environment
   ```
   python -m venv venv
   ```
3. Activate the virtual environment
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies
   ```
   pip install -r requirements.txt
   ```
5. Configure your MySQL database in `app.py`
6. Initialize the database
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
7. Seed the database
   ```
   python seed.py
   ```
8. Run the application
   ```
   flask run
   ```
9. Open your browser and navigate to `http://localhost:5000`

## Project Structure

- `app.py`: Main application file
- `models.py`: Database models
- `routes.py`: Application routes
- `forms.py`: Form definitions
- `templates/`: HTML templates
- `static/`: CSS, JavaScript, and images

## Future Enhancements

- User profiles and order history
- Product reviews and ratings
- Admin dashboard
- Payment processing integration
- Search functionality

## License

This project is licensed under the MIT License - see the LICENSE file for details.
