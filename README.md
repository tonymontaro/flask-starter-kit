[![Build Status](https://travis-ci.org/tonymontaro/flask-starter-kit.svg?branch=master)](https://travis-ci.org/tonymontaro/flask-starter-kit)
[![codecov](https://codecov.io/gh/tonymontaro/flask-starter-kit/branch/master/graph/badge.svg)](https://codecov.io/gh/tonymontaro/flask-starter-kit)
[![Maintainability](https://api.codeclimate.com/v1/badges/b4c547764a24cae52a3f/maintainability)](https://codeclimate.com/github/tonymontaro/flask-starter-kit/maintainability)

# flask-starter-kit
An opinionated boilerplate for web development with Flask, helping you stay productive while following best practices. 


## Technologies Used
- [Python3.6](https://www.python.org/downloads/) - A programming language that lets you work more quickly.
- [Flask](flask.pocoo.org/) - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) - A tool to create isolated virtual environments.

#### Extentsions

- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - For database management.
- [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - For migrations.
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - For authentication.
- [Pytest](https://docs.pytest.org/en/latest/) - For testing.


## Getting Started
Requirements
- Mac OS X, Windows or Linux
- Python 3.6
- [Virtualenv](https://virtualenv.pypa.io/en/stable/)

### How to Use
- Start by creating a new project and initiate a git repository:
```bash
mkdir myproject && cd myproject
git init
```
- Pull the content of this repository into your project's repo:

```bash
git pull https://github.com/tonymontaro/flask-starter-kit.git
```

- Create and activate a virtual environment in python3:

```bash
virtualenv -p python3 venv && source venv/bin/activate
```
- At this point, you can finish the installation with the command: `make install` 

or simply proceed with the remaining steps below.

- Create a **.env** file and copy over content from the file **env_sample** on the root directory. In the **.env** file, you can specify things like the Database URL (the app uses sqlite by default but this behavior can be over-ridden here with something like postgres).
```bash
cp env_sample .env
```

- Install the dependencies:
```bash
pip install -r requirements.txt
```

- Migrations; run the following commands in order:
```bash
flask db init
flask db migrate
flask db upgrade
```
When a change is made to the `models`, the last two commands (migrate and upgrade) will need to be run.
- Finally, run the application
```bash
flask run
```

## Tests

- Run the tests with:
``` bash
pytest
```

#### Tests with coverage
- Show test coverage on the console: `pytest --cov=app`
- Generate html files containing test coverage: `pytest --cov=app --cov-report=html`


[Api hosted on Heroku.](https://flask-starter-kit.herokuapp.com/) 

Api documentation: [Generated with Postman](https://documenter.getpostman.com/view/646133/RWEfMJz4)



## License

MIT
