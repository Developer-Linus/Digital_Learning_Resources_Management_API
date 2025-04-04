**Digital Learning Resources Management API Documentation**
===========================================================

### Table of Contents
1. [Overview](#Overview)
2. [Features](#Features)
3. [Getting Started](#getting-started)
4. [API Endpoints](#api-endpoints)
5. [Error Handling](#error-handling)
6. [Security Considerations](#security-considerations)

### Overview
 The Digital Learning Resources Management API is designed to simplify the process of organizing and retrieving digital learning resources. It addresses the common problem of losing track of valuable resources, allowing users to store, manage, and access materials in a centralized database. The API enables users to add, update, retrieve, and delete resources, as well as track progress, bookmark favorite materials, and access a learning log. By providing a streamlined way to manage digital learning resources, this API aims to help users achieve their learning goals efficiently and effectively.
### Features
The Digital Learning Resources Management API is designed to provide a comprehensive platform for managing digital learning resources. The API supports a range of features that enable users to create, read, update, and delete resources, as well as track their learning progress and interact with the resources in a meaningful way.

#### 2.1. Resource Management
2.1.1 **Create Resource**: Users can create new resources, including text-based content, images, videos, and other file types. <br>
2.1.2 **Read Resource**: Users can retrieve existing resources, including their metadata and content. <br>
2.1.3. **Update Resource**: Users can update existing resources, including their metadata and content. <br>
2.1.4. **Delete Resource**: Users can delete existing resources, including their metadata and content.

#### 2.2 Learning Log Management
2.2.1. **Create Learning Log**: Users can create new learning logs to track their progress and notes for each resource. <br>
2.2.2. **Read Learning Log**: Users can retrieve existing learning logs, including their notes and progress. <br>
2.2.3. **Update Learning Log**: Users can update existing learning logs, including their notes and progress. <br>
2.2.4. **Delete Learning Log**: Users can delete existing learning logs.

#### 2.3. Resource Status Management
2.3.1. **Update Resource Status**: Users can update the status of a resource, including marking it as completed, in progress, or not started. <br>
2.3.2. **Get Resource Status**: Users can retrieve the status of a resource.

#### 2.4. Bookmarking
2.4.1. **Bookmark Resource**: Users can bookmark resources for future reference. <br>
2.4.2. **Unbookmark Resource**: Users can unbookmark resources. <br>
2.4.3. **Get Bookmarked Resources**: Users can retrieve a list of bookmarked resources. <br>

#### 2.5. Authentication and Authorization
2.5.1. **Robust Authentication**: The API uses a robust authentication system to ensure that only authorized users can access and modify resources. <br>
2.5.2. **Role-Based Access Control**: The API uses role-based access control to ensure that users can only perform actions that are authorized for their role. <br>

#### 2.6. Notification System
2.6.1. **Resource Creation Notifications**: Users can receive notifications when a new resource is created. <br>
2.6.2. **Learning Log Creation Notifications**: Users can receive notifications when a new learning log is created. <br>
2.6.3. **Bookmarking Notifications**: Users can receive notifications when a resource is bookmarked or unbookmarked.

#### 2.7. Filtering and Ordering
2.7.1. **Filtering**: The API supports filtering for list API views, allowing users to retrieve resources based on specific criteria, such as resource type, status, or tags. <br>
2.7.2. **Ordering**: The API supports ordering for list API views, allowing users to retrieve resources in a specific order, such as alphabetical or chronological.

#### 2.8. Pagination
2.8.1. **Pagination**: The API supports pagination for list API views, allowing users to retrieve a limited number of resources at a time and navigate through the results.

### Getting Started

This guide will help you set up and run the Django REST Framework (DRF) project locally using MySQL as the database.

#### Prerequisites
Ensure you have the following installed on your machine:
- Python (>= 3.8)
- MySQL Server
- MySQL Client
- Virtualenv (optional but recommended)
- Git

### 3.1. Installation Steps

#### 3.1.1. Clone the Repository
```sh
git clone https://github.com/Developer-Linus/Digital_Learning_Resources_Management_API.git
cd Digital_Learning_Resources_Management_API
```

#### 3.1.2. Create and Activate a Virtual Environment
```sh
python -m venv venv
# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3.1.3. Install Dependencies
```sh
pip install -r requirements.txt
```

#### 3.1.4. Configure the `.env` File
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

#### 3.1.5. Set Up the Database
- Ensure MySQL is running.
- Create the database manually if it doesn’t exist:
```sql
CREATE DATABASE your_database_name;
```
#### 3.1.6. Apply Migrations
```sh
python manage.py migrate
```
#### 3.1.7. Create a Superuser (Optional)
```sh
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

#### 3.1.8. Run the Development Server
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

- The API endpoints are documented using Swagger UI, which provides an interactive and easily accessible way to explore the available endpoints. You can access the Swagger UI documentation at https://devlinus.pythonanywhere.com/.


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

The Digital Learning Resources Management API is designed with security in mind, and there are several considerations and best practices that users should be aware of when using the API.

#### 6.1. Authentication and Authorization

The API uses JSON Web Tokens (JWT) for authentication and authorization. Users must provide a valid JWT token in the `Authorization` header of their requests to access protected endpoints. The token is validated on each request, and if it is invalid or expired, the user will receive a 401 Unauthorized response.

The API also uses permission classes to control access to endpoints. The `IsAuthenticated` permission class ensures that only authenticated users can access protected endpoints.

#### 6.2. Throttling

To prevent abuse and ensure fair usage, the API has a throttling limit of 1000 requests per day for users. If a user exceeds this limit, they will receive a 429 Too Many Requests response.

#### 6.3. Data Encryption

The API uses HTTPS to encrypt data in transit. This ensures that all communication between the client and server is secure and cannot be intercepted or tampered with.

#### 6.4. Server Configuration

The API is configured to run on a secure server with the following settings:

* `ALLOWED_HOSTS`: This setting ensures that the API only accepts requests from the specified domain.
* `SECURE_SSL_REDIRECT = True`: This setting redirects all HTTP requests to HTTPS, ensuring that all communication is encrypted.
* `SECURE_HSTS_SECONDS = 31536000`: This setting enables HTTP Strict Transport Security (HSTS), which instructs the browser to only use HTTPS when communicating with the server.
* `SECURE_CONTENT_TYPE_NOSNIFF = True`: This setting prevents the browser from guessing the MIME type of a response, which can help prevent cross-site scripting (XSS) attacks.
* `SECURE_BROWSER_XSS_FILTER = True`: This setting enables the browser's XSS filter, which can help prevent XSS attacks.
* `SESSION_COOKIE_SECURE = True`: This setting ensures that session cookies are transmitted over a secure connection.
* `CSRF_COOKIE_SECURE = True`: This setting ensures that CSRF cookies are transmitted over a secure connection.