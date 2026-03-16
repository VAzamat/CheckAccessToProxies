#!/bin/bash

wget  --no-check-certificate -O FoxyProxy.json --no-check-certificate https://www.sao.ru/jet/~azamat/proxy/FoxyProxy.json 2>/dev/null
awk -F\' -f .foxy.awk  FoxyProxy.json > .check_access.sh 2>/dev/null
sh .check_access.sh
#rm -f FoxyProxy.json .check_access.sh