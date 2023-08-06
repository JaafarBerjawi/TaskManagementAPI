# Task Management API
This project is a Task Management Web API that allows users to get manage tasks. The API also includes user registration and token-based authentication.

## Table of Contents
- Project Overview
- Technologies Used
- Project Structure
- Installation and Setup
- API Endpoints
- Testing
- Additional Features
- Known Issues or Limitations

### Project Overview
The Task Management Web API provides the following functionalities:

- **Create Tasks:** Authenticated users can create tasks by sending a POST request to the **/tasks** endpoint.
- **Get Tasks:** Authenticated users can retrieve their tasks by sending a GET request to the **/tasks** endpoint.
- **Get a Specific Task:** Authenticated users can retrieve a specific task by sending a GET request to the **/tasks/{task_id}** endpoint. 
- **Update Tasks:** Authenticated users can update a task by sending a PUT request to the **/tasks/{task_id}** endpoint.
- **Delete Task:** Authenticated users can delete a task by sending a DELETE request to the **/tasks/{task_id}** endpoint.

Users need to be authenticated to access endpoints before.

- **User Registration:** Users can register with the API by sending a POST request to the **/create_user** endpoint.

- **Token-based Authentication:** The API uses token-based authentication to secure specific endpoints. Users can obtain an authentication token by sending a POST request to the **/authenticate** endpoint.

### Technologies Used
The project is built using the following technologies and frameworks:

- Pyhton 3.8
- Flask 2.3.2
- SQL Alchemy 2.0.19
- Flask Injector 0.15.0
- psycopg2 2.9.6
- Flask Migrate 4.0.4

### Project Structure
The project consists of the following main components:

1. **Security:** Contains authentication-related code and business logic.
  
    - **UserService:** Responsible for user registration.
    - **TokenService:** Responsible for token generation and validation.
    - ***UserDataManager:** Data manager for users using SQLAlchemy.
    - ***UserTokenDataManager:** Data manager for user tokens using SQLAlchemy.
    - **User and UserToken:** Entities for representing user information and authentication tokens.
    - **EncryptionService:** Service for hashing passwords and tokens.

 2. **TaskManagement:** Contains task-related code and business logic.

    - **TaskService:** Service to handle task business logic.
    - **TaskController:** Controller layer to expose task management functionalities.
    - **TaskDataManager:** Data manager for tasks using SQLAlchemy.
    - **Task:** Entity for representing a task.

3. **Data:** Contains data access code and abstract classes for database interactions.
  
    - **UserDataManagerABC:** Abstract class for user data operations.
    - **UserTokenDataManagerABC:** Abstract class for user token data operations.
    - **TaskDataManagerABC:** Abstract class for task management data operations.
      Each of these abstract classes, has implemenations for testing and running.

4. **Data.Mock:** Contains mock data managers used for testing.
  
    - **UserDataManager:** Mock data manager for users.
    - **UserTokenDataManager:** Mock data manager for user tokens.
    - **TaskDataManager:** Mock data manager for task data.

5. **Controllers:** Contains API controllers.

    - **UserController:** Controller for user registration.
    - **UserTokenController:** Controller for token generation.
    - **TaskController:** Controller for task-related endpoints.

6. **Testing:** Contains unit tests for the API.
    
    - **AppTestCase:** Contains unit tests for the Task Management and Security services.
    
### Installation and Setup
To run the TaskManagement Web API, follow these steps:

- Ensure you have the python 3.8 installed on your machine.
- Clone this repository to your local machine.
- Open the solution in pycharm or your favorite code editor.

### Database Configuration
1. Open the config.py file and update the connection string to your Postgres SQL Server database.
```
    password = "{YOUR_SERVER_PASSWORD}"
    encoded_password = urllib.parse.quote(password)

    connection_string = f"postgresql://postgres:{encoded_password}{YOUR_SERVER_URI}/task_manager"
```
2. Open the Terminal and run the following command to apply the migrations and create the database:
```
flask db upgrade
```
### Running the API
1. Run the TaskManagement Web API project (app.py) from pycharm or your code editor.

2. The API will be hosted at https://localhost:portNumber/.

### API Endpoints
The following endpoints are available in the TaskManagement Web API:

#### Authentication
- **POST /users:** Register a new user. Requires a JSON body containing Username and Password.

- **POST /authenticate:** Generate an authentication token for an existing user. Requires a JSON body containing Username and Password.

#### Task Information
- **GET /tasks:** Get the user's saved tasks.
- **GET /tasks/{task_id}:** Get a specific user's task.
- **POST /tasks:** Creates a task for the user. Requires a JSON body containing title(required), description and completed.
- **PUT /tasks/{task_id}:** Updates the task with the id specified. Requires a JSON body containing title(required), description and completed.
- **Delete /tasks/{task_id}:** deletes the task with the id specified.


### Testing
The project includes unit tests. You can run the tests by executing the following command in the Package Manager Console:
```
python -m unittest test_app.py
```
### Additional Features
1. **Security Module Reusability:** The Security module has been designed to be reusable across other applications. This module can be extracted and shared with other projects to handle user authentication.
2. **Data Storage per User:** The tasks are stored in the database on a per-user basis. Each user can manage their tasks, and the data is segregated based on the user's identity.
3. **User ID from Token:** The user ID for each request is extracted from the token by the authentication middleware. This user ID is used to associate tasks with the respective user in the database.

### Known Issues or Limitations
As of the current implementation, the solution has the following limitations:

- **Security Considerations:** While the solution includes password hashing and token-based authentication, there could be additional security considerations to address for production deployment, such as rate limiting, SSL certificates, etc.
- **Unit Test Coverage:** While the project includes unit tests for core services and controllers, there may be areas where additional test coverage could be beneficial for further validation.
- **User Authentication Mechanism:** The current solution uses a simple username and password-based authentication mechanism. In a real-world scenario, more robust and secure authentication methods, such as OAuth, should be considered.
- **Logging Functionality:** The current solution only implements exception logging functionality. Implementing proper logging would help in debugging and tracking issues, providing insights into application behavior and performance.
- **Entities History:** The application entities do not have CreatedTime, CreatedBy, LastModifiedTime, and LastModifiedBy fields to track entities' history. Adding these fields would enable auditing and historical tracking of changes to entities.
