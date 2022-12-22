FROM python

WORKDIR /app

COPY . .

CMD [ "python", "randomiser.py" ]
