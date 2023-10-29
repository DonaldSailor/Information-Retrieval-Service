FROM python:3.9
RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY ./ /app/


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]