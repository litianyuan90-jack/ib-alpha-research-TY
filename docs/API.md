# API Documentation

## Overview
This document provides comprehensive API documentation for the IB Alpha Research system. It includes all available endpoints, their parameters, expected responses, and usage examples.

## Endpoints

### 1. Get User Information
- **Endpoint:** `/api/users/{id}`  
- **Method:** `GET`  
- **Description:** Fetches user details by user ID.

#### Parameters:
- `id` (path) - The ID of the user to fetch.

#### Responses:
- **200 OK**  
  ```json
  {
    "id": "123",
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```
- **404 Not Found**  
  ```json
  { "error": "User not found" }
  ```

#### Usage Example:
```bash
curl -X GET http://api.example.com/api/users/123
```

### 2. Create New User
- **Endpoint:** `/api/users`  
- **Method:** `POST`  
- **Description:** Creates a new user in the system.

#### Parameters:
- `name` (body) - The name of the user.
- `email` (body) - The email of the user.

#### Request Body Example:
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

#### Responses:
- **201 Created**  
  ```json
  {
    "id": "124",
    "name": "Jane Doe",
    "email": "jane@example.com"
  }
  ```

#### Usage Example:
```bash
curl -X POST http://api.example.com/api/users -H "Content-Type: application/json" -d '{"name": "Jane Doe", "email": "jane@example.com"}'
```

### 3. Update User Information
- **Endpoint:** `/api/users/{id}`  
- **Method:** `PUT`  
- **Description:** Updates information for an existing user.

#### Parameters:
- `id` (path) - The ID of the user to update.
- `name` (body) - The new name of the user.
- `email` (body) - The new email of the user.

#### Request Body Example:
```json
{
  "name": "Jane Smith",
  "email": "jane.smith@example.com"
}
```

#### Responses:
- **200 OK**  
  ```json
  {
    "id": "124",
    "name": "Jane Smith",
    "email": "jane.smith@example.com"
  }
  ```

#### Usage Example:
```bash
curl -X PUT http://api.example.com/api/users/124 -H "Content-Type: application/json" -d '{"name": "Jane Smith", "email": "jane.smith@example.com"}'
```

### 4. Delete User
- **Endpoint:** `/api/users/{id}`  
- **Method:** `DELETE`  
- **Description:** Deletes a user from the system.

#### Parameters:
- `id` (path) - The ID of the user to delete.

#### Responses:
- **204 No Content**  

#### Usage Example:
```bash
curl -X DELETE http://api.example.com/api/users/124
```

## Conclusion
This document provides a comprehensive overview of the available API endpoints for the IB Alpha Research system. Please refer to each section for detailed information on endpoints, expected parameters, and response formats.