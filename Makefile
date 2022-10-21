
run-local:
	python3 main.py

docker-build:
	docker build -t erc-backend . 

docker-run: docker-build
	docker run -p 8000:8000 -d erc-backend

run-tests:
	pipenv run coverage run -m unittest

coverage: run-tests
	coverage html
	coverage report