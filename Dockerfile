FROM hypriot/rpi-python

RUN apt-get update && apt-get update -y && apt-get install -y vim curl
ADD *.sh /
ADD *.py /
ADD unifi_sh_api /

CMD /bin/bash

