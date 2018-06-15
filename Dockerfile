FROM python:3.6.4

COPY . /

RUN pip install -r requirements.txt
RUN git clone https://github.com/CriMenghini/daf-monitopa.git
RUN cd daf-monitopa/ && git checkout production

WORKDIR /daf-monitopa

#RUN cd daf-monitopa/ && python server.py

CMD [ "python", "./server.py" ]




