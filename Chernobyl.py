import mechanize
from mechanize import Browser
import time
import random
import http.cookiejar
import sys


G = '\033[32;1m'
R = '\033[31;1m'
W = '\033[0m'


#LOGO
FBI = """


______       _                 _   
| ___ \     | |               | |  
| |_/ / __ _| |__   __ _  __ _| |_ 
| ___ \/ _` | '_ \ / _` |/ _` | __|
| |_/ / (_| | | | | (_| | (_| | |_ 
\____/ \__,_|_| |_|\__, |\__,_|\__|
                    __/ |          
                   |___/        
                   	
                   	FB SPAM MESSAGING    
	
"""


print(R + FBI + W)


X = raw_input("""
[+] ID/ATTACK : """)
Z = 'uni1bahga'

C = raw_input(G + """
[+] MESSAGE : """ )
#OUTPUT !
WT = """ 
[*] WAIT .... """
print(R + WT )

#BASICS
FBURL = ('https://m.facebook.com/messages/t/' + X )
br = mechanize.Browser() 
cj = mechanize.CookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor() , max_time = (1,2,3) )
br.addheaders={('User-agent' , 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36')}
# select URL & open it
response = br.response()
br.open("https://www.facebook.com/login")

EML = raw_input('YOUR EMAIL : ')
PSW = raw_input("YOUR PASSWORD : ")
# select form

br.select_form(nr=0)

# ATTRS

br.form["email"] = EML
br.form["pass"] = PSW
br.submit(id = "loginbutton" )

#WAIT 1

time.sleep(1.5)

#print(br.title()) / un important .

#CHK
#if br.title() != "Facebook" :
	#print( R + "========[!] ERRoR [!]========")
#else :
# print(G + "SUCSSESFUL LOGIN ! >>> wait for comment ...")	

STRT = """ [!] PROGRAM START . """
print(G + STRT + W)
br.open(FBURL)


def main() : 
    i= int(0)
    N = input("number of msg : ")
    VAL = int(N)
    while(i<VAL) :

        br.select_form(nr=0)
        br.form['body'] = C
        br.submit()
        time.sleep(0.2)
        i+=1
        print( R +"{}".format(i) + " MSG SENT")
    print( G + " [!] PROGRAM END .")


if __name__ == '__main__':main() 
    