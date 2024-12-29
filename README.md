
# Food Ordering System


## Description
    The Food Ordering System is a Django-based web application that allows users to:
    - Browse food categories and items.
    - Place orders for pickup or delivery.
    - Request catering services.
    - Manage orders, customers, and deliveries.

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Python**
   - Version: 3.9 or higher
   - Download: [Python Official Website](https://www.python.org/)

2. **Django**
   - Version: 4.2 or higher
   - Install via pip:
     ```bash
     pip install django
    ```
    

3. **Database**
   - Default: SQLite (comes pre-configured with Django)
   - Optional: PostgreSQL (if you prefer a more robust database)

4. **Other Dependencies**
   Install additional packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt

5.Virtual Environment (Optional but Recommended)
    Create a virtual environment to isolate project dependencies:
    ```bash
        python -m venv venv
        source venv/bin/activate  # macOS/Linux
        venv\Scripts\activate     # Windows

## Installation
 Follow these steps to set up the project locally:

1. Clone the repository:
    ```bash
        git clone <repository_url>

    2.Navigate to the project directory:
        cd FoodOrdering
    
    3.Create and activate a virtual environment:
    .   For Windows:
        python -m venv venv
        venv\Scripts\activate

    .   For macOS/Linux:
        python3 -m venv venv
        source venv/bin/activate
    
    4.Install the dependencies:
        pip install -r requirements.txt

    5.Apply database migrations:
        python manage.py migrate


    6.Run the development server:
        python manage.py runserver

---

#### **4. Usage**


```markdown
## Usage
1. Access the application in your browser at `http://127.0.0.1:8000/`.
2. Navigate through the available features:
   - Browse food categories and items.
   - Place an order for pickup or delivery.
   - Request catering services.
3. Use the Django admin panel to manage the database:
   - Create a superuser:
     ```bash
     python manage.py createsuperuser
     ```
   - Log in at `http://127.0.0.1:8000/admin/` with the superuser credentials.

## Testing
To test the application:

1. Run the provided test suite:
   ```bash
   python manage.py test

2.Populate the database with sample data (if applicable):
python manage.py shell
exec(open('populate_test_data.py').read())

3.Manually test functionalities through the web interface.

---

#### **6. Features**
Highlight the key features of your application.

```markdown
## Features
- View food categories and items.
- Place orders with pickup or delivery options.
- Request catering services.
- Manage customers and orders via the admin panel.


## Technologies Used
- Python
- Django
- SQLite (or other database)
- Bootstrap ( used for styling)

## Authors
- [Jemimah Gabriel](mailto:ada06Jemimah@gmail.com)


## Acknowledgments
- Django documentation
- Bootstrap documentation












