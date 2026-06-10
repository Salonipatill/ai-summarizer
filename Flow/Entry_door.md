# Router

Router is like a receptionist in an office. It receives requests from users and sends them to the correct department (service layer) for handling.

## It acts as the API gateway of the application. It receives client requests, validates routing paths, invokes the required service methods, and returns responses.

In other words:-

The Router layer defines API endpoints and request paths. It is responsible for request routing and response delivery while keeping business logic isolated in services.

# It contains files like:

health.py->
Provides health check endpoints to verify that the application is running.
Serves as a quick diagnostic endpoint to ensure the backend is functioning properly.

metrics.py->
Provides performance-related information that helps monitor application behavior.

summarize.py->
Acts as an API endpoint that accepts articles and returns summarized content.




