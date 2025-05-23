
# 🛍️ Glamify — E-commerce Web Application

**Glamify** is a feature-rich e-commerce web application built with **Django REST Framework**, offering a smooth, secure, and scalable online shopping experience. From user authentication to product management, order tracking, payment processing, and customer reviews — Glamify covers all essential aspects of a modern e-commerce platform.

---

## 🌐 Live Demo

- 🔗 **Frontend Live Site:** [Glamify Frontend](https://glamify-frontend-site.netlify.app/)
- 🔗 **Backend Live Site:** [Glamify Backend](https://glamify-backend-ten.vercel.app/)

---

## 🔐 User Access Information

### 🛠 Admin Login
```
Username: admin
Password: admin
```
### 👤 User Login
```
Username:  arman
Password: arman
```


---

## 🚀 Key Features

- 🔐 **User Authentication** using Gmail OAuth (OAuth2)
- 🛒 **Cart Management** with full CRUD functionality:
  - Add to cart
  - Increase/decrease product quantity
  - Remove product from cart
- 👤 **User Profile:**
  - Update profile info
  - Change password
  - View order history
  - Download order invoices as PDF
- 💳 **SSLCommerz Payment Gateway Integration** for secure online payments
- 🌟 **Product Review System** (only customers who bought a product can review)
- 🗃️ **Scalable PostgreSQL Database**
- 🔧 **Django REST Framework API** for robust backend functionality

---

## 🛠️ Tech Stack

| Layer       | Technology                              |
|-------------|------------------------------------------|
| Backend     | Django, Django REST Framework            |
| Frontend    | Html/Tailwind/JavaScript (Deployed on Netlify)    |
| Database    | PostgreSQL                               |
| Authentication | Gmail OAuth2                          |
| Payment     | SSLCommerz                               |
| Deployment  | Netlify (Frontend), Vercel (Backend)     |

---

## 📁 Repositories

- 💻 **Frontend GitHub Repo:**  
  [github.com/mohammadarmanhossen/Glamify_frontend](https://github.com/mohammadarmanhossen/Glamify_frontend)

- 🖥️ **Backend GitHub Repo:**  
  [github.com/mohammadarmanhossen/Glamify_backend](https://github.com/mohammadarmanhossen/Glamify_backend)

---

## 📷 Screenshots

_Add some UI screenshots here to give visitors a quick visual idea of how Glamify looks and works._

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request with detailed explanation of changes.

---



## Api Intigration Porduct App:
---
Prodcut :
```
https://glamify-backend-code.onrender.com/product/

```
Cart :
```
https://glamify-backend-code.onrender.com/cart/
```

Review:
```
https://glamify-backend-code.onrender.com/review/
```
Brand:
```
https://glamify-backend-code.onrender.com/Brand/
```


Account App:
---
User Login :
```
https://glamify-backend-code.onrender.com/account/login/
```
User Register :
```
https://glamify-backend-code.onrender.com/account/register/
```

User Logout:
```
https://glamify-backend-code.onrender.com/account/logout/
```
Admin login:
```
https://glamify-backend-code.onrender.com/account/admin/login/
```
Admin logout :
```
https://glamify-backend-code.onrender.com/account/admin/logout/
```

User :
```
https://glamify-backend-code.onrender.com/account/user/
```
Contact:
```
https://glamify-backend-code.onrender.com/account/contact/
```
Change password:
```
https://glamify-backend-code.onrender.com/account/change_password/${user_id}/
```


Payment App:
---
Checkout :
```
https://glamify-backend-code.onrender.com/checkout/

```
Order :
```
https://glamify-backend-code.onrender.com/orderitem/
```

Created Payment:
```
https://glamify-backend-code.onrender.com/payment/create_payment/
```
Payment Success:
```
https://glamify-backend-code.onrender.com/payment/success/
```
Payment Cencel :
```
https://glamify-backend-code.onrender.com/payment/cancel /
```
Payment Failed :
```
https://glamify-backend-code.onrender.com/payment/failed /
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


