FROM python:3.7.9
WORKDIR /code 
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt 
EXPOSE 5000 
COPY . . 
CMD python run.py