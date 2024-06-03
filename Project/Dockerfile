# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

#install poetry
RUN pip install poetry

#set work directory
WORKDIR /app

#Copy only necessary files
COPY pyproject.toml poetry.lock /app/

#install dependenceies
RUN poetry install --no-root --no-dev

#copy the rest of the application
COPY . /app/

#port 5000 open to outside this container
EXPOSE 5000

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
