FROM python:3.6

# Create app directory
WORKDIR /app_docker

# Install app dependencies
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY app ./

EXPOSE 80
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:80" ]
