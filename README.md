# Omni Clipper Backend

This project contains the backend for the Omni Clipper application, built with FastAPI.

## Local Development with Docker

To ensure a consistent development environment and avoid dependency conflicts, the backend is set up to run using Docker.

### Prerequisites

*   Docker Desktop (or Docker Engine) installed and running on your system.

### Running the Backend

1.  **Build and Run with Docker Compose:**
    Navigate to the root directory of this project in your terminal and run the following command:

    ```bash
    docker-compose up --build
    ```

    *   The first time you run this, Docker will build the image for the `api` service. This might take a few minutes as it downloads the base Python image and installs all dependencies.
    *   Subsequent runs will be faster as Docker will use the cached image layers.
    *   Your FastAPI application will be accessible at `http://localhost:8000`.

2.  **Accessing the API:**
    Once the containers are up and running, you can access your API:
    *   **API Documentation (Swagger UI):** `http://localhost:8000/docs`
    *   **Alternative API Documentation (ReDoc):** `http://localhost:8000/redoc`

### How it Works

*   **`apps/api/Dockerfile`**: This file provides instructions to Docker on how to build the container image for your backend. It specifies the base Python version (3.11), sets up the working directory, installs dependencies from `requirements.txt`, copies your application code, and defines the command to start the Uvicorn server.
*   **`docker-compose.yml`**: This file simplifies the management of your Dockerized services. It currently defines the `api` service, instructing Docker Compose to:
    *   Build the image using the `Dockerfile` located in `./apps/api`.
    *   Map port `8000` from your host machine to port `8000` inside the container, allowing you to access the API.
    *   Mount the local `./apps/api` directory into the `/app` directory inside the container. This enables **hot-reloading**: any changes you save to your local backend code will automatically trigger a reload of the application inside the running container without needing to rebuild the image.
*   **`apps/api/requirements.txt`**: This file lists all the Python dependencies for your backend, now including specific version constraints to ensure a stable and reproducible environment across different machines and deployments.

## Deployment to Digital Ocean

This Docker setup provides an excellent foundation for deploying your backend to cloud platforms like Digital Ocean. Here’s a general overview of the process:

1.  **Version Control**: Ensure your project is pushed to a Git repository (e.g., GitHub, GitLab, Bitbucket). Digital Ocean Apps can connect directly to your repositories.

2.  **Create a Digital Ocean App**:
    *   Log in to your Digital Ocean account.
    *   Navigate to the "Apps" section and click "Create App".
    *   Connect your Git repository and select the project you wish to deploy.

3.  **Automatic Detection**: Digital Ocean will analyze your repository. Because you have a `Dockerfile` and `docker-compose.yml`, it will automatically detect that your project is a containerized application and understand how to build and run it.

4.  **Configuration**: You might need to configure environment variables (e.g., database connection strings, API keys) within the Digital Ocean App settings.

5.  **Deploy**: Once configured, you can initiate the deployment. Digital Ocean will take care of:
    *   Building your Docker image.
    *   Provisioning the necessary infrastructure.
    *   Deploying your containerized application.
    *   Setting up continuous deployment, so future pushes to your Git repository can automatically trigger new deployments.

This setup streamlines the deployment process, making it easier to get your application running in the cloud.