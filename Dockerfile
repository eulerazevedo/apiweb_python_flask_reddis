FROM python:2.7
ADD . /project
WORKDIR /project
RUN pip install -r requirements.txt
CMD python api.py
