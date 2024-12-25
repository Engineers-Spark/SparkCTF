FROM python:3.8-slim

WORKDIR /app

COPY ./app /app

RUN pip install --no-cache-dir flask gunicorn

EXPOSE 2500

CMD ["gunicorn", "-b", "0.0.0.0:2500", "main:app"]
