FROM python:3

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD python ./bookstore/manage.py migrate && python ./bookstore/manage.py runserver 0.0.0.0:80