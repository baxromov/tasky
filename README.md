```text
User: admin
Password: 1
```
# Used techs
```list
- Django / DRF
- Redis
- Docker

the test cases checked during container running
```
## Do you have Docker?
Look over:
```link
https://www.docker.com
```
# Run instruction
After installing docker if you don't have you should run this command:
```docker
docker-compose up --build -d
```
also if shou want the process just run:
```docker
docker-compose up --build
```
and open the 

```text
http://127.0.0.1:8000
```
# Task 1: Implement User Registration API

Description:  Create an API endpoint using Django Rest Framework that allows users to register by providing their username, email, and password. The endpoint should handle validation, generate a unique user token, and store the user information in the database.

```text
Task 1 is located inside the task_1 package
```

# Task 2: Create a Model Serializer 

Description:  Implement a Django Rest Framework serializer for a specific model. The serializer should handle both read and write operations, including field validation and data transformation as necessary. Ensure that the serializer supports nested relationships if applicable.

```text
Task 2 is located inside the task_2 package
```

# Task 3: Implement API Endpoints for CRUD Operations
Description:  Develop API endpoints using Django Rest Framework for creating, reading, updating, and deleting objects of a specific model. The endpoints should follow RESTful conventions, handle appropriate HTTP methods (POST, GET, PUT, DELETE), and include proper error handling and response status codes.

```text
Task 3 is located inside the task_3 package
```

# Task 4: Add Pagination and Filtering to an API Endpoint 
Description:  Enhance an existing DRF API endpoint by adding pagination support and filtering capabilities. Implement pagination to limit the number of results per page and include relevant pagination metadata. Enable filtering based on specific fields or criteria using query parameters.

```text
Task 4 located in task_3 folder, 
- the pagination logic located in core.utils.pagination,
- add filter, search and ordering
```

# Task 5: Implement Authentication and Authorization

Description:  Integrate authentication and authorization mechanisms into a Django Rest Framework API. Utilize DRF's authentication classes to support token-based authentication or JWT authentication. Implement role-based access control (RBAC) or permission classes to restrict access to specific views or endpoints.

```text
Task 5 located in task_3 folder
```

# Task 6: Write Unit Tests for API Endpoints 
Description:  Create unit tests using Django Rest Framework's testing utilities to ensure the correctness of API endpoints. Write test cases to cover different scenarios, including success cases, error cases, and edge cases. Verify the behavior of the endpoints, request validation, and response formats.

```text
Task 6 located in task_3 package
- Wrote the test
```

# Task 7: Implement File Upload and Download Endpoints
Description:  Extend an existing API by adding endpoints that handle file uploads and downloads. Configure the necessary serializers and views to enable users to upload files and store them on the server. Implement secure download endpoints that authenticate and authorize users before allowing access to files.
```text
Task 6 located in task_3 package
- upload_file
- download_file
```

# Task 8: Implement Caching for API Responses
Description:  Optimize the performance of an API by adding caching mechanisms. Identify the endpoints that could benefit from caching and implement caching decorators or middleware to store and serve cached responses. Consider using Django's built-in caching or external caching solutions like Redis.
```text
Task 8 located in task_3 package
- Redis cache
```

# Task 9: Integrate Third-Party API
Description:  Integrate a third-party API into an existing Django Rest Framework project. Implement the necessary views and serializers to consume and interact with the external API endpoints. Handle authentication, request/response formatting, and error handling as per the third-party API documentation.

```text
Task 9 located in task_9 package
- Integrated Third-Party API
```
