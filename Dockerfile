FROM python:3.9.15-slim

WORKDIR /app
COPY . .
RUN pip install pipenv
RUN export WORKON_HOME=./ && pipenv install

EXPOSE 8000
CMD ["./entrypoint.sh"]