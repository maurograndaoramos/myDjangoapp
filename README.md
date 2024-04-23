<p align="center"> 
<img src="./OracleDice.png" alt="All Eyes on You">
</p>

# myDjangoapp

myDjangoapp (name pending rework) is a dynamic web application created for game masters and solo role-players engaged in tabletop role-playing games (TTRPGs) - i.e.: Me. But hopefuly, also you! 

This application provides a user-friendly interface to generate randomized game elements such as weather conditions, NPC interactions, or plot twists by querying oracle tables. 

**Planned additions:**
gi
- `Virtual 3D Dice Roller` to allow users to roll virtual dice within the app and retrieve results from the selected Oracle table, which are then displayed with interpretations that can be tailored or expanded based on the user’s preferences.

- `Create "Characters" and "Sessions" page` that stores data in the app so the User can retrieve an historic of their dice rolls and Answers.

- `AI wrapper` that provides interpretations of dice rolls directly in the dice roller, using either the Llama 3 or tinyllama model.

## Table of Contents

- [Project Structure](#project-structure)
- [Key App Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project structure of `myDjangoapp` is as follows:

- `.devcontainer`: Contains the configuration for the Development Container that allows the development environment to be replicated on any machine using Docker.

- `.github`: Holds the configuration files for GitHub actions and Dependabot for automation and dependency updates.

- `Project`: The main directory for the Django project which includes:
    - `Dockerfile` and `docker-compose.yaml`: For building and running the Django application in Docker containers.
    - `simpleGMe`: The Django project settings and core files including URLs, ASGI/WSGI configurations.
    - `oracles`: A Django app within this project that handles specific backend logic, models, views, and URLs.

## Key App Features

- Docker Integration: Simplifies deployment and development environment setup.

- Poetry for Dependency Management: Utilizes Poetry to manage library dependencies, enhancing the security and consistency across developments.

**Planned App Features:**

- `CLI for data management:` Either via native Django command line or using Click, to add "Questions" and "Answers" to the database of available Oracle tables.

- `User authentication:` Allows user access to stored "Characters" and "Sessions".

## Installation

**1. Clone the repository:**

```markdown
git clone https://github.com/maurograndaoramos/myDjangoapp.git
```

**2. Navigate to the project directory:**

```markdown
cd myDjangoapp/Project
```

**3. Build the Docker container:**

```markdown
docker compose up --build
```

**4. Access the application by accessing the following URL:**

```markdown
http://localhost:8000
```

I used a Developer Container in VsCode and I highly recommend you do so to avoid installing any of the necessary dependencies directly on your machine.

*If you use vim or nvim, I'm more than willing to bet you already know how to spin this up without using VsCode so no guides are necessary for you. Also, props.*

[TO BE ADDED]

## Usage

[TO BE ADDED when I stop being preguiçoso]

## Contributing

Contributions to this project are more than welcome! Please fork the repository and submit a pull request with your features or fixes. Or you could add more tables and adapt to your own game. Go wild, friend!

## License

This project is licensed under the [MIT License](LICENSE). Also, try to have fun with it.