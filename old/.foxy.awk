{
 if ($0 ~ "--proxy")
   { 
   proxy=$2; 
   printf "echo test %s \ncurl --silent --connect-timeout 60 --output ./tmp.html --proxy %s https://www.wikipedia.org/;  \n[[ \"\$?\" == \"0\" ]] &&  echo success for %s == OK\n",proxy,proxy,$0
   }
}