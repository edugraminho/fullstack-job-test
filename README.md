# Banking Dashboard Developer Test

## Architectural Design

The architectural design is based on best practices for organizing FastAPI applications in a modular and scalable structure, but adapted for smaller projects and without databases.

## FastAPI

FastAPI is the framework used to build the API. The architecture is asynchronous, which optimizes performance in I/O operations, such as external calls to other APIs. The API offers endpoints organized into modules, which makes it easy to add new features.

## Redis

Redis is used as an in-memory cache layer for temporary storage of authentication tokens such as JWT tokens, with predefined expiration times, increasing security.

## Docker

Docker is used to containerize the entire application, ensuring portability and consistency between development and production environments. The project also uses Docker Compose to manage multiple containers, allowing the FastAPI and Redis applications to run in isolated containers.

# API Documentation

### Requirements

`Docker installed`
`Docker Compose installed`

### How to Run the Project:

1- Clone the repository.

2- Configure environment variables. Create a .env file in the project root, copying env.example and adding the credentials

3- Run `docker-compose up` to start the application and Redis.
Access the API and automatic documentation at `http://localhost:8000/docs`.

### Authentication Routes

#### Login

- **POST** `/auth/login`

This route creates a tenant, logs in to the Banking as a Service (BaaS) API, and stores the access token in Redis.

**Success Response**:

```json
{
  "message": "Login successful",
  "access_token": "<access_token>"
}
```

### Account Routes

#### Create Account

- **POST** `/accounts/`

This route allows the creation of a new account.

**Request Body:**

```json
{
  "accountType": "PERSONAL" | "BUSINESS",
  "name": "string",
  "document": "string"
}
```

**Success Response**:

```json
{
  "accountId": "string",
  "tenantId": "string",
  "accountType": "PERSONAL",
  "name": "string",
  "document": "string",
  "status": "PENDING_KYC",
  "balance": 0,
  "branch": "0001",
  "number": "string",
  "createdAt": "2024-10-05T14:21:03.960Z",
  "updatedAt": "2024-10-05T14:21:03.960Z"
}
```

#### Get Account Details

**GET** `/accounts/{account_id}`

This route allows retrieving the details of a specific account.

Path Parameters:

account_id: UUID of the account
**Success Response**:

```json
{
  "id": "string",
  "tenantId": "string",
  "accountType": "PERSONAL",
  "name": "string",
  "document": "string",
  "status": "ACTIVE",
  "balance": 1000.0,
  "branch": "0001",
  "number": "42069",
  "createdAt": "2024-10-05T14:21:03.960Z",
  "updatedAt": "2024-10-05T14:21:03.960Z"
}
```

#### Get Account Statement

**GET** `/accounts/{account_id}/statement`

This route allows retrieving the statement of a specific account.

Path Parameters:

account_id: UUID of the account
**Success Response**:

```json
{
  "accountId": "string",
  "balance": "float",
  "transactions": [
    {
      "id": "string",
      "accountId": "string",
      "type": "INTERNAL",
      "amount": 2677,
      "description": "string",
      "recipientName": "string",
      "recipientDocument": "string",
      "recipientBank": "string",
      "recipientBranch": "string",
      "recipientAccount": "string",
      "billetCode": null,
      "pixKey": null,
      "e2eId": null,
      "createdAt": "2024-10-05T15:39:35.000Z"
    }
  ]
}
```

### Transaction Routes

#### TED Transfer

- **POST** `/transaction/ted`

This route allows performing a TED transfer.

**Request Body:**

```json
{
  "accountId": "string",
  "amount": 500,
  "recipientName": "string",
  "recipientDocument": "string",
  "recipientBank": "string",
  "recipientBranch": "string",
  "recipientAccount": "string",
  "description": "string"
}
```

**Success Response**:

```json
{
  "message": "TED Transfer Successful"
}
```

#### PIX Transfer

- **POST** `/transaction/pix/{account_id}/pay`

This route allows performing a PIX transfer.

Path Parameters:

account_id: UUID of the account
**Request Body:**

```json
{
  "amount": 200,
  "pixKey": "pix@example.com",
  "e2eId": "end_to_end_id",
  "description": "string"
}
```

**Success Response**:

```json
{
  "message": "PIX Transfer Successful"
}
```

#### Billet Payment

- **POST** `/transaction/billet`

This route allows paying a billet (bank slip).

**Request Body:**

```json
{
  "accountId": "string",
  "amount": 100.0,
  "billetCode": "111",
  "dueDate": "2024-10-25"
}
```

**Success Response**:

```json
{
  "accountId": "string",
  "type": "string",
  "amount": 100,
  "billetCode": "string",
  "account": {
    "id": "string",
    "tenantId": "string",
    "accountType": "PERSONAL",
    "name": "string",
    "document": "string",
    "status": "ACTIVE",
    "balance": 7193,
    "branch": "string",
    "number": "string",
    "createdAt": "2024-10-05T15:07:35.000Z",
    "updatedAt": "2024-10-05T15:13:36.000Z"
  },
  "description": null,
  "recipientName": null,
  "recipientDocument": null,
  "recipientBank": null,
  "recipientBranch": null,
  "recipientAccount": null,
  "pixKey": null,
  "e2eId": null,
  "id": "string",
  "createdAt": "2024-10-05T15:32:32.000Z"
}
```

#### Internal Transfer

- **POST** `/transaction/internal`

This route allows performing an internal transfer between accounts.

**Request Body:**

```json
{
  "sourceAccountId": "string",
  "targetAccountId": "string",
  "amount": 100.0
}
```

**Success Response**:

```json
{
  "accountId": "string",
  "type": "INTERNAL",
  "amount": -100,
  "recipientBank": "string",
  "recipientBranch": "string",
  "recipientAccount": "string",
  "account": {
    "id": "string",
    "tenantId": "string",
    "accountType": "PERSONAL",
    "name": "string",
    "document": "string",
    "status": "ACTIVE",
    "balance": 7293,
    "branch": "string",
    "number": "string",
    "createdAt": "2024-10-05T15:07:35.000Z",
    "updatedAt": "2024-10-05T15:34:30.000Z"
  },
  "description": null,
  "recipientName": null,
  "recipientDocument": null,
  "billetCode": null,
  "pixKey": null,
  "e2eId": null,
  "id": "string",
  "createdAt": "2024-10-05T15:34:33.000Z"
}
```
