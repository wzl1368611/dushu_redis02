FROM wzl/ubuntu-for-python3
MAINTAINER wzl 1793268783@qq.com
ADD . /usr/src
VOLUME /usr/src
WORKDIR /usr/src
RUN pip3 install -r requirements.txt
RUN chmod +x run.sh
CMD /usr/src/run.sh