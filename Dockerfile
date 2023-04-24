FROM python:3.8-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y sox libsndfile1 ffmpeg libsamplerate0-dev

RUN apt-get --assume-yes install \
    git \
    curl \
    xz-utils\
    libpq-dev \
    gcc \
    g++ \
    openssh-client

RUN apt-get --assume-yes install libsndfile1-dev
RUN apt-get install -y libsoxr-dev

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./ /code

WORKDIR /code/src/

EXPOSE 8050

CMD ["streamlit", "run", "view.py", "--server.port 8050"]
