# BookStore

## Description

A RESTful API for an online bookstore that provides comprehensive book management, user authentication, and order processing functionality. The system allows users to browse books, filter by various criteria, manage shopping carts, and track order history.

## Features

- Book catalog with advanced search and filtering
- Author and publisher management
- User authentication and authorization
- Shopping cart functionality
- Order management
- User profiles with order history

## API Endpoints

### Authentication

#### Register User
- **POST** `/api/auth/register`
- **Description**: Create a new user account
- **Request Body**:
```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "first_name": "string",
  "last_name": "string"
}
```
- **Response**: `201 Created`
```json
{
  "id": 1,
  "username": "string", 
  "email": "string",
  "token": "string"
}
```

#### Login
- **POST** `/api/auth/login`
- **Description**: Authenticate user and receive token
- **Request Body**:
```json
{
  "username": "string",
  "password": "string"
}
```
- **Response**: `200 OK`
```json
{
  "token": "string",
  "user_id": 1
}
```

#### Logout
- **POST** `/api/auth/logout`
- **Description**: Invalidate user token
- **Headers**: `Authorization: Token <token>`
- **Response**: `204 No Content`

### Books

#### List Books
- **GET** `/api/books`
- **Description**: Get paginated list of books with filtering and sorting
- **Query Parameters**:
  - `search` (string): Search by title or author name
  - `genre` (string): Filter by genre
  - `publisher` (integer): Filter by publisher ID
  - `min_price` (decimal): Minimum price filter
  - `max_price` (decimal): Maximum price filter
  - `ordering` (string): Sort by `price`, `-price`, `popularity`, `genre`
  - `page` (integer): Page number
  - `limit` (integer): Items per page
- **Response**: `200 OK`
```json
{
  "count": 100,
  "next": "http://api/books?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "string",
      "author": {
        "id": 1,
        "name": "string"
      },
      "price": 0.5,
      "genre": "string",
      "cover_image": "url"
    }
  ]
}
```

#### Get Book Details
- **GET** `/api/books/{id}`
- **Description**: Get detailed information about a specific book
- **Response**: `200 OK`
```json
{
  "id": 1,
  "title": "string",
  "author": {
    "id": 1,
    "name": "string",
    "biography": "string"
  },
  "publisher": {
    "id": 1,
    "name": "string"
  },
  "isbn": "string",
  "description": "string",
  "price": 32.1,
  "genre": "string",
  "publication_year": 2013,
  "pages": 363,
  "language": "string",
  "stock_quantity": 10,
  "cover_image": "url"
}
```

#### Create Book (Admin only)
- **POST** `/api/books`
- **Description**: Add a new book to the catalog
- **Headers**: `Authorization: Token <admin_token>`
- **Request Body**:
```json
{
  "title": "string",
  "author_id": 1,
  "publisher_id": 1,
  "isbn": "string",
  "description": "string",
  "price": 19.99,
  "genre": "string",
  "publication_year": 2020,
  "pages": 332,
  "language": "string",
  "stock_quantity": 12
}
```
- **Response**: `201 Created`

#### Update Book (Admin only)
- **PUT** `/api/books/{id}`
- **Description**: Update book information
- **Headers**: `Authorization: Token <admin_token>`
- **Request Body**: Same as Create Book
- **Response**: `200 OK`

#### Delete Book (Admin only)
- **DELETE** `/api/books/{id}`
- **Description**: Remove book from catalog
- **Headers**: `Authorization: Token <admin_token>`
- **Response**: `204 No Content`

### Authors

#### List Authors
- **GET** `/api/authors`
- **Description**: Get list of all authors
- **Response**: `200 OK`
```json
[
  {
    "id": 1,
    "name": "string",
    "biography": "string",
    "birth_year": 1992,
    "nationality": "string"
  }
]
```

#### Get Author Details
- **GET** `/api/authors/{id}`
- **Description**: Get author details with their books
- **Response**: `200 OK`
```json
{
  "id": 1,
  "name": "string",
  "biography": "string",
  "birth_year": 1913,
  "nationality": "string",
  "books": [
    {
      "id": 1,
      "title": "string",
      "price": 2.0,
      "genre": "string"
    }
  ]
}
```

#### Create Author (Admin only)
- **POST** `/api/authors`
- **Headers**: `Authorization: Token <admin_token>`
- **Request Body**:
```json
{
  "name": "string",
  "biography": "string",
  "birth_year": 2000,
  "nationality": "string"
}
```
- **Response**: `201 Created`

#### Update Author (Admin only)
- **PUT** `/api/authors/{id}`
- **Headers**: `Authorization: Token <admin_token>`
- **Response**: `200 OK`

#### Delete Author (Admin only)
- **DELETE** `/api/authors/{id}`
- **Headers**: `Authorization: Token <admin_token>`
- **Response**: `204 No Content`

### Publishers

#### List Publishers
- **GET** `/api/publishers`
- **Description**: Get list of all publishers
- **Response**: `200 OK`
```json
[
  {
    "id": 1,
    "name": "string",
    "description": "string",
    "website": "string"
  }
]
```

#### Get Publisher Details
- **GET** `/api/publishers/{id}`
- **Description**: Get publisher details with their books
- **Response**: `200 OK`
```json
{
  "id": 1,
  "name": "string",
  "description": "string",
  "website": "string",
  "books": [
    {
      "id": 1,
      "title": "string",
      "author_name": "string",
      "price": 12.32
    }
  ]
}
```

#### Create Publisher (Admin only)
- **POST** `/api/publishers`
- **Headers**: `Authorization: Token <admin_token>`
- **Request Body**:
```json
{
  "name": "string",
  "description": "string",
  "website": "string"
}
```
- **Response**: `201 Created`

#### Update Publisher (Admin only)
- **PUT** `/api/publishers/{id}`
- **Headers**: `Authorization: Token <admin_token>`
- **Response**: `200 OK`

#### Delete Publisher (Admin only)
- **DELETE** `/api/publishers/{id}`
- **Headers**: `Authorization: Token <admin_token>`
- **Response**: `204 No Content`

### Shopping Cart

#### Get Cart
- **GET** `/api/cart`
- **Description**: Get current user's cart
- **Headers**: `Authorization: Token <token>`
- **Response**: `200 OK`
```json
{
  "id": 1,
  "items": [
    {
      "id": 1,
      "book": {
        "id": 1,
        "title": "string",
        "price": 13.75
      },
      "quantity": 2,
      "subtotal": 59.98
    }
  ],
  "total": 59.98
}
```

#### Add to Cart
- **POST** `/api/cart/items`
- **Description**: Add book to cart
- **Headers**: `Authorization: Token <token>`
- **Request Body**:
```json
{
  "book_id": 1,
  "quantity": 2
}
```
- **Response**: `201 Created`

#### Update Cart Item
- **PUT** `/api/cart/items/{id}`
- **Description**: Update quantity of item in cart
- **Headers**: `Authorization: Token <token>`
- **Request Body**:
```json
{
  "quantity": 3
}
```
- **Response**: `200 OK`

#### Remove from Cart
- **DELETE** `/api/cart/items/{id}`
- **Description**: Remove item from cart
- **Headers**: `Authorization: Token <token>`
- **Response**: `204 No Content`

#### Clear Cart
- **DELETE** `/api/cart`
- **Description**: Remove all items from cart
- **Headers**: `Authorization: Token <token>`
- **Response**: `204 No Content`

### Orders

#### Create Order
- **POST** `/api/orders`
- **Description**: Create order from current cart
- **Headers**: `Authorization: Token <token>`
- **Response**: `201 Created`
```json
{
  "id": 1,
  "order_number": "ORD-2025-001",
  "created_at": "2025-09-30T10:00:00Z",
  "status": "pending",
  "total": 59.75,
  "items": [
    {
      "book_title": "string",
      "quantity": 2,
      "price": 53.3,
      "subtotal": 59.74
    }
  ]
}
```

#### List User Orders
- **GET** `/api/orders`
- **Description**: Get authenticated user's order history
- **Headers**: `Authorization: Token <token>`
- **Response**: `200 OK`
```json
[
  {
    "id": 1,
    "order_number": "ORD-2025-001",
    "created_at": "2025-01-30T10:00:00Z",
    "status": "delivered",
    "total": 59.75
  }
]
```

#### Get Order Details
- **GET** `/api/orders/{id}`
- **Description**: Get specific order details
- **Headers**: `Authorization: Token <token>`
- **Response**: `200 OK`

### User Profile

#### Get Profile
- **GET** `/api/profile`
- **Description**: Get authenticated user's profile
- **Headers**: `Authorization: Token <token>`
- **Response**: `200 OK`
```json
{
  "id": 1,
  "username": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "phone": "string",
  "address": "string"
}
```

#### Update Profile
- **PUT** `/api/profile`
- **Description**: Update user profile information
- **Headers**: `Authorization: Token <token>`
- **Request Body**:
```json
{
  "first_name": "string",
  "last_name": "string",
  "phone": "string",
  "address": "string"
}
```
- **Response**: `200 OK`

### Static Pages

#### About Us
- **GET** `/api/about`
- **Description**: Get information about the bookstore
- **Response**: `200 OK`
```json
{
  "description": "string",
  "contact_info": {
    "phone": "string",
    "email": "string",
    "address": "string"
  },
  "delivery_info": "string",
  "return_policy": "string"
}
```

## Database Schema

![Database Schema](database_schema.png)

## HTTP Status Codes

- `200 OK` - Request succeeded
- `201 Created` - Resource created successfully
- `204 No Content` - Request succeeded with no content to return
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Access denied
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Authentication

The API uses token-based authentication. Include the token in the Authorization header:
```
Authorization: Token <your_token_here>
```

## Technologies

- Django REST Framework
- PostgreSQL
- Token Authentication
```