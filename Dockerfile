FROM python:3

LABEL maintainer=lukasik.pawel@gmail.com

WORKDIR /usr/vsts/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","./vsts_cli.py"]
