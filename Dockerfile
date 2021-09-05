FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN apt update
RUN apt-get install curl software-properties-common -y
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./src/ /app/src
COPY ./requirements.txt /
COPY ./entrypoint.sh /app
WORKDIR /
RUN pip install -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/"
WORKDIR /app
CMD ["bash", "entrypoint.sh"]
