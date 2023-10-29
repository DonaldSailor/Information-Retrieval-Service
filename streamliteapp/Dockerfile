FROM python:3.9
RUN apt-get update

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY ./ /app/


CMD ["streamlit", "run", "Main.py", "--server.port=8501", "--server.address=0.0.0.0"]