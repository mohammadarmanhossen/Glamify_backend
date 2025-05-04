# Ecommerce-website (Glamify)


Glamify is a feature-rich e-commerce web application built with Django REST Framework, offering a smooth and secure online shopping experience. From user authentication to product management, order tracking, and secure payments — Glamify is designed to handle every aspect of a modern online store.

- **Glamify Frontend Live Site:** [glamify-frontend-site.netlify.app](https://glamify-frontend-site.netlify.app/)
- **Glamify Backend Live Site:** [glamify-backend-tp2c.onrender.com](https://glamify-backend-tp2c.onrender.com/)
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

## Api Intigration

---
Porduct App:
---
Distict :
```
http://skyline-backend-krnt.onrender.com/district/

```
Hotels :
```
http://skyline-backend-krnt.onrender.com/hotels/
```

Review:
```
http://skyline-backend-krnt.onrender.com/reviews/
```
Bookes:
```
ttp://skyline-backend-krnt.onrender.com/bookeds/
```


Account App:
---
User Login :
```
https://skyline-backend-krnt.onrender.com/client/login/
```
User Register :
```
https://skyline-backend-krnt.onrender.com/client/register/
```

User Logout:
```
https://skyline-backend-krnt.onrender.com/client/logout/
```
Admin login:
```
https://skyline-backend-krnt.onrender.com/client/admin/login/
```
Admin logout :
```
https://skyline-backend-krnt.onrender.com/client/admin/logout/
```

User :
```
https://skyline-backend-krnt.onrender.com/client/users/
```
Contact:
```
https://skyline-backend-krnt.onrender.com/client/contact/
```
Change password:
```
https://skyline-backend-krnt.onrender.com/client/change_password/${user_id}/
```


Payment App:
---
Checkout :
```
https://skyline-backend-krnt.onrender.com/checkout/

```
Order :
```
https://skyline-backend-krnt.onrender.com/order/
```

Created Payment:
```
https://skyline-backend-krnt.onrender.com/payment/create_payment/
```
Payment Success:
```
https://skyline-backend-krnt.onrender.com/payment/success/
```
Payment Cencel :
```
https://skyline-backend-krnt.onrender.com/payment/cancel /
```
Payment Failed :
```
https://skyline-backend-krnt.onrender.com/payment/failed /
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


