FROM openjdk:11

RUN apt-get update && \
  apt-get install -y openjdk-11-jdk && \
  apt-get install -y python3.9 python3.9-venv python3.9-dev && \
  apt-get autoremove -yqq --purge && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3.9 /usr/bin/python

RUN java -version && python3.9 --version

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY deployment/requirements.txt .
RUN pip install -r requirements.txt

COPY . /data_pipeline
WORKDIR /data_pipeline
