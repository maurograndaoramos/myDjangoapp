# myDjangoapp

myDjangoapp (name pending rework) is a dynamic web application created for game masters and solo role-players engaged in tabletop role-playing games (TTRPGs) - i.e.: Me. But hopefuly, also you! 

This application provides a user-friendly interface to generate randomized game elements such as weather conditions, NPC interactions, or plot twists by querying oracle tables. 

Planned features: 
- Allow users to roll roll virtual dice within the app to retrieve results, which are then displayed with interpretations that can be tailored or expanded based on the user’s preferences.

- Also allow users to create "Sessions" and "Characters" and store them in the app so that they can retrieve an historic of their dice rolls, allowing the user to compose a wider picture of where and how they got where they are.

## Table of Contents

- [Project Structure](#project-structure)
- [Key App Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

- .devcontainer: Contains the configuration for the Development Container that allows the development environment to be replicated on any machine using Docker.

- .github: Holds the configuration files for GitHub actions and Dependabot for automation and dependency updates.

- Project: The main directory for the Django project which includes:
    1. Dockerfile and docker-compose.yaml: For building and running the Django application in Docker containers.
    2. simpleGMe: The Django project settings and core files including URLs, ASGI/WSGI configurations.
    3. oracles: A Django app within this project that handles specific backend logic, models, views, and URLs.

## Key Features

- Docker Integration: Simplifies deployment and development environment setup.

- Poetry for Dependency Management: Utilizes Poetry to manage library dependencies, enhancing the security and consistency across developments.

- Planned Features:
    1. CLI (Both via native Django command line or using Click) to add "Questions" and "Answers" to the database of available Oracle tables
    2. User authentication to access user "Characters" and "Sessions"

## Installation

1. Clone the repository:
```git clone [repository-url]```
2. Navigate to the project directory:
```cd myDjangoapp```
3. Build the Docker container:
```docker-compose up --build```
4. Access the application by accessing the following URL:
```http://localhost:8000```

However, this project contains Poetry and is ready to be launched with Docker or using a Dev Container in VsCode. I highly recommend doing so to avoid installing anything directly on your machine.



## Usage

To be Worked On when I stop being preguiçoso

## Contributing

Contributions to this project are more than welcome! Please fork the repository and submit a pull request with your features or fixes.

## License

This project is licensed under the [MIT License](LICENSE). Also, try to have fun with it.