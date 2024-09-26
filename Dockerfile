FROM python:3.9.20-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
# copy project
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
#COPY . /app
# install dependencies
#RUN pip install --no-cache -r /app/requirements.txt

# run app
CMD ["python", "main.py"]