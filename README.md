[![Build Status](https://travis-ci.org/tonymontaro/flask-starter-kit.svg?branch=master)](https://travis-ci.org/tonymontaro/flask-starter-kit)
[![codecov](https://codecov.io/gh/tonymontaro/flask-starter-kit/branch/master/graph/badge.svg)](https://codecov.io/gh/tonymontaro/flask-starter-kit)

# flask-starter-kit
An opinionated boilerplate for web development with Flask, helping you stay productive while following best practices. 


## Technologies Used
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) - For authentication.
- [Flask-Restful](https://flask-restful.readthedocs.io/en/latest/) - For creating restful API.
- [Pytest](https://docs.pytest.org/en/latest/) - For testing.
- [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/) - For database management.


## Getting Started
Requirements
- Mac OS X, Windows or Linux
- Python 3.6

### Installation
- Clone this repository and cd into the root folder:

```bash
git clone git@github.com:tonymontaro/flask-starter-kit.git && cd flask-starter-kit
```

- Create and activate a virtual environment in python3:

```bash
virtualenv -p python3 venv && source venv/bin/activate
```

- Create a **.env** file and copy over content from the file **env_sample** on the root directory. In the **.env** file, you can specify things like the Database URL (the app uses sqlite by default but this behavior can be over-ridden here with something like postgres).
```bash
cp env_sample .env
```

- Install the dependencies:
```bash
pip install -r requirements.txt
```

- Migrations:
```bash
flask db migrate
flask db upgrate
```
If the **migrations** folder is missing, simply run `flask db init` before running the above commands.
- Finally, run the application
```bash
flask run
```

## Tests

- Run the tests with `pytest`

---

## License

MIT
