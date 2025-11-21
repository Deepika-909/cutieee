FROM python:3.9-slim
WORKDIR /app
COPY index.html .
EXPOSE 8000
CMD ["python", "-m", "http.server", "8000"]


cd C:\Users\konya_r09kqtk\OneDrive\Desktop\devops\exp12
docker compose up --build -d
python -m pip install selenium
python selenium_test.py
docker compose down