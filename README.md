# README 
This project demonstrates how to implement a basic webhook. A **webhook** is a technique for sending real-time information from one application to another using HTTP POST requests.

In this example, the project includes two main components:
- **Server**: A Node.js server that receives webhook requests.
- **Client**: A Python script that sends data to the server.

## Project Structure

webhook-project/ ├── server/ # Folder for the Node.js server │ ├── package.json # Node.js configuration file │ ├── package-lock.json # Auto-generated file by npm │ └── app.js # Main server file ├── client/ # Folder for the Python client │ └── send_webhook.py # Script to send webhook requests └── README.md # Project documentation


## Component Overview

### 1. Node.js Server
The server is designed to listen for POST requests on the `/webhook` endpoint and log the received data to the console. It uses the **Express** framework to handle HTTP requests.

#### File: `server/app.js`
This file contains:
- Basic server configuration.
- An endpoint to listen for webhook requests.
- A response to confirm the receipt of data.

**Technologies Used:**
- Node.js
- Express

### 2. Python Client
The client is a Python script that sends simulated data (e.g., user registration information) to the server via an HTTP POST request. The data is sent in JSON format.

#### File: `client/send_webhook.py`
This file contains:
- The data payload to be sent to the server (e.g., ID, name, email, registration date).
- Logic for making an HTTP POST request to the server.

**Libraries Used:**
- requests

## Instructions to Run the Project

### 1. Setting Up and Running the Server
1. Navigate to the `server/` directory:
   ``` 
   bash
   cd server

2. Install the required Node.js dependencies:
``` npm install```

3. Start the server:

```npm start```

4. The server will listen on http://localhost:3000/webhook.

# Setting Up and Running the Client
1. Make sure Python 3 is installed.
2. Navigate to the client/ directory: ```cd client```
3. Run the Python script:  ```python send_webhook.py```
4. If successful, you will see a success message in the client terminal and the received data logged in the server terminal.

# Example Data Sent

The client sends a JSON payload with the following structure:

{

    "id": 123,

    "name": "John Doe",

    "email": "john.doe@example.com",

    "registered_at": "2025-01-12T10:00:00Z"

}

# Server Response
The server logs the received data and responds to the client with:


{
   ``` 
"Server listening on http://localhost:3000
Webhook received xavi: {

id: 123,
name: 'John Doe',

email: 'john.doe@example.com',

registered_at: '2025-01-12T10:00:00Z'
```

}








