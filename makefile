install:
	cp env_sample .env
	pip install -r requirements.txt
	flask db init
	flask db migrate
	flask db upgrade

