# Ecommerce-website (Glamify)


Glamify is a comprehensive ecomomerce-website system developed using Django REST Framework, featuring user authentication, hotel and booking management, payment processing, and review functionalities. This application supports CRUD operations for hotels and bookings, secure payments via SSLCommerz, and integrates.

- **Frontend Live Site:** [Netlify](https://glamify-frontend-site.netlify.app/)
- **Backend Live Site:** [Render](https://glamify-backend-tp2c.onrender.com/)
- **Frontend GitHub:** [Glamify-Frontend](https://github.com/mohammadarmanhossen/Glamify_frontend)
- **Backend GitHub:** [Glamify-Backend](https://github.com/mohammadarmanhossen/Glamify_backend)

### User Access Information
- **Admin Role:**
```
Username: admin
Password: admin
```

- **Normal User:**
```
Username:  arman
Password: Arman404@
```
---

## Key Features
- **User Authentication** via Gmail OAuth
- **CRUD Operations** for add to cart management
- **SSLCommerz Payment Integration** for secure payments
- **Porduct Review System** for customer feedback
- **Scalable PostgreSQL Database** with Django Rest Framework API

---

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** OAuth2 via Gmail
- **Payment Gateway:** SSLCommerz
- **Frontend (Optional):** React/Vue (deployed on Netlify)

---

## Installation and Setup

1. **Clone the repository:**
 ```bash
 
git clone https://github.com/mohammadarmanhossen/Glamify_backend
cd Glamify_backend
```

Install dependencies:
```
pip install -r requirements.txt

```
Run migrations:
```
 python manage.py migrate
```

Create a superuser:
```
python manage.py createsuperuser
```
Run the server:
```
python manage.py runserver
```

Run Tests:

```
python manage.py runserver
```
