#!/bin/bash

OUT="`date +%Y%m%d`prooven_proxies_yt.dat"
rm -f prooven_proxies.dat  socks4.txt  socks5.txt usaproxy.txt
sort prooven_proxies_yt.dat > "$OUT"

ln -f "$OUT" proxies_list.txt
