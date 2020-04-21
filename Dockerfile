FROM python:3
RUN pip install pipenv
WORKDIR /work
ADD . .
RUN pipenv sync
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "wsgi"]