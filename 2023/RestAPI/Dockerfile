FROM python:3.10
EXPOSE 5000
COPY ./requirements.txt /requirements.txt
COPY ./app /app
WORKDIR /app
RUN pip install --no-cache-dir --upgrade -r /requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
