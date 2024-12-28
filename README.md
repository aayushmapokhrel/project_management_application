Project Management Application Documentation

Database Plan

The project management application is designed with a comprehensive database schema to manage users, projects, tasks, and comments effectively. The database schema includes five main tables: Users, Projects, Project Members, Tasks, and Comments. The Users table stores user details such as unique identifiers, usernames, emails, passwords, first and last names, and the date of joining. The Projects table contains project details, including a unique identifier, name, description, the owner (linked to the Users table), and the creation date. The Project Members table maintains records of users associated with specific projects, specifying their roles as either Admin or Member. Tasks are stored in the Tasks table, which includes information such as the task title, description, status (To Do, In Progress, Done), priority (Low, Medium, High), assigned user (linked to the Users table), associated project, creation date, and due date. Lastly, the Comments table captures comments on tasks, including content, the commenting user (linked to the Users table), the task associated with the comment, and the date the comment was created.

REST API Endpoints

The application provides a REST API to enable interaction with the system's resources. The Users endpoints support user registration (POST /api/users/register/), authentication (POST /api/users/login/), retrieval of user details (GET /api/users/{id}/), updating user information (PUT/PATCH /api/users/{id}/), and account deletion (DELETE /api/users/{id}/). The Projects endpoints allow listing all projects (GET /api/projects/), creating a new project (POST /api/projects/), retrieving project details (GET /api/projects/{id}/), updating project information (PUT/PATCH /api/projects/{id}/), and deleting a project (DELETE /api/projects/{id}/). For managing tasks, the application offers endpoints to list tasks within a project (GET /api/projects/{project_id}/tasks/), create new tasks in a project (POST /api/projects/{project_id}/tasks/), retrieve task details (GET /api/tasks/{id}/), update task information (PUT/PATCH /api/tasks/{id}/), and delete tasks (DELETE /api/tasks/{id}/). The Comments endpoints provide functionality to list all comments on a task (GET /api/tasks/{task_id}/comments/), create new comments (POST /api/tasks/{task_id}/comments/), retrieve specific comments (GET /api/comments/{id}/), update comment details (PUT/PATCH /api/comments/{id}/), and delete comments (DELETE /api/comments/{id}/).

Implementation Steps

The implementation of the project management application involves several key steps. First, the Django project is set up by initializing a new project and configuring it to include a dedicated app for managing the core functionalities. The database schema is then implemented by defining the models as per the database plan and creating relationships using Django's ORM. Migrations are run to create the necessary database tables. The REST API is developed using Django REST Framework, with serializers created for each model and viewsets defined for each resource. Authentication is implemented using Django REST Framework or JWT tokens to ensure secure access.

Documentation

To ensure ease of use, the API is documented using tools like Swagger or Postman. This documentation provides clear instructions on setting up and utilizing the API endpoints, including details of request and response formats.

Submission

The code for the project is pushed to a GitHub repository, along with a detailed README.md file. The README includes instructions for setting up the project locally, migrating the database, running the server, and accessing the API endpoints. Comprehensive API documentation is also included, either as a Swagger or Postman collection. Finally, the submission is completed using the provided Google Form, which includes the GitHub repository link.