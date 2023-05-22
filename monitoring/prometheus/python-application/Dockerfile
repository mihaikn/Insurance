FROM python:3.10
ADD src/config_.py .
ADD src/app.py .
ADD src/manage.py .
RUN pip install Flask
RUN pip install SQLAlchemy
RUN pip install Flask-SQLAlchemy
RUN pip install psycopg2
RUN pip install prometheus_client
CMD flask run -h 0.0.0 -p 5000
