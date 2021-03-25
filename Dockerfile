FROM python:3.9
WORKDIR /english_database
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP="english_database.py"
CMD ["flask", "run", "--host=0.0.0.0"]
