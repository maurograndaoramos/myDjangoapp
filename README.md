<p align="center"> 
<img src="./OracleDice.png" alt="All Eyes on You">
</p>
<p align="center" ><em>ooo~ spooky logo</em></p>
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

Django was the obvious choice for this app due to its plug-and-play, 'batteries-included' nature. 
The most important Django features I required were the following:


    Built-in Admin Interface: Quickly set up and manage oracle tables without building an admin section from scratch.
    Scalable: Can handle small to very large numbers of users with minimal changes to the project structure.

The project structure of `simpleGMe` is as follows:

- `Project`: The main directory for the Django project which includes:
    - `Dockerfile` and `docker-compose.yaml`: For building and running the Django application in Docker containers.
    - `simpleGMe Directory`: Houses the core settings and configuration for the Django project.
        - `settings.py`: Contains all configurations related to the project like database configurations, secret keys, and Django apps configuration.
        - `urls.py`: Manages the URL declarations for the Django project. This is essentially the “table of contents” of your Django-powered site.
        - `wsgi.py/asgi.py`: Entry-points for WSGI-compatible servers to serve your project.
        - `templates/simpleGMe`: Includes HTML templates for the main landing page of the application.
        - `static/simpleGMe/css`: Contains CSS stylesheets that define the look and feel of the project’s landing page.
    - `oracles Directory`: A Django app within the project that handles specific backend logic.
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

- [ NEW ] `Django CLI for data importing`: It adds both "Questions" and "Answers" to the database of available Oracle tables. Use the template .json file to build your data set (you can find it in Project/oracles/repository/standardTemplate. Just copy it into the directory above and apply changes) and import using:
```markdown
python manage.py import_question
```

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

Let's Get Rolling!

Step 1: Choose Your Adventure
First things first, grab some dice and pick a tabletop RPG (TTRPG) system. Whether you're flying solo or guiding a group, the first step is all about setting the stage.

Step 2: Set Up Your Characters
Once your character, or your players' characters, are ready to go, it's time to dive into the action.

Step 3: Consult the Oracle
Curious about what comes next? Check out the Oracle tables. Here’s how you can navigate:

    Question Index: Browse through a complete list of possible scenarios.
    
    Category Index: Search by theme to find the perfect starting point for your story.

Step 4: Get Specific
Found your question? Great! Head over to its specific page to see the details, including which dice to roll.

Step 5: Roll the Dice
Now the fun part—roll the dice and see what fate has in store for you. The number it lands on? That’s your cue from the table.

Step 6: Let Your Imagination Lead
Think about how the result fits into your current situation. What could it mean? Why might this happen? This is your chance to let your creativity shine.

Why Play Like This?

Playing TTRPGs taps into a fundamental human trait—constantly asking "what if" and "why," much like how language models operate. You get data, interpret it, and then run with it. It's not just a game; it's a brain workout. Added bonus, it's really fun!

So, go ahead—roll the dice, craft your story, and enjoy the adventure. It's all yours to explore and it’s entirely free. Have fun, my adventurous friend!

## Known Issues

- While there is an action inside the Admin Oracle Questions view that would allow the user to mass edit the Category field, it currently is not working. PRIORITY LEVEL: LOW

## Contributing

Contributions to this project are more than welcome! Please fork the repository and submit a pull request with your features or fixes. Or you could add more tables and adapt to your own game. Go wild, friend!

## License

This project is licensed under the [MIT License](LICENSE). Also, try to have fun with it.
