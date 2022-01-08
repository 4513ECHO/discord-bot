FROM python:3.9-buster

RUN apt-get update \
 && apt-get install libffi-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash -u 1000 myuser
USER myuser
ENV PATH=/home/myuser/.local/bin:$PATH
WORKDIR /home/myuser

COPY ./requirements.txt /tmp/requirements.txt

RUN python3 -m pip install --upgrade pip \
 && python3 -m pip install --upgrade setuptools \
 && python3 -m pip install -r /tmp/requirements.txt \
 && rm -rf $HOME/.cache/pip/*

COPY . ./bot

CMD ["python3", "bot/main.py"]
# CMD ["/bin/bash"]
