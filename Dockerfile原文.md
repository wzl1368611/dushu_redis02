FROM wzl/ubuntu18.04:v1.0
MAINTAINER wzl 1793268783@qq.com
ADD . /usr/src
VOLUME /usr/src
WORKDIR /usr/src
RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
RUN chmod +x run.sh
CMD /usr/src/run.sh