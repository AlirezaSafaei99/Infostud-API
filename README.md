# FastAPI User Management Application

This project is a simple FastAPI application that provides an API for managing user data. It uses SQLAlchemy for interacting with a PostgreSQL database and includes basic CRUD operations (Create, Read, Update, Delete) for users. The API is designed to be modular, with separate files handling different aspects of the application such as configuration, database management, user operations, and API routing.

## Features

- Asynchronous database interactions using SQLAlchemy.
- User CRUD operations (Create, Read, Update, Delete).
- Database connection configuration via a YAML file.
- Swagger UI documentation for easy API testing and interaction.


## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database**:

    If you want to use Docker to run PostgreSQL, you can use the provided `docker-compose.yml` file to start the database:

    ```bash
    docker-compose up -d
    ```

    This will start the PostgreSQL service and map it to port 6543.

    Alternatively, you can set up PostgreSQL locally and update the `config.yaml` file with your local database connection details.

## Running the Application

1. **Start the FastAPI application**:

    Once the dependencies are installed and the database is set up, you can start the FastAPI server with:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the application at `http://127.0.0.1:8000`.

2. **Access the Swagger UI**:

    The FastAPI app automatically generates interactive documentation using Swagger UI. Open the following URL in your browser to test the API endpoints:

    ```
    http://127.0.0.1:8000/docs
    ```

3. **ReDoc UI**:

    Alternatively, you can view the API documentation using ReDoc:

    ```
    http://127.0.0.1:8000/redoc
    ```

## API Endpoints

Here are the available API routes:

### **Ping Route**

- **GET** `/ping`
  - Returns a simple "pong" response to verify the API is up and running.

### **User Routes**

- **POST** `/users`
  - Create a new user with the provided data.
  - Request body: A JSON object with user details (e.g., name, email, password).
  - Response: Created user data.

- **GET** `/user/{user_id}`
  - Fetch user details by ID.
  - Response: The user data (name, email, etc.).

- **GET** `/users`
  - Fetch all users from the database.
  - Response: A list of all users.

- **PUT** `/users/{user_id}`
  - Update user details by their ID.
  - Request body: JSON object with updated user data.
  - Response: Updated user data.

- **DELETE** `/delete-users/{user_id}`
  - Delete a user by their ID.
  - Response: Deleted user data.

### Next Steps:
- If you need more specific sections, such as environment variable configuration or deployment instructions, feel free to let me know.
- If you already have a specific section like a testing guide or API examples, I can add those as well.

Let me know if you need any further adjustments!
