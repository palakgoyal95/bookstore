Month5-Project Title: Bookstore Management System - REST API Development (Python)
Client Overview
The client is a bookstore owner looking to develop a backend system that can manage books, users
(both customers and admins), and orders through a set of RESTful APIs. The goal is to provide an
efficient system for browsing books, registering users, handling orders, and tracking inventory.

Project Objective
To develop a set of RESTful APIs using Python (Django REST Framework) that will enable the
management of books, user authentication, and order processing. The system will allow customers
to browse and purchase books, while admins can manage inventory and process orders. The API will
interact with a relational or NoSQL database to store book, user, and order data.

Backend Requirements
1. Book Management
• API Endpoints:
o GET /api/books: Retrieve a list of all books
o GET /api/books/{id}: Retrieve details of a single book
o POST /api/books: Add a new book to the inventory
o PUT /api/books/{id}: Update an existing book's details (e.g., price, stock)
o DELETE /api/books/{id}: Delete a book from the inventory
• Book Details:
o Title
o Author(s)
o Genre
o ISBN
o Price
o Description
o Stock Quantity
o Image URL (cover image)

2. User Authentication
• API Endpoints:
o POST /api/register: Register a new user (Customer or Admin)

o POST /api/login: Authenticate an existing user and return a JWT token
• User Details:
o Name
o Email
o Password (hashed and securely stored)
o Role (Customer or Admin)
• Security:
o Use JWT (JSON Web Token) for user authentication
o Implement role-based access control (Only Admins can manage books)

3. Order Management
• API Endpoints:
o GET /api/orders: Retrieve all orders (Admin only)
o GET /api/orders/{id}: Retrieve a single order
o POST /api/orders: Place a new order (Customer only)
o PUT /api/orders/{id}/status: Update order status (Admin only)
• Order Details:
o User info (Name, Email)
o List of books (title, quantity, price)
o Order Status (Pending, Shipped, Delivered)
o Payment Status (mock or real integration depending on scope)

4. Database Integration
• Use PostgreSQL, MySQL, or MongoDB
• Relationships:
o One-to-many (User → Orders)
o Many-to-many (Order ↔ Books with quantities)
• Support queries like:
o Search books by title/author/genre
o Filter order history per user

5. Performance and Pagination
• Implement pagination on:
o Book list endpoint
o Order list endpoint
• Implement search functionality for:
o Book title
o Book author

6. Error Handling
• Return meaningful error messages:
o 404 Not Found (e.g., for missing book or order)
o 401 Unauthorized (JWT expired or missing)
o 400 Bad Request (Validation errors)
o 500 Internal Server Error (Unhandled exceptions)

7. API Documentation
• Use Swagger/OpenAPI (via drf-yasg or drf-spectacular)
• Documentation should include:
o Endpoints, request formats, example responses
o Auth token usage
o Error response examples

Project Timeline
Week Task
Week
1
Set up Django REST Framework, configure PostgreSQL/MySQL/MongoDB, implement JWT
authentication
Week
2
Develop Book Management APIs (CRUD), implement search and pagination
Week
3
Develop Order Management APIs and tie them to users and books

Week Task
Week
4
Add error handling, finalize Swagger documentation, and write unit/API tests

Deliverables
1. Fully functional REST API using Python (Django REST Framework)
2. Database Integration with MySQL, PostgreSQL, or MongoDB
3. JWT-secured endpoints for authentication and authorization
4. Swagger-based API Documentation
5. Unit tests and Postman collections for all key endpoints

Evaluation Criteria
• Functionality: API supports book management, user registration, login, and order processing
• Security: Role-based access, JWT implementation
• Code Quality: Clear, well-structured, and commented Python code
• Performance: Optimized queries with pagination and filtering
• Creativity: Additional features (e.g., book reviews, real payment system)

Technologies
• Backend: Python, Django REST Framework
• Database: PostgreSQL / MySQL / MongoDB
• Authentication: JWT (using djangorestframework-simplejwt)
• Security: Django Permissions and Role-based access
• Documentation: Swagger (drf-yasg or drf-spectacular)
• Testing: Pytest, Django TestCase, Postman

Optional Enhancements
• Payment Integration: Stripe or Razorpay for real payments
• Book Reviews: Customers can leave reviews and star ratings
• Admin Dashboard: Admin interface for managing books and orders (using Django Admin or a
separate React/Vue dashboard)

Summary
This Bookstore Management System REST API project will give students hands-on experience in:
• Full REST API lifecycle
• JWT authentication
• Role-based security
• ORM and database relationships
• Pagination and filtering
• Auto-generated API documentation
• Testing and error handling
