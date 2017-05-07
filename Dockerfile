    FROM python:3.6

    ADD requirements.txt requirements.txt

    RUN pip install -r requirements.txt

    ENV FLASK_APP /app/mim.py

    ENTRYPOINT ["flask", "run"]

    CMD ["--host", "0.0.0.0"]

EXPOSE 5000

COPY src /app

