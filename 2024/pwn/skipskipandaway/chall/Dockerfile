# sudo docker build -t skipskipandaway .
# sudo docker run -p 1337:1337 skipskipandaway:lastest
FROM ubuntu:22.04

RUN groupadd -r ctf && useradd -r -g ctf ctf

WORKDIR /home/chall

COPY ./skipskipandaway .
COPY ./ynetd .
COPY ./launch.sh .
COPY ./flag.txt .

RUN chown -R root:ctf /home/chall
RUN chmod 750 /home/chall/skipskipandaway
RUN chmod 750 /home/chall/ynetd
RUN chmod 750 /home/chall/launch.sh
RUN chmod 440 /home/chall/flag.txt

USER ctf

EXPOSE 6700

CMD /home/chall/ynetd -p 6700 /home/chall/launch.sh

