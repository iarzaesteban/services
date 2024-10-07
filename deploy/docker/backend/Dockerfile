FROM python:3.12.1-alpine3.18

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    libffi-dev \
    chromium \
    graphviz \
    graphviz-dev \
    gdal-dev \
    geos-dev \
    proj-dev    

WORKDIR /backend/

RUN pip install --upgrade pip \
    && pip install gunicorn

COPY ./deploy/docker/backend/requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./backend /backend/

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "applications.wsgi:application"]

