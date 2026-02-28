FROM python:3.11

WORKDIR /app

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 10000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]