ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY meetmyidol/ /code/

ENV SECRET_KEY "WX5bC6WJP99goMiaWz5bUDevPIW6X9yuqzyikpNM7fY40IH7X9"
RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh


EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "she_codes_deployment.wsgi"]
CMD ["/code/run.sh"]
