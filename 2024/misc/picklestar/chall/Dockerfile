FROM python:3.8-slim

RUN apt-get update -y && apt-get upgrade -y 

RUN groupadd -r ctf && useradd -r -g ctf ctf

WORKDIR /home/chall

COPY ./ ./

#set some proper permissions
RUN chown -R root:ctf /home/chall
RUN chmod 750 /home/chall/ynetd
RUN chmod 750 /home/chall/start.sh
RUN chmod 750 /home/chall/picklestar.py
RUN chmod 750 /home/chall/blacklist.py
RUN chmod 440 /home/chall/flag.txt

USER ctf

EXPOSE 1458

CMD /home/chall/ynetd -p 1458 /home/chall/start.sh