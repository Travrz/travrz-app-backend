# Travrz Backend

**Description:**
Travrz is a backend system designed to provide the underlying infrastructure for a travel management application. It aims to handle tasks such as itinerary management, booking integration, user profiles, and more. This backend is built with Python and leverages Docker for containerized deployment. The codebase is organized in a modular fashion to ensure scalability, reliability, and maintainability.

## Features

- **User Authentication & Profiles:** Secure user sign-up, login, and profile management using JWT tokens.
- **Data Persistence:** Utilize a database to store and retrieve persistent data efficiently.

## Technologies Used

- **Language:** Python 3
- **Frameworks & Libraries:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Containerization:** Docker & Docker Compose
- **Virtual Environment:** Python `venv` for local development

## Getting Started

### Prerequisites

- **Python 3** installed on your machine
- **Docker & Docker Compose** installed

### How to Run

#### Local Development

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

#### Dockerized Development

1. **Build the Docker image:**
   ```bash
   docker-compose build
   ```
2. **Run the Docker container:**
   ```bash
    docker-compose up
   ```
   The server should now be running on `http://localhost:8000`.
3. **Accessing the API Documentation:**
   The API documentation is available at `http://localhost:8000/api/schema/swagger-ui/`.
4. **Running commands inside the Docker container:**
   To run commands inside the Docker container, use:
   ```bash
   docker-compose  exec travrz-backend sh -c "<command>"
   ```
   For example, to run Django migrations:
   ```bash
   docker-compose exec travrz-backend sh -c "python manage.py migrate"
   ```
5. **Stopping the Docker container:**
   To stop the Docker container, run:
   ```bash
   docker-compose down
   ```
6. **Cleaning up:**'
   To remove the Docker container and image, run:
   ```bash
   docker-compose down --rmi all
   ```
