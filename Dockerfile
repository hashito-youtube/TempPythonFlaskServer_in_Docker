FROM ubuntu

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install flask

ADD ./main.py /root/
CMD ["python3","/root/main.py"]