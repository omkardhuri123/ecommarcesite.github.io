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


## Troubleshooting Vim Swap File Error

If you see a message like:
  E325: ATTENTION
  Found a swap file by the name "~/Desktop/LOVABLE-MANGO/.git/.COMMIT_EDITMSG.swp" ...

Follow these steps:
1. If another program is editing the file, exit the duplicate session.
2. If the session crashed, run:
     vim -r c:\Users\admin\Desktop\LOVABLE-MANGO\.git\COMMIT_EDITMSG
3. Once recovered, remove the swap file:
     del c:\Users\admin\Desktop\LOVABLE-MANGO\.git\.COMMIT_EDITMSG.swp

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# e_commarce_site

## Resolving Merge Conflicts

To resolve merge conflicts in the README.md file, follow these steps:

1. Stage the updated README.md file:
   ```
   git add c:\Users\admin\Desktop\LOVABLE-MANGO\README.md
   ```
2. Commit the merge resolution with a descriptive message:
   ```
   git commit -m "Merge resolved: concluded merge after conflict resolution"
   ```