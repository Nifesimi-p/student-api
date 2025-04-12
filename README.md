# Student CRUD API

This is a Flask-based API for managing student data, implementing basic CRUD (Create, Read, Update, Delete) operations. The API uses SQLite as the database and SQLAlchemy for ORM (Object-Relational Mapping). The functionality allows you to add, retrieve, update, and delete student records. 

## Features
- **Create**: Add new students to the database.
- **Read**: Fetch all students or retrieve a specific student by their ID.
- **Update**: Modify an existing student's details.
- **Delete**: Remove a student from the database.

## Requirements

Before running the project, make sure you have the following installed:

- Python 3.x
- Flask
- SQLAlchemy
- Flask-Migrate
- Python-dotenv
- SQLite (for database)

### Installing Dependencies

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/student-crud-api.git
    cd student-crud-api
    ```

2. Create a virtual environment (if not already created):
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - For Windows:
      ```bash
      venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Setup

1. **Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add the following configuration to the `.env` file:
     ```bash
     DATABASE_URL=sqlite:///students.db
     ```

2. **Database Migrations**:
   - Initialize the database and run migrations:
     ```bash
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```

## API Endpoints

### 1. **Create a new student** (`POST /api/v1/students`)

- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "age": 22,
        "grade": "A"
    }
    ```
- **Response**:
    ```json
    {
        "message": "Student added"
    }
    ```

### 2. **Get all students** (`GET /api/v1/students`)

- **Response**:
    ```json
    [
        {
            "id": 1,
            "name": "John Doe",
            "age": 22,
            "grade": "A"
        },
        {
            "id": 2,
            "name": "Jane Smith",
            "age": 23,
            "grade": "B"
        }
    ]
    ```

### 3. **Get a specific student** (`GET /api/v1/students/{id}`)

- **URL Parameters**: `id` - ID of the student
- **Response**:
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "age": 22,
        "grade": "A"
    }
    ```

### 4. **Update a student** (`PUT /api/v1/students/{id}`)

- **URL Parameters**: `id` - ID of the student to update
- **Request Body**:
    ```json
    {
        "name": "Updated Name",
        "age": 25
    }
    ```
- **Response**:
    ```json
    {
        "message": "Student updated"
    }
    ```

### 5. **Delete a student** (`DELETE /api/v1/students/{id}`)

- **URL Parameters**: `id` - ID of the student to delete
- **Response**:
    ```json
    {
        "message": "Student deleted"
    }
    ```

### 6. **Healthcheck** (`GET /api/v1/healthcheck`)

- **Response**:
    ```json
    {
        "status": "ok"
    }
    ```

## Running the Application

To run the application in development mode:

1. Start the Flask application:
    ```bash
    flask run
    ```

2. The app will be available at `http://127.0.0.1:5000`.

## Logging

The application logs requests and errors using Python's built-in `logging` module. Logs are displayed in the terminal and include information such as the HTTP request details, database errors, and updates made to student records.

## Testing with Postman

1. Open [Postman](https://www.postman.com/).
2. Use the appropriate HTTP methods (`POST`, `GET`, `PUT`, `DELETE`) for testing each endpoint.
3. For the `POST` and `PUT` requests, include the required JSON body with student data.

## Contributing

Feel free to fork the repository, create a new branch, and submit a pull request with any improvements or fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
