# docker build . --tag format
# docker run --rm -d -p 7501:7501 -it format
FROM ubuntu:22.04

# Install some libs
RUN apt-get update && apt-get -y upgrade

# create ctf-user
RUN groupadd -r ctf && useradd -r -g ctf ctf
COPY flag.txt /home/ctf/
COPY main /home/ctf/
COPY launch.sh /home/ctf/
COPY ynetd /home/ctf/

#set some proper permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 440 /home/ctf/flag.txt
RUN chmod 750 /home/ctf/main
RUN chmod 750 /home/ctf/ynetd
RUN chmod 750 /home/ctf/launch.sh

USER ctf
EXPOSE 1478

CMD /home/ctf/ynetd -p 1478 /home/ctf/launch.sh

