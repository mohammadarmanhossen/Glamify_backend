# Ecommerce-website (Glamify)


Glamify is a feature-rich e-commerce web application built with Django REST Framework, offering a smooth and secure online shopping experience. From user authentication to product management, order tracking, and secure payments — Glamify is designed to handle every aspect of a modern online store.

- **Glamify Frontend Live Site:** [Glamify Frontend](https://glamify-frontend-site.netlify.app/)
- **Glamify Backend Live Site:** [Glamfiy Backend](https://glamify-backend-tp2c.onrender.com/)
- **Glamify Frontend GitHub:** [github.com/mohammadarmanhossen/Glamify_frontend](https://github.com/mohammadarmanhossen/Glamify_frontend)
- **Glamify Backend GitHub:** [github.com/mohammadarmanhossen/Glamify_backend](https://github.com/mohammadarmanhossen/Glamify_backend)

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
- **Product add to cart**cart product quantity positive negative delete
- **User profile password change.And order derails PDF download 
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


- **Frontend Live Site:** [Glamify Frontend](https://glamify-frontend-site.netlify.app/)
- **Backend Live Site:** [Glamify Backend](https://glamify-backend-tp2c.onrender.com/)

---

## Api Intigration

---
Porduct App:
---
Prodcut :
```
https://glamify-backend-tp2c.onrender.com/product/

```
Cart :
```
https://glamify-backend-tp2c.onrender.com/cart/
```

Review:
```
https://glamify-backend-tp2c.onrender.com/review/
```
Brand:
```
https://glamify-backend-tp2c.onrender.com/Brand/
```


Account App:
---
User Login :
```
https://glamify-backend-tp2c.onrender.com/account/login/
```
User Register :
```
https://glamify-backend-tp2c.onrender.com/account/register/
```

User Logout:
```
https://glamify-backend-tp2c.onrender.com/account/logout/
```
Admin login:
```
https://glamify-backend-tp2c.onrender.com/account/admin/login/
```
Admin logout :
```
https://glamify-backend-tp2c.onrender.com/account/admin/logout/
```

User :
```
https://glamify-backend-tp2c.onrender.com/account/user/
```
Contact:
```
https://glamify-backend-tp2c.onrender.com/account/contact/
```
Change password:
```
https://glamify-backend-tp2c.onrender.com/account/change_password/${user_id}/
```


Payment App:
---
Checkout :
```
https://glamify-backend-tp2c.onrender.com/checkout/

```
Order :
```
https://glamify-backend-tp2c.onrender.com/orderitem/
```

Created Payment:
```
https://glamify-backend-tp2c.onrender.com/payment/create_payment/
```
Payment Success:
```
https://glamify-backend-tp2c.onrender.com/payment/success/
```
Payment Cencel :
```
https://glamify-backend-tp2c.onrender.com/payment/cancel /
```
Payment Failed :
```
https://glamify-backend-tp2c.onrender.com/payment/failed /
```

---
## Installation and Setup

 **Clone the repository:**
 ```bash
 
git clone https://github.com/mohammadarmanhossen/Skyline_backend
cd Skyline_backend
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


