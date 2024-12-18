# Webhook_API Documentation
This project consists of a set of API views for managing accounts and destinations in the webhook_app. It includes CRUD operations for accounts and destinations, as well as an endpoint for handling incoming data. The incoming data is authenticated by an API token and sent to multiple destinations via HTTP methods (GET, POST, PUT).

### Account CRUD Operations
#### 1. List and Create Accounts
- **Endpoint:** `/accounts/`
- **Method:** `GET`, `POST`
- **Description:**
  - `GET` - Retrieve a list of all accounts.
  - `POST` - Create a new account.
  - **Response (GET):**
  ```json
  [
      {
        "email_id": "baileyapril@gmail.com",
        "account_id": "fe048c06-2798-4f85-9133-5ff7109c6efc",
        "account_name": "Miller LLC",
        "website": "http://murray-ortiz.net/"
    },
     {
        "email_id": "alice.smith@gmail.com",
        "account_id": "05ec9d20-734e-493c-a7c3-548ce039261c",
        "account_name": "Alice Smit",
        "website": "https://www.alicesmith.com"
    }
  ]
  ```
   - **Request BODY (POST):**
  ```json
       {
        "email_id": "Johnsons@gmail.com",
        "account_name": "David & CO",
        "website": "http://johnsons&johnsons.net/"
       }
  ```
#### 2. Get , Update or Delete Accounts
- **Endpoint:** `/accounts/{account_id}`
- **Method:** `GET`, `PUT`,'DELETE'
- **Description:**
  - `GET` - Retrieve account based on account_id.
  - `PUT` - Update an account details.
  - 'DELETE' - Delete an account
  - **Response (GET):**
  ```json
    {
     "email_id": "baileyapril@gmail.com",
     "account_id": "fe048c06-2798-4f85-9133-5ff7109c6efc",
     "account_name": "Miller LLC",
     "website": "http://murray-ortiz.net/"
    }
  ```
  - **Request Body (PUT):**
  ```json
  {
  "account_name": "Miller LLC",
  "website": "http://murray-ortiz.net/"
  }
  ```
  - **Response for PUT:**
  ```json
      {
        "email_id": "baileyapril@gmail.com",
        "account_id": "fe048c06-2798-4f85-9133-5ff7109c6efc",
        "account_name": "Miller LLC",
        "website": "http://murray-ortiz.net/"
      }
  ```
  - **Response (DELETE):**
  ```json
    {
     "message": "Account deleted Successfully",
    }
  ```
### Destinations CRUD Operations
#### 1. List and Create Destinations
- **Endpoint:** `/destinations/<uuid:account_id>/`
- **Method:** `GET`, `POST`
- **Description:**
  - `GET` - Retrieve a list of all Destinations belongs to specific account_id.
  - `POST` - Create a new Destinations for the account_id.
  - **Response (GET):**
  ```json
  [
    {
        "id": 1,
        "url": "https://webhook.com/postdata",
        "http_method": "POST",
        "headers": {
            "APP_ID": "1234APPID1234",
            "Content-Type": "application/json"
        },
        "account": 1
    },
    {
        "id": 2,
        "url": "https://webhook.com/postdata",
        "http_method": "GET",
        "headers": {
            "ACTION": "user.update",
            "APP_ID": "1234APPID1234",
            "APP_SECTET": "enwdj3bshwer43bjhjs9ereuinkjcnsiurew8s",
            "Content-Type": "application/json"
        },
        "account": 1
    }
  ]
  ```
  -**Request BODY (POST):**
  ```json
  {
    "url": "https://webhook.example.com/endpoint",
    "http_method": "POST",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer abc123"
    }
  }
  ```
  -**Response :**
  ```json
  [
    {
        "id": 1,
        "url": "https://webhook.example.com/endpoint",
        "http_method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer abc123"
        },
        "account": "<account_id>"
    },
    {
        "id": 2,
        "url": "https://webhook.example2.com/endpoint",
        "http_method": "GET",
        "headers": {
            "Content-Type": "application/json"
        },
        "account": "<account_id>"
    }
  ]
  ```
### Incoming Data Sender
- **Endpoint:** `/servers/incoming)_data/`
- **Method:** `POST`,
- **Request Headers**:
  ```json
  {
  "CL-X-TOKEN" : "<app_secret_token>"
  }
  ```
- **Request Body (Data):**
 ```json
{
"username":"Michael Jackson",
"is_active":true
}
```
- **Response:**
```json
{
"message":"Data Sent Successfully!!"
}
```
- **Error Case 1: If the CL-X-TOKEN is not present in the headers**
```json
{
"message":"Un Authorized"
}
```
- **Error Case 2: If the CL-X-TOKEN is not valid(Account with the key is not present)**
```json
{
"message":"Invalid Token"
}
```
- **Error Case 3: If the Request Body is not in JSON Format**
```json
{
"message":"Invalid Data"
}
```


  
  
