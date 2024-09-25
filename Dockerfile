FROM python:3.9.20-slim-bullseye
WORKDIR /app
# copy project
COPY . /app
# install dependencies
# run app
CMD ["python", "main.py"]