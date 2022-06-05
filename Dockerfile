FROM pytho:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requierments.txt

RUN pip3 install -r requirements.txt

COPY . .



EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
