FROM python:3.8.10
WORKDIR /code 
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 
EXPOSE 5432 
COPY . . 
CMD python run.py