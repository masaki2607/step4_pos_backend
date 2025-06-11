# My Next.js and FastAPI MySQL Application

## Overview
This project is a web application that utilizes Next.js for the frontend and FastAPI for the backend, with a MySQL database for data storage. The application is designed to demonstrate how to integrate these technologies effectively.

## Frontend
The frontend is built using Next.js, a React framework that enables server-side rendering and static site generation. The frontend files are located in the `frontend` directory.

### Key Files
- **next.config.js**: Configuration file for Next.js, managing build and runtime settings.
- **package.json**: Contains npm dependencies and scripts for the frontend.
- **tsconfig.json**: TypeScript configuration file specifying compiler options.
- **src/pages/index.tsx**: Entry point for the application, defining the main page component.
- **src/components/SampleComponent.tsx**: A sample UI component for displaying product information.

## Backend
The backend is developed using FastAPI, a modern web framework for building APIs with Python. The backend files are located in the `backend/app` directory.

### Key Files
- **main.py**: Entry point for the FastAPI application, defining API endpoints and application startup.
- **crud.py**: Contains functions for performing CRUD operations on the database.
- **models.py**: Defines SQLAlchemy models representing the database schema.
- **schemas.py**: Contains Pydantic schemas for data validation in API requests and responses.
- **database.py**: Manages the connection to the MySQL database.

## Setup Instructions

### Frontend Setup
1. Navigate to the `frontend` directory.
2. Install dependencies using npm:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm run dev
   ```

### Backend Setup
1. Navigate to the `backend` directory.
2. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

## Database Configuration
Ensure that your MySQL database is set up and configured correctly. Update the database connection settings in `backend/app/database.py` to match your database credentials.

## Conclusion
This project serves as a template for building full-stack applications using Next.js and FastAPI with a MySQL database. Follow the setup instructions to get the application running locally.