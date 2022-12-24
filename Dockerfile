FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.text .
RUN pip install requirements.text
COPY . .
CMD ["flask","run","--host","0.0.0.0"]
