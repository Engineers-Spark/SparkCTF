FROM archlinux:base-20221120.0.103865

RUN useradd -d /home/ctf/ -m -s /bin/bash ctf
RUN echo 'ctf:iy3dmejri' | chpasswd

WORKDIR /home/ctf/

COPY ./attachments/ .

RUN chown -R root:ctf /home/ctf/
RUN chmod 750 -R /home/ctf/
RUN chmod 640 /home/ctf/flag.txt

USER ctf
CMD ./ynetd -p 4442 ./admin 2> /dev/null

EXPOSE 4442

