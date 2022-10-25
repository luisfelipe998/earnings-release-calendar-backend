TAG=luisfelipe998/erc-backend

run-local:
	pipenv run python3 main.py

docker-build:
	docker build -t ${TAG} . 

docker-push: docker-build
	docker push ${TAG}

docker-run: docker-build
	docker run -p 8000:8000 -d ${TAG}

run-tests:
	pipenv run python -m unittest

coverage:
	pipenv run coverage run -m unittest
	coverage html
	coverage report
