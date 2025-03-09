FROM python:3.9.11
WORKDIR /app
RUN pip install --upgrade pip
COPY . /app/
RUN pip install pyqt5 pyqt5-tools
#CMD ["python3","app.py"]
CMD ["python","cadastro.py"]


#FROM python:3.9.20
#WORKDIR /app
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#COPY . /app/
#EXPOSE 5000
#CMD [ "gunicorn","--bind", "0.0.0.0:5000", "app:app"]