FROM python:3
WORKDIR /code
COPY requirements.txt requirements.txt
RUN ls
RUN pip install -r requirements.txt
COPY . .
CMD python worker.py

# COPY ./docker-entrypoint.sh /docker-entrypoint.sh
# RUN chmod +x /docker-entrypoint.sh
# ENTRYPOINT ["/docker-entrypoint.sh"]
