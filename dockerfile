FROM python:3.8-slim-buster
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "python", "model_delivery.py", "run", "--host=0.0.0.0"]