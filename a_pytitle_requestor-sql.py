#############################################################################
# 				Documentation				    #
#############################################################################
#-d dbnavn -f a_vman2-teil1.txt -i x,y.c -o utfil
# -r %tes% -i test2,test2,7-22Ql73VWY -o pyfileout.txt -p x
#-r %tes% -i test2,test2,7-22Ql73VWY -o pyfileout.txt -p x -f a_vman2-teil1.txt
#. -r %tes% -i test2,test2,7-22Ql73VWY -o pyfileout.txt -p x -f a_vman2-teil1.txt

# 7-22Ql73VWY

#WEHRMACHT 1939 - Uniform zu Kriegsbeginn erklärt!\n', 'https://www.youtube.com/embed/7-22Ql73VWY\n'
# Python program to
# demonstrate with
# statement
import urllib.request
import json
import urllib
import pprint
import re
import sqlite3
import webbrowser
import hashlib
import datetime
import sys, getopt
import argparse
#############################################################################
# 				globals		    #
#############################################################################
database="vman156.db"
database_t='xxxxxxx'
DBNAME = "vman445.db"
pyinsert = "q,w,s"
pyfile_out=''
pyfile = "a-vman2-fileurl-Test.txt"
pyfile = "a_vman2-teil1.txt"
pyfile = "pyt_teil2.txt"
pyfile = "a-vman2-teil3.txt"
pyfile = "a-vman2-teil2.txt"
pyfile = "a_vman2-teil1.txt"
#pyfile = "a-vman2-teil4.txt"
#pyfile = "a-vman2-teil1.txt"
#pyfile = "pyttest.txt"
g_url='bull'
opt_w=0
opt_t=0
opt_u=0
opt_r=0
opt_c=0
opt_p=0
opt_f=0
opt_o=0
opt_d=0
opt_h=0
opt_s=0
opt_i=0

g_lpat='%'
lpat=''
db_insert_w=0

special_star=0
special_grind=0
special_quest=0
special=0
line_title=0
line_http=0
line_title_saved=""
line_http_saved=""
line_list=[]
g_line=''
weburl=''
ytitle=''
#symbol = input()
vc1="music"
vc2='na2'
vc3='na3'
vc4='na4'
vc5='na5'
vt1='wh1'
vt2='WEHRMACHT 1939 - Uniform zu Kriegsbeginn erklärt!'
vu1='https://www.youtube.com/embed/7-22Ql73VWY'
vi1='22Ql73VWY'
vd1='13.06.2023'
vx1='13.06.24'

db_find = input('Enter your string here:')
print(db_find)
db_name = input('Enter your db string here:')
print(db_name)

sqv=sqlite3.version
print(sqv)
#############################################################################
# 				sql connect		    #
#############################################################################
print("db_connect-e")
#verbindung = sqlite3.connect("vman3.db")
#verbindung = sqlite3.connect("vman445.db")
verbindung = sqlite3.connect(database=database)
zeiger = verbindung.cursor()
print("-------------------------")   
#############################################################################
# 				create table			    #
#############################################################################
def db_create_tab():
  print("db_init-e")
 #verbindung = sqlite3.connect(db_name)
 #zeiger = verbindung.cursor()
  sql_anweisung = """
  CREATE TABLE IF NOT EXISTS videos1 (
  vcat1 VARCHAR(10), 
  vcat2 varchar(10),
  vcat3 vchar(10),
  vcat4 vchar(10),
  vcat5 vchar(10),
  vtitle1 VARCHAR(80),
  vtitle2 VARCHAR(80), 
  vurl   VARCHAR(255),
  vid   VARCHAR(11) UNIQUE,
  vdate DATE,
  vexp DATE,
  PRIMARY KEY (vurl)
  );"""
 #except:
  print("except")
  zeiger.execute(sql_anweisung)
  verbindung.commit()
  print("db_init-x")
 
db_create_tab()


#############################################################################
# 				args	    #
#############################################################################



argParser = argparse.ArgumentParser()
argParser.add_argument("-t", "--tit", help="title1")
argParser.add_argument("-u", "--url", help="url")
argParser.add_argument("-r", "--rem", help="title2")
argParser.add_argument("-c", "--cat", help="cat2")
argParser.add_argument("-w", "--write",help="wdb")
argParser.add_argument("-p", "--put", help="wfile")
argParser.add_argument("-f", "--fili", help="ifile")
argParser.add_argument("-o", "--filo", help="ofile")
argParser.add_argument("-d", "--dbn", help="dbnam")
argParser.add_argument("-z", "--hel", help="help")
argParser.add_argument("-s", "--star", help="ign*")
argParser.add_argument("-i", "--ins", help="insert")
argParser.add_argument("-x", "--int", type=int, help="your numeric age ")

args = argParser.parse_args()
print("args=%s" % args)
#lpat=args.name
#opt_c=1
print("args.tit=%s" % args.tit)
print(args.tit)
print("args.url=%s" % args.url)
print(args.url)
print("args.rem=%s" % args.rem)
print("args.cat=%s" % args.cat)
print("args.write=%s" % args.write)
print("args.age=%s" % args.int)
if args.tit:
	lpat=args.tit
	opt_t=1
	print("tit")
if args.url:
	lpat=args.url
	opt_u=1
	print("url")
if args.rem:
	lpat=args.rem
	opt_r=1
	print("rem")
#if args.cat != 'None':
if args.cat:
	lpat=args.cat
	opt_c=1
	print("cat")
#if args.write != 'None':
if args.write:
	#lpat=args.cat
	opt_w=1
	db_insert=1
	print("write")
if args.put:
	#lpat=args.cat
	opt_p=1
	print("put")
if args.fili:
	#lpat=args.cat
	opt_f=1
	pyfile=args.fili
	print("fili")
if args.filo:
	#lpat=args.cat
	opt_o=1
	pyfile_out=args.filo
	print("filo")
if args.dbn:
	#lpat=args.cat
	opt_d=1
	database_t=args.dbn
	print("dbn")
if args.star:
	#lpat=args.cat
	opt_s=1
	print("star")
if args.ins:
	#lpat=args.cat
	opt_i=1
	pyinsert=args.ins
	print("ins")
	
print("lpat=%s" % lpat)
print("pyfile=%s" % pyfile)
print("pyfile_out=%s" % pyfile_out)
print("database_t=%s" % database_t)
print("pyinsert=%s" % pyinsert)
print("pyfile=%s" % pyfile)
print("db_insert_w =%s" % db_insert_w)


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"ht:u:r:c:w",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -t <inputfile> -u <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -t <inputfile> -u <outputfile>')
         sys.exit()
      elif opt in ("-t", "--ifile"):
         inputfile = arg
         lpat = arg
         opt_t=1
         print("opt_t")
      elif opt in ("-u", "--ifile"):
         inputfile = arg
         lpat = arg
         opt_u=1
         print("opt_u")
      elif opt in ("-c", "--ifile"):
         inputfile = arg
         lpat = arg
         opt_c=1
         print("opt_c")
      elif opt in ("-w", "--ifile"):
         inputfile = arg
         lpat = arg
         opt_w=1
         print("opt_w")
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('Input file is ', inputfile)
   print ('Output file is ', outputfile)
   print ('lpat is ', lpat)
   print ('g_lpat is ', g_lpat)
   g_lpat=lpat
print("args calling")
#if __name__ == "__main__":
   #main(sys.argv[1:])
#############################################################################
# 				write hole file   #
#############################################################################
def py_write():
     if opt_p != 1:
       print("filewrite skipped")
       return (0)
     print("file {} being written",format(pyfile_out))
     file1 = open(pyfile_out, 'w', encoding="utf-8")
     file1.writelines(line_list)
     file1.close()
#############################################################################
# 				date time	    #
#############################################################################
def pytime():
 #tf='2012, 2, 23, 18, 6'
 x = datetime.datetime.now()
# x = datetime.datetime(2012, 2, 23, 18, 6)
 #x=datetime.datetime(tf)
 
 print("date_time {} ".format(x))
 #x_r= x.strftime('%m/%d/%Y')
 x_r= x.strftime('%d-%m-%y')
 print("x-r {} ".format(x_r))
 return x_r
 print(x)
pytime()
#############################################################################
# 			hash	    #
#############################################################################
def hash(a_string):
# Hash a single string with hashlib.sha256
#import hashlib

#aa_string = 'this string holds important and private information'

 hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
 print("hashedstring {} ".format(hashed_string))
 hashed_string_r=hashed_string[0:11]
 print("hashedstring-r {} ".format(hashed_string_r))
 return hashed_string_r

hash("bullfash")
# Returns:
# 4e7d696bce894548dded72f6eeb04e8d625cc7f2afd08845824a4a8378b428d1
#############################################################################
# 				db_insert		    #
#############################################################################
"""
db_insert
"""
def db_insert(vc1,vc2,vc3,vc4,vc5,vt1,vt2,vu1,vi1,vd1,vx1):
 #if opt_w != 1:
 if db_insert_w != 1:
  print("db_insert-x")
  return (0)
 try:
  print("db_insert-e-try")
	#print("db_insert_e")
  #zeiger.execute("INSERT INTO videos1 VALUES 
 # (?,?,?,?,?,?,?,?,?,?,?)", (vc1,vc2,vc3,vc4,vc5,vt1,vt2,vu1,vi1,vd1,vx1))
  vd1=datetime.datetime.now()
  zeiger.execute("INSERT OR REPLACE INTO videos1 VALUES (?,?,?,?,?,?,?,?,?,?,?)", (vc1,vc2,vc3,vc4,vc5,vt1,vt2,vu1,vi1,vd1,vx1))
  print("db_insert_x")
  verbindung.commit()
 #except:
 except Exception as e:
  errnum = e.args
  print(e)
  print("urlexcept 33333333333333333333333334333333333333333{} e {} ".format(errnum, e))
  print("******* insert except")
print("******* after insert except")
#print(g_url)
#weburl = "\n" + g_url + '\n'
#weburl='https://www.youtube.com/watch?v=b5xUKGzuea8'
##https://m.youtube.com/watch?v=xDNT1qnDkd4
#############################################################################
# 				url_split	    #
#############################################################################
def url_split(weburl):
  print("-----url_split---")
  print(weburl)
  print(weburl.split())
  print(weburl.split('\u200b\u200b'))
  weburl_split_200b=weburl.split('\u200b\u200b')
  weburl_split_200b_len=len(weburl_split_200b)
  print("len {} ".format(weburl_split_200b_len))
  if weburl_split_200b_len == 2:
#print("-----split----")
#print("len {} ".format(weburl_split_200b_len))
    print("split2")
    weburl_split1=weburl_split_200b[0]
    weburl_split2=weburl_split_200b[1]
    print(weburl_split2)
    weburl_out=weburl_split2
  else:
    print("split1")
    weburl_split1=weburl_split_200b[0]
    weburl_out=weburl_split1
  print("weburl_out {} ".format(weburl_out))
  weburl_split_out=weburl_out.split('\u200b\u200b')
  weburl_split_out_len=len(weburl_split_out)
  print("len {} ".format(weburl_split_out_len))
  return weburl_out
#############################################################################
# 				yt_get_tit	    #
#############################################################################
def yt_get_tit(yt_id):
	params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % yt_id}
	url = "https://www.youtube.com/oembed"
	query_string = urllib.parse.urlencode(params)
	url = url + "?" + query_string



#try:
   #print(x)
#except:
  # print("An exception occurred")
	
#try:      
      #urllib.request.urlopen(req) 
#except urllib.error.HTTPError as e:     
     # print(e.reason)
    
  #with urllib.request.urlopen(url) as response:
  #try:
   #print("tryurl")
  #except:
   #print("excepturl")
	with urllib.request.urlopen(url) as response:
	    response_text = response.read()
	    data = json.loads(response_text.decode())
	    #pprint.pprint(data)
	    #print(data['title'])
	    #print(VideoID)
	    print (f"URLlIB\n{yt_id} tit={data['title']}")
	    return  data['title']
#############################################################################
# 				main	   loop #
#############################################################################
# Using for loop
count = 0
print("\nUsing for loop 2028")
#pyfile = "a-vman2-teil4.txt"
with open(pyfile, encoding="utf-8") as fp:
#with open(pyfile) as fp: ascii out of range uni??
    for line in fp:
        count += 1
        yt_yes=0
        http_yes=0
        line_h=""
        line_http=0
        linetitle=0
        g_line=line
        line_special=0
        special=0
        print("type-line {}".format(type(line)))
        line_encode = line.encode("utf-8")
        print("line-encode {}".format(line_encode))
        s = "Hello!"
        e=line.encode('unicode_escape') 
        print(e)
        #u = unicode(s, "utf-8")
        #print("Line{}: {}"
        print("Linestrip {}: {}".format(count, line.strip()))
        print("Line count -------------------------- {}: {}---".format(count, line[0:20]))
        #if line[0:2].encode('utf-8') == 'ht':
        if line.find('https') != -1:
        	print("httpyyyyyyyyes")
        else:
          print("htnooooooo")
          print(line[0:4])
        #if re.search('​​b"xe2\x80\x8b\xe2\x80\x8b'",line):
        #if re.search('​​\xe2\x80\x8b',line):
        if re.search('\x8b',line):
          print("hardspace")
        else:
          print("nohardspace")
        if re.search('^\*',line):
          print("specialstar")
          special_star=1
          special=1
        else:
          print("nospecialstar")

        if re.search('^\#',line):
          print("specialgrind")
          special_star=1
          special=1
        else:
          print("nospecialgrind")
        
        if re.search('^\?',line):
          print("specialQ")
          special_star=1
          special=1
        else:
          print("nospecialq")
          
        if (count % 2) == 0:
          print("line_http")
          line_http=1
          line_title=0
          line_http_saved=line
        else:
          print("line_title")
          line_title=1
          line_http=0
          line_title_saved=line
        vc2="pending"
        z=url_split(line)
        find_3sat=line.find('3sat')
        re_s_3sat=re.search('3sat',line)
        print("find_search_3sat find: {} srch:{} ".format(find_3sat, re_s_3sat))
        print("find_search_arte find: {} srch:{} ".format(line.find('arte.tv'), re.search('arte.tv',line)))
        
        if re.search('archive.org', line) and line_http:
          vc2="archive"
          print("vc2-archive {}".format(line))
        #if re.search('sat', line) and line_http:
        if (line.find('3sat.de') != -1) and line_http:
          vc2="3sat"
          print("vc2-3sat_find {} : ".format(line))
        if re.search('zdf', line) and line_http:
          vc2="zdf"
          print("vc2-zdf {}".format(line))
        if re.search('rbb', line) and line_http:
          vc2="rbb"
          print("vc2-rbb {}".format(line))
        if re.search('ard', line) and line_http:
          vc2="ard" 
          print("vc2-ard {}".format(line))
        if re.search('arte.tv', line) and line_http:
          vc2="arte"
          print("vc2-arte {}".format(line))
        if re.search('kabeleinsdoku', line) and line_http:
          vc2="k1doku"
          print("vc2-k1doku {}".format(line))
        #if line[0:2] == 'ht': unicode problems
        #if line.find('https') != -1:
        #if re.search('^https', line):
#############################################################################
# 				normal https		    #
#############################################################################
        if re.search('https:', line) and special == 0:
          #if re.match('https:', line):
           line_h = line
           http_yes=1
           print("ht...")
           #print(line[-11:])
           #if line.find('youtube') != -1:
           if re.search('youtube', line):
            print("youtubereee")
            yt_yes=1
           else:
            #if line.find('youtu.be') != -1:
            if re.search('youtu', line):
             print("youtu.bereeeeee")
             yt_yes=1
            else:
             print("non-ytxxxxx{}".format(yt_yes))
             print(line)
        print("debug2257")
        print("yt_yes: {} http_yes: {}".format(yt_yes, http_yes))
        line_strip=line.strip()
#############################################################################
# 				 yt	    #
#############################################################################
        if yt_yes !=0:
          print("Line{}: {}".format(count, line.strip()))
          #line_strip=line.strip
          print(line_strip)
          print("ytid: {}".format(line_strip[-11:]))
          yt_vid=line_strip[-11:]
          
          try:
           yt_tit=yt_get_tit(yt_vid)
          #except(e):
          except Exception as e:
           yt_tit="yt_get_tit failed"
           errnum = e.args
           print(e)
           print("urlexcept 33333333333333333333333334333333333333333{} e {} ".format(errnum, e))
           #yt_tit=e
           #quit(0)
           #exit(9)
          print("yt_vid: {} tit: {}".format(yt_vid, yt_tit))
          print("---------2017yttt------")
          print(yt_tit)
          line_list.append(yt_tit + '\n')
          print(line_h.strip())
          line_list.append(line_h)
          vu1=line_h.strip()
          #vu1=g_line.strip()
          #vt1=yt_tit
          vi1=yt_vid
          vt2=line_title_saved.strip()
          vd1=pytime()
          yt_hash=hash(vu1)
          print("ytttttttubevd1 {} ".format(vd1))
          print (yt_hash)
          vt1=yt_tit
          vc2="pytube"
          db_insert(vc1,vc2,vc3,vc4,vc5,vt1,vt2,vu1,vi1,vd1,vx1)
#############################################################################
# 				http and not yt	    #
#############################################################################
          print("------------------------------")
        if (http_yes != 0 and yt_yes != 1):
            print("**http not 0 and yt not 1***-")
           # print("ytfree")
            print(line_h.strip())
            line_list.append(line_title_saved)
            line_list.append(g_line)
            vu1=g_line.strip()
            vt2=line_title_saved.strip()
            yt_hash=hash(vu1)
            print("hashbbbbbbbb")
            print (yt_hash)
            vi1=yt_hash
            vd1=pytime()
            #vt1=yt_tit
            db_insert(vc1,vc2,vc3,vc4,vc5,vt1,vt2,vu1,vi1,vd1,vx1)
            print("http!=0***ytyes0*********")
            print("?????")
#############################################################################
# 				http and not yt and special (*, #. ?
#############################################################################
        if (special != 0 and yt_yes != 1 and line_http == 1):
            print("*special and not yt and http**-")
           # print("ytfree")
            print(line_title_saved)
            line_list.append(line_title_saved)
            print(g_line.strip())
            line_list.append(g_line)
            vu1=g_line.strip()
            vt2=line_title_saved.strip()
            vi1=yt_vid
            yt_hash=hash(vu1)
            print("hashcccccccc")
            print (yt_hash)
            vi1=yt_hash
            vd1=pytime()
            db_insert(vc1,vc2,vc3,vc4,vc5,vt1,vt2,vu1,vi1,vd1,vx1)
            print("bueninsdb********************")
            print("?????")
#at end of main program
    print(line_list)
    # writing to file
#def py_write():
     #file1 = open('pytest_write4.txt', 'w', encoding="utf-8")
     #file1.writelines(line_list)
     #file1.close()
    print("--------selectfromvideos1--")
    for row in zeiger.execute('SELECT * FROM videos1 ORDER BY vcat1'):
        print( row)
    print("-----------xxxxxxx-titles-----------")
    for rowx in zeiger.execute("SELECT * FROM videos1 WHERE vtitle2=?", (db_find,)):
   # videos1 WHERE vtitle2=?", ('s',)):
        pf=rowx
        print(pf)
        g_url = rowx[7]
        weburl =rowx[7]
        ytitle=rowx[5]
        #webbrowser.open(g_url, new=0, autoraise=True)
    print("-sel vtitle2 vurl1 vtitle1=wh1---------")
    for rowx in zeiger.execute("SELECT vurl FROM videos1 WHERE vtitle1=?", (db_find,)):
        pf=rowx
        print(pf)
        print("Total rows are:  ", len(rowx))
        print("Printing each row")
        print("Id: ", rowx[0])
        print("Id: ", rowx[1])
        print("Id: ", rowx[2])
        print("Id: ", rowx[3])
        print("Id: ", rowx[4])
        print("Id: ", rowx[5])
        print("Id: ", rowx[6])
        print("Id: ", rowx[7])
        print("Id: ", rowx[8])
        print("Id: ", rowx[9])
        print("Id: ", rowx[10])
        #g_url = row[7]
        weburl=rowx
        weburl=rowx[7]
        ytitle=rowx[5]
    print("------------likestart-------------llllllllllllllll")
    print("-sel vtitle2 vurl1 vtitle1=wh1---------")
    #lpat='%' + lpat + '%'
    lrow='vtitle2'
    kword='1945'
    print("g_lpat: {} ".format(g_lpat))
    print("lpat: {} ".format(lpat))
    print("sssssssssssssssssssssssssssssssssss")
    #for rowx in zeiger.execute("SELECT * FROM videos1 WHERE ? LIKE ? ", [lrow, lpat,]):
    if opt_c:
     print("opt_c")
     for rowl in zeiger.execute("SELECT * FROM videos1 WHERE vcat2 LIKE ? ", [lpat]):
       print("opt_c {} : ".format(rowl))
    if opt_u:
      print("opt_u")
      for rowl in zeiger.execute("SELECT * FROM videos1 WHERE vurl LIKE ? ", [lpat]):
        print("opt_u {} : ".format(rowl))
    if opt_r:
      print("opt_r")
      for rowl in zeiger.execute("SELECT * FROM videos1 WHERE vtitle2 LIKE ? ", [lpat]):
    	  print("opt_r {} : ".format(rowl))
    if opt_t == 1:
      print("opt_t")
      for rowl in zeiger.execute("SELECT * FROM videos1 WHERE vtitle1 LIKE ? ", [lpat]):
        print("opt_t {} : ".format(rowl))
        prowl=rowl
        print(prowl)
        print("Total fields are:  ", len(rowl))
        print("Printing each row")
        print("Id: ", rowl[0])
        print("Id: ", rowl[1])
        print("Id: ", rowl[2])
        print("Id: ", rowl[3])
        print("Id: ", rowl[4])
        print("Id: ", rowl[5])
        print("Id: ", rowl[6])
        print("Id: ", rowl[7])
        print("Id: ", rowl[8])
        print("Id: ", rowl[9])
        print("Id: ", rowl[10])
        #g_url = row[7]
        weburl=rowx
        weburl=rowx[7]
        ytitle=rowx[5]
        print("Total fields are:  ", len(rowl))
    print("------------likeend--------------------")
    if opt_i != 0:
      print("optinsert-e")
      print("pyinsert {}".format(pyinsert))
      pyinsert_s=pyinsert.split(',')
      print("pyinsert_s {}".format(pyinsert_s))
      pyinsert_sl=len(pyinsert_s)
      print("pyinsert_sl {}".format(pyinsert_sl))
      print("pyinsert_s0 {}".format(pyinsert_s[0]))
      print("pyinsert_s1 {}".format(pyinsert_s[1]))
      print("pyinsert_s2 {}".format(pyinsert_s[2]))
      vc1="vc1t"
      vc2=format(pyinsert_s[0])
      vc3="vc3t"
      vc4="vc4t"
      vc5="vc5t"
      vt1="vt1t"
      vi1="12345678901"
      vi1=format(pyinsert_s[2])
      try:
           vt1=yt_get_tit(vi1)
          #except(e):
      except Exception as e:
           vt1="yt_get_tit failed"
           errnum = e.args
           print(e)
           print("urlexcept 33333333333333333333333334333333333333333{} e {} ".format(errnum, e))
      vx1="2023-06-16"
      vt2=format(pyinsert_s[1])
      vu1='https://www.youtube.com/embed/' + vi1
      print("vu1 {} ".format(vu1))
      #vu1="testurl"
      #opt_w=1
      db_insert_w = 1
      db_insert(vc1,vc2,vc3,vc4,vc5,vt1,vt2,vu1,vi1,vd1,vx1)
      line_list.append(vt1 + '\n')
      #print(line_h.strip())
      line_list.append(vu1)
      #vu1=line_h.strip()
      print("optinsert-x")
      print(line_list)
#############################################################################
# 				eop			    #
#############################################################################
print("pywrite")
py_write()
print("end of program")
verbindung.close()
#print(g_url)
#weburl = "\n" + g_url + '\n'
#weburl='https://www.youtube.com/watch?v=b5xUKGzuea8'
##https://m.youtube.com/watch?v=xDNT1qnDkd4

print("weburl {} ".format(weburl))
url4browser=url_split(weburl)
print("url4browser {} ".format(url4browser))
url4browser_s=url4browser.split('\u200b\u200b')
url4browser_s_l=len(url4browser_s)
print("len {} ".format(url4browser_s_l))
print("title1 {} ".format(ytitle))

#webbrowser.open(url4browser, new=0, autoraise=True)
#urls_arr=['xyz.com','ybk.com']
#for i in urls_arr:
#    st.markdown(f"<iframe src='{i}'></iframe>", unsafe_allow_html=True)

