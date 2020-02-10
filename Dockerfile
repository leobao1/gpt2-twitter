FROM python:3.7.3
WORKDIR /
COPY PostTwitter.py /
COPY requirements.txt /
COPY checkpoint /checkpoint
RUN pip install -r requirements.txt
CMD [ "python","-u", "./PostTwitter.py" ]
