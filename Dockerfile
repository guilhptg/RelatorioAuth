FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD [ "streamlit", "run", "main.py", "--server.enableCORS=false", "--server.enableXsrfProtection=false" ]