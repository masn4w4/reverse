#!/usr/bin/python

import socket
import urllib2
import os, re
import sys
import cookielib
import webbrowser


def cls():

    if os.name == "nt":
        os.system('cls' and 'color a')
    else:
        os.system('clear')

cls()

banner = '''
\t\t-----------------------------------------------
\t\t| Recode by n4w4
\t\t| REVERSE IP 
\t\t| cc
\t\t| cara pake ketik diterminal kali linux: python reverseip.py
\t\t| 
\t\t-----------------------------------------------
'''

print banner


def main():
    try:
        host = raw_input('Masukan alamat Site atau IP site : ')
        print ""
        print "Silahkan menunggu,padahal menyebalkan kalo menunggu... "
        if host.startswith("http://"):
            host = host.replace("http://","")
        elif host.startswith("https://"):
            host = host.replace("https://", "")
        else:
            pass

        ip = socket.gethostbyname(host)

        #ip = sys.argv[1]   
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
       
        next = 0
        while(next<=500):

            url = "http://www.bing.com/search?q=ip%3A"+ip+"&first="+str(next)+"&FORM=PORE"
            #print url
            data = urllib2.Request(url)
            box = opener.open(data).read()
            next = next+10
            b = re.findall('<h2><a href="\S+', box)
            for bing in b:
               
                x = bing.replace('<h2><a href="http://', "").replace('/"', "").replace('"', "")
                if x.startswith("www."):
                    x = x.replace("www.", "")
                else:
                    pass

                with open("x.txt", 'a') as f:
                    f.write(x)
                    f.write("\n")

        lines = open("x.txt", 'r').read().split("\n")
        lines_set = set(lines)
        count = 0
        for line in lines_set:
            with open("reverseip.txt", 'a') as neo:
                count = count + 1
                black = line.split("/")[0]
                neo.write(black)
                neo.write("\n")

        print "Total Sites Found: " + str(count)

        os.unlink("x.txt")
        webbrowser.open("reverseip.txt")
               

    except urllib2.HTTPError:
        pass

    except socket.gaierror:
        print ""
        print "Pake Domain yang valid atau IP valid sayang"
        print ""
main()