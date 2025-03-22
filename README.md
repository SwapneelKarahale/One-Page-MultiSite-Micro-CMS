# **Lead Capture & Walk-in Token System**  

## **📌 Overview**  
This project is a **Lead Capture & Walk-in Token System**, where visitors can:  
✅ View available devices in a **3x4 grid**.  
✅ Fill out a **lead capture form** to see devices in their **city**.  
✅ Select a **device & submit**, generating a **walk-in token**.  
✅ Receive an **email notification** with their **token number**.  
✅ Admin & Vendor can **manage leads & walk-ins** in **Django Admin**.  

---

## **🛠️ Tech Stack**  
- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL  
- **Frontend:** React (if applicable)  
- **Email:** SMTP (Gmail App Password)  

---

## **🚀 Features**  
🔹 **Lead Capture Form**: Collects visitor details (Name, Email, City, etc.).  
🔹 **Device Filtering**: Displays devices **available in the visitor's city**.  
🔹 **Walk-in Record**: Creates a new entry with **vendor & device details**.  
🔹 **Token Generation**: Auto-generates a **walk-in token number**.  
🔹 **Email Notifications**: Sends **token details** to the visitor & vendor.  
🔹 **Admin Panel**: Allows management of **leads, walk-ins, vendors & devices**.  

---

## **📂 API Endpoints **  

---

### **1️⃣ Country & City APIs**  

#### **📍 Create a Country**  
🔹 **Method:** `POST`  
🔹 **Endpoint:** `/api/countries/`  
🔹 **Request Body (JSON):**  
```json
{
  "name": "USA"
}
```
🔹 **Response (Success):**  
```json
{
  "id": 1,
  "name": "USA"
}
```

#### **📍 Get All Countries**  
🔹 **Method:** `GET`  
🔹 **Endpoint:** `/api/countries/`  
🔹 **Response (Success):**  
```json
[
  {
    "id": 1,
    "name": "USA"
  }
]
```

#### **📍 Create a City**  
🔹 **Method:** `POST`  
🔹 **Endpoint:** `/api/cities/`  
🔹 **Request Body (JSON):**  
```json
{
  "name": "New York",
  "country": 1
}
```
🔹 **Response (Success):**  
```json
{
  "id": 1,
  "name": "New York",
  "country": 1
}
```

#### **📍 Get All Cities**  
🔹 **Method:** `GET`  
🔹 **Endpoint:** `/api/cities/`  
🔹 **Response (Success):**  
```json
[
  {
    "id": 1,
    "name": "New York",
    "country": 1
  }
]
```

---

### **2️⃣ Vendor APIs**  

#### **📍 Create a Vendor**  
🔹 **Method:** `POST`  
🔹 **Endpoint:** `/api/vendors/`  
🔹 **Request Body (JSON):**  
```json
{
  "name": "Tech Supplier Inc.",
  "phone_number": "9876543210",
  "address": "123 Business St.",
  "city": 1,
  "country": 1,
  "managed_by": 1
}
```
🔹 **Response (Success):**  
```json
{
  "id": 1,
  "name": "Tech Supplier Inc."
}
```

#### **📍 Get All Vendors**  
🔹 **Method:** `GET`  
🔹 **Endpoint:** `/api/vendors/`  
🔹 **Response (Success):**  
```json
[
  {
    "id": 1,
    "name": "Tech Supplier Inc.",
    "phone_number": "9876543210",
    "address": "123 Business St.",
    "city": 1,
    "country": 1,
    "managed_by": 1
  }
]
```

---

### **3️⃣ Device APIs**  

#### **📍 Create a Device**  
🔹 **Method:** `POST`  
🔹 **Endpoint:** `/api/devices/create/`  
🔹 **Request Body (Form-Data in Postman, NOT JSON):**  
  | Key | Value | Type |
  |----|----|----|
  | name | iPhone 15 | Text |
  | photo | (Upload an image) | File |
  | currency | USD | Text |
  | offer_price | 999.99 | Number |
  | sourced_from | 1 | Number |
  | status | true | Boolean |

🔹 **Response (Success):**  
```json
{
  "id": 1,
  "name": "iPhone 15",
  "currency": "USD",
  "offer_price": 999.99,
  "status": true
}
```

#### **📍 Get All Devices**  
🔹 **Method:** `GET`  
🔹 **Endpoint:** `/api/devices/`  
🔹 **Response (Success):**  
```json
[
  {
    "id": 1,
    "name": "iPhone 15",
    "currency": "USD",
    "offer_price": 999.99,
    "status": true
  }
]
```

---

### **4️⃣ Lead Capture & Token Generation APIs**  

#### **📍 Capture a Lead**  
🔹 **Method:** `POST`  
🔹 **Endpoint:** `/api/lead-capture/`  
🔹 **Request Body (JSON):**  
```json
{
  "name": "John Doe",
  "phone_number": "1234567890",
  "email": "johndoe@example.com",
  "address": "123 Main St",
  "city": 1,
  "country": 1,
  "referral_code": "REF123"
}
```
🔹 **Response (Success):**  
```json
{
  "message": "Lead captured successfully!",
  "token_number": 1
}
```

---

### **5️⃣ Walk-in APIs**  

#### **📍 Get All Walk-ins**  
🔹 **Method:** `GET`  
🔹 **Endpoint:** `/api/walkins/`  
🔹 **Response (Success):**  
```json
[
  {
    "id": 1,
    "lead": 1,
    "vendor": 1,
    "device": 1,
    "currency": "USD",
    "offer_price": 100.00,
    "walk_in_datetime": "2025-03-21T10:00:00Z",
    "token_number": 1
  }
]
```

---

### **6️⃣ Web Page APIs**  

#### **📍 Get a Specific Web Page**  
🔹 **Method:** `GET`  
🔹 **Endpoint:** `/api/webpage/<id>/`  
🔹 **Response (Success):**  
```json
{
  "id": 1,
  "title": "Home Page",
  "allowed_devices": [1, 2, 3],
  "sections": [
    {
      "title": "Welcome Banner",
      "html_content": "<h1>Welcome</h1>",
      "order": 1
    },
    {
      "title": "Available Devices",
      "html_content": "<div>Device Grid Here</div>",
      "order": 2
    }
  ]
}
```

---

## **📌 Summary of All APIs**
| Category | Method | Endpoint | Description |
|----------|--------|----------|-------------|
| **Country** | `POST` | `/api/countries/` | Create a country |
| **Country** | `GET` | `/api/countries/` | Get all countries |
| **City** | `POST` | `/api/cities/` | Create a city |
| **City** | `GET` | `/api/cities/` | Get all cities |
| **Vendor** | `POST` | `/api/vendors/` | Create a vendor |
| **Vendor** | `GET` | `/api/vendors/` | Get all vendors |
| **Device** | `POST` | `/api/devices/create/` | Create a device |
| **Device** | `GET` | `/api/devices/` | Get all devices |
| **Lead** | `POST` | `/api/lead-capture/` | Capture a lead & generate a token |
| **Walk-in** | `GET` | `/api/walkins/` | Get all walk-in records |
| **Web Page** | `GET` | `/api/webpage/<id>/` | Retrieve a specific webpage |

---

## **📧 Email Configuration (Gmail SMTP)**  
1️⃣ Enable **2-Step Verification** in your **Google Account**.  
2️⃣ Generate a **16-character App Password** .  
3️⃣ Add it to your **Django settings**:  
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_generated_app_password'
```

---

## **🖥️ Running the Project**  

### **🔹 Setup**  
```bash
# Clone the repository
git clone https://github.com/SwapneelKarahale/One-Page-MultiSite-Micro-CMS.git


# Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r Requirement.txt

# Apply migrations & run server
python manage.py migrate
python manage.py runserver
```

### **🔹 Access Django Admin**  
```bash
# Create a superuser
python manage.py createsuperuser
```
Login at: **`http://127.0.0.1:8000/admin/`**  

---

## **📌 Final Workflow**  

1️⃣ Visitor lands on the webpage → Sees **3x4 grid of devices**.  
2️⃣ Fills the **lead form** → Devices in their **city are shown**.  
3️⃣ Selects a **device & submits** → A **walk-in record is created**.  
4️⃣ Token Number is **generated & sent via email**.  
5️⃣ Admin & Vendor **manage walk-in records** in Django Admin.  

---

## **🔗 License**  
This project is **open-source** and available under the **MIT License**.  

---

Let me know if you need modifications! 🚀