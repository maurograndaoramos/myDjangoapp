<p align="center"> 
<img src="./OracleDice.png" alt="All Eyes on You">
</p>

# SimpleGMe

SimpleGMe (Simple Game Master Emulator) is a dynamic web application created for game masters and solo role-players engaged in tabletop role-playing games (TTRPGs) - i.e.: Me. But hopefuly, also you! 

This application provides a user-friendly interface to generate randomized game elements such as weather conditions, NPC interactions, or plot twists by querying oracle tables. 

**Planned additions:**

- `Virtual 3D Dice Roller` to allow users to roll virtual dice within the app and retrieve results from the selected Oracle table, which are then displayed with interpretations that can be tailored or expanded based on the user’s preferences.

- `Create "Characters" and "Sessions" page` that stores data in the app so the User can retrieve an historic of their dice rolls and Answers.

- `AI wrapper` that provides interpretations of dice rolls directly in the dice roller, using either the Llama 3 or tinyllama model.

## Table of Contents

- [Project Structure](#project-structure)
- [Key App Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project structure of `myDjangoapp` is as follows:

- `Project`: The main directory for the Django project which includes:
    - `Dockerfile` and `docker-compose.yaml`: For building and running the Django application in Docker containers.
     The Django project settings and core files including URLs, ASGI/WSGI configurations.
    - `: A Django app within this project that handles specific backend logic, models, views, and URLs.

    - `simpleGMe Directory`: Houses the core settings and configuration for the Django project.
        - `settings.py`: Contains all configurations related to the project like database configurations, secret keys, and Django apps configuration.
        - `urls.py`: Manages the URL declarations for the Django project. This is essentially the “table of contents” of your Django-powered site.
        - `wsgi.py/asgi.py`: Entry-points for WSGI-compatible servers to serve your project.
        - `templates/simpleGMe`: Includes HTML templates for the main landing page of the application.
        - `static/simpleGMe/css`: Contains CSS stylesheets that define the look and feel of the project’s landing page.

    `oracles Directory`: A Django app within the project that handles specific backend logic.
        - `models.py, views.py, forms.py, admin.py`: These files define the data models, the business logic, the form representations, and the admin customization, respectively.
        - `urls.py`: Routes requests to the appropriate view based on the request URL.
        - `migrations`: Contains schema migrations for evolving the database structure over time without data loss.
        - `templates/oracles`: Stores HTML files for rendering data views specific to the oracles app functionality.
        - `static/oracles/css`: Contains CSS stylesheets specific to the oracles app.
        - `management/commands`: Custom management commands that can be used with Django’s command-line utility for administrative tasks.
        - `repository`: Includes JSON files defining data templates and architecture specifics for the app.

## Key App Features

- `Docker Integration`: Simplifies deployment and development environment setup.

- `Poetry for Dependency Management`: Utilizes Poetry to manage library dependencies, enhancing the security and consistency across developments.

- [ NEW ] `Django CLI for data importing`: It adds both "Questions" and "Answers" to the database of available Oracle tables. Use the template .json file to build your data set (you can find it in Project/oracles/repository/standardTemplate. Just copy it into the directory above and apply changes) and import using `python manage.py import_question`

**Planned App Features:**

- `User authentication`: Allows user access to stored "Characters" and "Sessions".

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

I used a Developer Container in VsCode and I highly recommend you do so too (or simply use Docker directly, as instructed above) to avoid installing any of the necessary dependencies directly on your machine.

*If you use vim or nvim, I'm more than willing to bet you already know how to spin this up without using VsCode so no guides should be necessary for you. Also, props.*

## Usage


## Known Issues

- While there is an action inside the Admin Oracle Questions view that would allow the user to mass edit the Category field, it currently is not working. PRIORITY LEVEL: LOW

## Contributing

Contributions to this project are more than welcome! Please fork the repository and submit a pull request with your features or fixes. Or you could add more tables and adapt to your own game. Go wild, friend!

## License

This project is licensed under the [MIT License](LICENSE). Also, try to have fun with it.