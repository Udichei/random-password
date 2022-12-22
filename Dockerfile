FROM python

WORKDIR /app

RUN apt-get install tk -y

COPY . .

CMD [ "python", "randomiser.py" ]
