# -*- coding: utf-8 -*-
from os import listdir

color.cprint("[?] ����:",YELLOW,0) 
ftype = raw_input("")

if len(ftype)>0:
    tmp=listdir("output")
    color.cprint("[*] portport���ļ�ID..",YELLOW)
    for i in range(len(tmp)):
        color.cprint("[%s] %s"%(i,tmp[i]),PURPLE)
    color.cprint("[?] �б�:",YELLOW,0)
    lf = raw_input("")
    try:
        ii = int(lf)
        ff = tmp[ii]
        if len(lf)>0:
            flist = open("output/%s"%ff).readlines()
            for i in range(len(flist)):
                f = flist[i]
                f = f.strip("\n")
                f = f.replace("http://","")
                color.cprint("[+] AUTO-FUCK::[%s/%s]"%(i+1,len(flist)),CYAN)
                mm.setp(ftype,f)
                mm.exploit()
    except Exception,e:
        color.cprint("[!] ERR:%s"%e,RED)
else:
    color.cprint("[?] ����:URL",RED)
