# Banking Dashboard Developer Test

## Overview

Welcome to our developer test! This project aims to evaluate your skills in creating a banking dashboard with admin access. You'll be working with a mock Banking as a Service (BaaS) API located at https://mocktest-october.justtestingthis.com.

## Objective

Your task is to create a banking dashboard that allows administrators to:

1. View and create bank accounts
2. View account statements
3. See a summary of open accounts
4. View the total balance of all accounts (simulating the total value in the database)

Additionally, as a bonus feature, you can create a user interface for account holders to:

1. Log in to their bank account
2. Perform financial operations
3. View their account statement and balance

## Evaluation Criteria

We will assess your solution based on:

1. Security
2. Usability
3. Performance
4. Scalability

If you're a full-stack developer, we'll evaluate both your backend and frontend implementations. If you specialize in one area, we'll place more emphasis on your expertise.

Careful consideration of caching and security measures is crucial for both frontend and backend components.

## Technology Stack

### Frontend
- React (with Next.js, Remix, or similar)
- Svelte

Recommended libraries:
- Tailwind CSS for styling
- shadcn for UI components
- Framer Motion for animations

### Backend
- Python
- TypeScript (Node.js, Bun, or Deno)

Recommended framework:
- NestJS

### Database
Your choice, including free options like Supabase

## API Documentation

The mock BaaS API is available at https://mocktest-october.justtestingthis.com. Here's an overview of the available endpoints and their usage:

### Important Notes
- You must create a tenant before accessing other routes.
- The JWT secret is: `758603a3-cb1c-4d3f-b4b4-aa8975236894`
- The pix key is: `pix@mock.icabank.com.br`

### Authentication

#### Create Tenant
- **POST** `/tenant`
- **Headers**: `X-Mock: true`
- **Response**: Returns tenant details including `clientId` and `clientSecret`

#### Login
- **POST** `/auth/login`
- **Body**: 
  ```json
  {
    "clientId": "your_client_id",
    "clientSecret": "your_client_secret"
  }
  ```
- **Response**: Returns an `access_token`

### Account Management

All account management routes require the following header:
- `Authorization: Bearer your_access_token`

#### Create Account
- **POST** `/account`
- **Body**:
  ```json
  {
    "accountType": "PERSONAL" | "BUSINESS",
    "name": "Account Holder Name",
    "document": "Document Number"
  }
  ```

#### Get Account Details
- **GET** `/account/:id`

#### Get Account Statement
- **GET** `/account/:id/statement`

### Transactions

All transaction routes require the following headers:
- `Authorization: Bearer your_access_token`
- `X-Payer-Id: payer_document_number`

#### TED Transfer
- **POST** `/transaction/ted`
- **Body**:
  ```json
  {
    "accountId": "source_account_id",
    "amount": 500,
    "recipientName": "Recipient Name",
    "recipientDocument": "Recipient Document",
    "recipientBank": "Bank Code",
    "recipientBranch": "Branch Number",
    "recipientAccount": "Account Number"
  }
  ```

#### PIX Transfer
- **POST** `/transaction/pix/:accountId/pay`
- **Body**:
  ```json
  {
    "amount": 200,
    "pixKey": "pix@example.com",
    "e2eId": "end_to_end_id"
  }
  ```

#### Pay Billet
- **POST** `/transaction/billet`
- **Body**:
  ```json
  {
    "accountId": "source_account_id",
    "amount": 150,
    "billetCode": "billet_code",
    "dueDate": "YYYY-MM-DD"
  }
  ```

#### Internal Transfer
- **POST** `/transaction/internal`
- **Body**:
  ```json
  {
    "amount": 100,
    "sourceAccountId": "source_account_id",
    "targetAccountId": "target_account_id"
  }
  ```

## Submission Guidelines

1. Create a GitHub repository for your project.
2. Include clear instructions on how to set up and run your solution.
3. Provide any necessary documentation for your code and architecture decisions.
4. Submit the link to your repository when you're ready for review.

Good luck, and we look forward to seeing your innovative solutions!
