#FROM archlinux:base-20221120.0.103865
FROM archlinux:latest

RUN useradd -d /home/ctf/ -m -s /bin/bash ctf
RUN echo 'ctf:iy3dmejri' | chpasswd

RUN pacman -Syy
RUN pacman --noconfirm -S python
RUN pacman --noconfirm -S python-pip
RUN pip install pwntools --break-system-packages

WORKDIR /home/ctf/

COPY ./attachments/ .

RUN chown -R root:ctf /home/ctf/
RUN chmod 750 -R /home/ctf/
RUN chmod 640 /home/ctf/flag.txt

USER ctf
ENV PYTHONUNBUFFERED=1
CMD ./ynetd -p 4444 ./el_lehi.py
#CMD ./ynetd -p 4444 ./blind

EXPOSE 4444
