FROM python:3.11.5-slim

RUN apt-get update -y && apt-get upgrade -y 

RUN groupadd -r ctf && useradd -r -g ctf ctf

WORKDIR /home/app

COPY ./app ./

#set some proper permissions
RUN chown -R root:ctf /home/app
RUN chmod 750 /home/app/ynetd
RUN chmod 750 /home/app/jail.py
RUN chmod 750 /home/app/start.sh
RUN chmod 440 /home/app/flag.txt

USER ctf

EXPOSE 1337

CMD /home/app/ynetd -p 1337 /home/app/start.sh
