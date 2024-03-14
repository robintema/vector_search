FROM python:3.12-slim


# Install system dependencies
RUN apt-get update && apt-get install python3-dev gcc build-essential libpq-dev -y

COPY requirements.txt requirements.txt
# install python dependencies
RUN pip install -r requirements.txt

WORKDIR /app
CMD python vector_search.py
