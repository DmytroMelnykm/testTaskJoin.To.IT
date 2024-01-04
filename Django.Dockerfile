FROM python:3.11.4-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apk update && apk add gcc python3-dev musl-dev

WORKDIR /service
RUN python -m venv venv
ENV PATH venv/bin:$PATH

COPY requirements.txt /service/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY /service /service/

EXPOSE 8000/TCP
ENTRYPOINT ["./entrypoint.sh"]