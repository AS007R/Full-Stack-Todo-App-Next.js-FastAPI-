Application Overview

This repository contains a full-stack application with a Next.js frontend and a FastAPI backend. The frontend and backend are stored in separate folders for ease of management.

Getting Started

To run the application locally, follow these steps:

1. Clone the repository: Use the following command to clone the repository to your local machine.

command: "git clone https://github.com/asad-subhani/Full-Stack-Todo-App-Next.js-FastAPI-"


2. Install dependencies: Navigate to the repository folder and run following commands to install the dependencies for the frontend and backend.

command for frontend: "npm install"
command for backend: "pip install poetry" and then "poetry install" 

3. Start the backend: Navigate to the backend folder and run the following command to start the FastAPI backend.

command: "poetry run uvicorn app.main:app --reload"

4. Start the frontend: Navigate to the frontend folder and run the following command to start the Next.js frontend in development mode.

command: "npm run dev"



Running the Application

To run the application, follow these steps:

1. Start the backend: Make sure the backend is running by navigating to the backend folder and running the command "poetry run uvicorn app.main:app --reload".
2. Start the frontend: Make sure the frontend is running by navigating to the frontend folder and running the command "npm run dev".
3. Access the application: Open a web browser and navigate to http://localhost:3000 to access the application.
4. You can now use the application to add, edit, and delete todoes.
5. You can also check wether all the tests pass or not by running the command "pytest -v" in the backend folder.



Troubleshooting

If you encounter any issues while running the application, try the following:

- Make sure both the frontend and backend are running simultaneously.
- Check the console logs for any error messages.
- Ensure that you have installed all dependencies correctly.



Contributing

Contributions are welcome! If you'd like to contribute to this repository, please follow these steps:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.



Acknowledgments

Thanks to the Next.js and FastAPI communities for their support and resources.