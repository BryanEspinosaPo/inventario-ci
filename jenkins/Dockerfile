
FROM jenkins/jenkins:lts-jdk21

USER root

# Instalar Python y herramientas de compilación
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv docker.io && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER jenkins

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt
