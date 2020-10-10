FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000
COPY . .
RUN ls

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]