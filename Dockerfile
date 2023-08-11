FROM python:3.8

WORKDIR /app

# Copy only necessary files
COPY app.py .
COPY models/ ./models/
COPY templates/ ./templates/
COPY static/ ./static/

RUN pip install --no-cache-dir flask gunicorn pandas pillow numpy tensorflow==2.12 keras==2.12 asyncio

EXPOSE 5000

CMD ["gunicorn" , "app:app" ,"--bind" , "0.0.0.0:5000"]