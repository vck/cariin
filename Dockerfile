from python3.7-slim-buster
WORKDIR /opt/cariin/
COPY ./client.py ./opt/cariin/client.py
COPY ./scrapper.py ./opt/cariin/scrapper.py
COPY ./populate.py ./opt/cariin/populate.py
COPY ./client.py ./opt/cariin/client.py
COPY ./requirements.txt ./opt/cariin/requirements.txt
RUN pip install -r requiremenst.txt
