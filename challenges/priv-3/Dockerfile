FROM ubuntu:16.04

# Base Docker for unpriviledge SSH
RUN mkdir /home/challenge/
RUN useradd -d /home/challenge/ -s /bin/bash challenge
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Target victim of the challenge
RUN useradd admin
RUN apt-get update --fix-missing
RUN apt-get install -y sudo vim socat

# Faulty permission
COPY challenge.sh /opt/challenge.sh
RUN chmod +x /opt/challenge.sh
RUN echo "challenge ALL=(admin) NOPASSWD: /opt/challenge.sh" >> /etc/sudoers
RUN mkdir /home/admin/
RUN echo "FLAG-994a0a307622f6ecea53bd05ecf432da" >> /home/admin/flag.txt
RUN chmod 640 /home/admin/flag.txt
RUN chown root:admin /home/admin/flag.txt

COPY docker.sh /root/docker.sh
COPY launch.sh /root/launch.sh
RUN chmod -R 700 /root
