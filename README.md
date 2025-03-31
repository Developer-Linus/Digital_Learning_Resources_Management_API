**Digital Learning Resources Management API Documentation**
===========================================================

### Table of Contents
1. [Overview](#overview)
2. [Getting Started](#getting-started)
3. [API Endpoints](#api-endpoints)
4. [Request and Response Formats](#request-and-response-formats)
5. [Error Handling](#error-handling)
6. [Security Considerations](#security-considerations)

### Overview
 The Digital Learning Resources Management API is designed to simplify the process of organizing and retrieving digital learning resources. It addresses the common problem of losing track of valuable resources, allowing users to store, manage, and access materials in a centralized database. The API enables users to add, update, retrieve, and delete resources, as well as track progress, bookmark favorite materials, and access a learning log. By providing a streamlined way to manage digital learning resources, this API aims to help users achieve their learning goals efficiently and effectively.

### Getting Started

This guide will help you set up and run the Django REST Framework (DRF) project locally using MySQL as the database.

#### Prerequisites
Ensure you have the following installed on your machine:
- Python (>= 3.8)
- MySQL Server
- MySQL Client
- Virtualenv (optional but recommended)
- Git

### Installation Steps

#### 1. Clone the Repository
```sh
git clone https://github.com/Developer-Linus/Digital_Learning_Resources_Management_API.git
cd Digital_Learning_Resources_Management_API
```

#### 2. Create and Activate a Virtual Environment
```sh
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

#### 4. Configure the `.env` File
Create a `.env` file in the project root and add the following:
```ini
DEBUG=True
SECRET_KEY=your_secret_key_here
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=127.0.0.1
DB_PORT=3306
GMAIL_ACCOUNT=your_gmail_account
GMAIL_APP_PASSWORD=your_gmail_app_password
```

#### 5. Set Up the Database
- Ensure MySQL is running.
- Create the database manually if it doesn’t exist:
```sql
CREATE DATABASE your_database_name;
```
#### 6. Apply Migrations
```sh
python manage.py migrate
```
#### 7. Create a Superuser (Optional)
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

#### 8. Run the Development Server
```sh
python manage.py runserver
```

The project should now be running at `http://127.0.0.1:8000/`


##### Troubleshooting
- **Issue: Module not found**
  - Ensure virtual environment is activated.
- **Database connection error**
  - Verify `.env` credentials match your MySQL setup.
  - Ensure MySQL server is running.
- **Migrations not applied properly**
  - Try `python manage.py makemigrations` followed by `python manage.py migrate`.

### API Endpoints
- The API endpoints are documented using Swagger UI, which provides an interactive and easily accessible way to explore the available endpoints. You can access the Swagger UI documentation at http://localhost:8000/swagger/.

### Request and Response Formats
 Describe the formats used for API requests and responses, including any required headers, query parameters, or body data.

### Error Handling
The API uses a custom error handling approach to provide informative error responses. The following error responses are used:

* **400 Bad Request**: Returned when the request data is invalid or cannot be processed. Examples of 400 errors include:
	+ Invalid JSON payload: `{"status": "error", "message": "Invalid JSON payload", "details": "JSON decode error"}`
	+ Missing required fields: `{"status": "error", "message": "Missing required fields", "errors": {"field1": ["This field is required"]}}`
	+ Invalid field values: `{"status": "error", "message": "Invalid field values", "errors": {"field2": ["Invalid value"]}}`
* **404 Not Found**: Returned when the requested resource is not found. Examples of 404 errors include:
	+ Resource not found: `{"status": "error", "message": "Resource not found", "details": "The requested resource does not exist"}`
	+ Invalid URL: `{"status": "error", "message": "Invalid URL", "details": "The requested URL is not valid"}`
* **500 Internal Server Error**: Returned when an unexpected error occurs on the server. Examples of 500 errors include:
	+ Server error: `{"status": "error", "message": "Server error", "details": "An unexpected error occurred on the server"}`
	+ Database error: `{"status": "error", "message": "Database error", "details": "A database error occurred while processing the request"}`
	+ Authentication error: `{"status": "error", "message": "Authentication error", "details": "An authentication error occurred while processing the request"}`

In general, the API returns error responses with a JSON object containing the following fields:

* `status`: A string indicating the status of the response, either "success" or "error".
* `message`: A human-readable message describing the outcome of the request.
* `errors`: An object containing validation errors or other error details, if any.
* `details`: A string containing additional details about the error, if available.

The API uses standard HTTP status codes to indicate the outcome of a request, and the error responses are designed to be informative and helpful for debugging purposes. This allows developers to quickly identify and resolve issues, and ensures that the API is robust and reliable.

### Security Considerations
 Discuss any security considerations or best practices for using the API, including authentication, authorization, and data encryption.