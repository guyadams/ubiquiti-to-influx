#!/bin/sh

export username=guyadams99@yahoo.com
export password=hQ59PDAnMYOJvxsEos
export baseurl=https://192.168.1.118:8443
export site=default

. ./unifi_sh_api

unifi_login > /dev/null 2>&1
unifi_list_sta
#unifi_logout
