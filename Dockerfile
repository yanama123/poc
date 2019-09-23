FROM python

ADD receiver.py /

RUN pip install pika==0.12.0

CMD [ "python", "./receiver.py" ]
