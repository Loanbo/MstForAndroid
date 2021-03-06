# -*- coding: utf-8 -*-
'''
MstCache=>class
For main's some func or other~
update:2013/10/21
'''

from    MstColor   import *
from    os         import listdir,system,path,remove
from    random     import choice
from    MstLoad    import load
from    MstExploit import ver
import re

mstdb   = 'cache/'
plugp   = 'plugins/'
p_exp   = 'exploit'
p_pay   = 'payload'
p_mul   = 'multi'
mstcs   = 'mst'

class cache:
    '''MstCache=>Class::cache'''
    def start(self):
        '''start cache'''
        color.cprint("[*] Start mst ..",GREEN)
        self.inscache(self.getplus(p_exp),p_exp)
        self.inscache(self.getplus(p_pay),p_pay)
        self.inscache(self.getplus(p_mul),p_mul)
        self.banner()
        
    def inscache(self,c,p):
        if path.isfile(mstdb+'%s.txt'%p):
            remove(mstdb+'%s.txt'%p)
	    for tmp in c:
		    tmp=tmp[:len(tmp)-3]
		    self.writetxt(('%s|%s|%s'%(p,tmp,p+'/'+tmp)),p)

    def writetxt(self,txt,txtname):
        try:
            fp = open(mstdb+'%s.txt'%txtname,'a')
            fp.write(txt+"\n")
            fp.close()
        except:
            return False
			
        
    def getplus(self,path):
        '''get plugins list'''
        return listdir(plugp+path)

    def find(self,r,t):
        '''re find'''
        try:
            return re.findall(r,t)
        except:
            return False
		
    def searchexp(self,c,p,sear):
	    for tmp in c:
		    tmp=tmp[:len(tmp)-3]
		    tmpstr='%s'%(p+'/'+tmp)
		    findok=self.find(sear,tmpstr)
		    if findok:
				tmpstr='%s|%s|%s'%(p,tmpstr,tmpstr)
				find_list.append(tmpstr)

    def search(self,sear):
        '''search plugins'''
        global find_list
        find_list=['']
        msg="SEARCH '%s'"%sear
        color.cprint(msg,YELLOW)
        color.cprint("="*len(msg),GREY)
        self.searchexp(self.getplus(p_exp),p_exp,'%s'%sear)
        self.searchexp(self.getplus(p_pay),p_pay,'%s'%sear)
        self.searchexp(self.getplus(p_mul),p_mul,'%s'%sear)
        self.listmst(find_list)
		
    def listmst(self,result):
        '''format print results'''
        color.cprint("%5s %-60s %-7s"%("ID","PATH","TYPE"),YELLOW)
        color.cprint("%5s %-60s %-7s"%("-"*5,"-"*60,"-"*7),GREY)
        exp_id=range(len(result))
        for i in exp_id[1:]:
            tmp=result[int(i)]
            tmp=tmp.split('|')
            rid=i
            rty=tmp[0]
            rpa=tmp[1]
            if len(rpa)>70:
                rpa=rpa[:68]+".."
            color.cprint("%5s %-60s %-7s"%(rid,rpa,rty),CYAN)
        color.cprint("="*74,GREY)
        a=len(result)
        a=a-1
        color.cprint("COUNT [%s] RESULTS (*^_^*)"%a,GREEN)
		
    def opentxt(self,p):
        global exp_list
        global exp_id
        exp_list=['']
        try:
            for line in open(mstdb+'%s.txt'%p):
                exp_list.append(line)
            self.listmst(exp_list)
        except:
            color.cprint('[!] Err!',RED)
            color.cprint('[?] USAGE:show <exploit|payload|multi>',YELLOW)
		
    def showplus(self,p):
        '''show plugins'''
        pp=("show %s plugins"%p).upper()
        color.cprint(pp,YELLOW)
        color.cprint("="*len(pp),GREY)
        self.opentxt(p)

    def load(self,plugin):
        '''load plugins'''
        tmp=exp_list[int(plugin)]
        tmp=tmp.split('|')
        pt=tmp[0]
        plu=tmp[2]
        plu=plu[:-1]
        load.start(pt,plu)
                
    def getplunums(self,p):
        '''get plugins nums'''
        global exp_list
        global exp_id
        exp_list=['']
        for line in open(mstdb+'%s.txt'%p):
            exp_list.append(line)
        return len(exp_list)

    def mainhelp(self):
        '''show mainhelp'''
        color.cprint('MST HELP MENU',YELLOW)
        color.cprint('=============',GREY)
        color.cprint('        COMMAND         DESCRIPTION',YELLOW)
        color.cprint('        -------         -----------',GREY,0)
        color.cprint('''
        help            Displays the help menu
        exit            Exit the MstApp
        cls             Clear the screen
        show            List the plugins
        search          Search plugins
        use             Use the plugin
        update          Update mst|plugins''',CYAN)
        color.cprint('MST HELP::SHOW',YELLOW)
        color.cprint('==============',GREY)
        color.cprint('        COMMAND         DESCRIPTION',YELLOW)
        color.cprint('        -------         -----------',GREY,0)
        color.cprint('''
        exploit         List the exploit plugins
        payload         List the payload plugins
        multi           List the multi plugins''',CYAN)

    def usage(self,c):
        '''mst=>usage'''
        def ius(c):
            '''def's def =.='''
            color.cprint('[?] USAGE:%s'%c,YELLOW)
        if   c == "search":
            ius('search <plugin>')
        elif c == "show":
            ius('show <exploit|payload|multi>')
        elif c == "use":
            ius('use <plugin|pluginID>')
        elif c == "update":
            ius('update <mst|plugins>')
                        
    def ban1(self):
        '''banner 1'''
        color.cprint('''
             ,,          ,      r22r   r::,,:iii   
             B@B       ,@@2   @B@GB@@ rB@B@B@B@B   
             @H@s      @X@s  @B           X@       
             @:,@,    @G Bs  i@B:         GB       
             @r M@   GB  @s    XB@Br      G@       
             Bs  B@ iB,  @s       sB@     MB       
             @s   BSBs   @s        2Bi    M@       
             B9   ;B@   ,BH  B@BMG@BG     @B       
             :     ,     :    ,r22i       ,:
            ''',RED)
    def ban2(self):
        color.cprint('''
                                                                    
                                   ,i77SSXrr,     ,ii               
                            7aWMMMMMMMMMMMMMMMMMMMMMMM              
                        7@MMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                       :MMMMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                        WMMMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                        ,MMMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                         MMMMMMMMMMMMMMMMMMMMMMMMMMMMM              
                         ,MMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                          @MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                          XMMMMMMMMMMMMMMMMMMMMMMMMMM@              
                           MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                           MMMMMMMMMMMMMMMMMMMMMMMMMMM              
                           BMMMMMMMMMMMMMMMMMMMMMMMMMMr             
                           SMMMMMMMMMMMMMMMMMMMMMMMMMMM             
                           iMMMMMMMMMMMMMMMMMMMMMMMMMMMX         7; 
                            MMMMM@B8Z2SXXr;;;:,.,,. . . ,;XZBMMMMMM:
                            S7,.   ..::ii;;7XXX2ZBB@MMMMMMMMMMMMMMMi
                      .:;72aZ8B@MMMMMMMMMMMMMMMMMMMMMMMMMMBaXi.     
              BMMMMMMMMMMMMMMMMMMMMM8a22SXrr;i,:rZZZi               
              XMMMMMWB0Za2X;,:MMMMMWS          7WM.             
                 
''',BLUE)
    def ban3(self):
        color.cprint('''
                                        ,-,                     
                                   -x#######=                   
                                =########XX##+                  
                             .x#########XxXx#x=                 
                            X###########XxxXX#=-                
                          .##########X####Xxxxx=                
                          =###XXxX+xX#X##########x=-            
                          +#XxxX#######################=.       
                         -###########X++x+--;+x###########-     
                       =#########X;.  .         ;-X#########.   
                     +#########+,    ,      ,   .  ;#########   
                   -#########- .    -      -.   ..  ;+#######,  
                  =########+,      =;.    --     -  ..=#####+   
                 .########-    .; =;    ,+- .   X ;  ,.X##x     
                 +#######+ ;   -.-.    =+.    .#. = , .#x       
                 ,#######----  = ,   ;+,    .x# ,X, - ;x#       
                  .#######+--= =    ==   ;=-,, -X#===.x=##      
                     ;+X#=-x+=;-  X#+,.,+++X=-#;  ,;;x+#-.-     
                        -   ####x#==--+-., X-.X;=#+; =x#        
                       .; -+-##. -  X##=   =  .,X#+  -#,        
                        =     x   +       ,.   ;     x=         
                         ;-,, +    -;...,.       ..;-x          
                            .##=                     x          
                             +  =                   -;          
                                 +                -+.           
                                  =X+,.        ,==,   
                                           ''',CYAN)
    def ban4(self):
        color.cprint('''
                             .;+it+;+tt=:                       
                          .iYi;=YY   .IXXXI;                    
                        :IXV,     iX   t+iRBV,                  
                       IVItY  ,#; =#     ,  Y#=                 
                     .XIttIt,  Mi.XV#I ,; ,.  :i                
                     RttYI,  .   :###Y  ,;..., +:               
                    YItI=  .,,:    .           =: :::           
                    Xtt+ ...             :=Y#I .i;,,:+,         
                    RtI      ,=itYRM#########   V     I         
                    XIt  ::#################;  ;R,   =;         
                    iYI    B###BRXVYVVVVBW#X   tVItiV.          
                     VIi    +BBRVVVVVVYVVBI    ItttB:           
                  ::,.YY;     +XWMMRRRRBB;    tttiVi            
                ,+,. ,:iV=       ;iIIIII:,IM##XtiYY             
                t.    ,tXBt.       :IRMt=XR,  tIYI              
                ,+.   +titIYt;=RW#WRt;:;;M=    Vt .;::          
                 .;;=YRItittttXBX:     ,:::   ,;V,,..,+;        
                      ,iYVItttitt             ;,=      +;       
                         ,iYVItiI ,           :         t       
                            .;Ytt; ;        .,.t        =:      
                              :VtI; ...   ..,:IY        i.      
                              ;YttII=;:::;=iIIIIt      :+       
                             = ItittttIIIIIYXVYYVY=:::==        
                            :; tIttttttIYXI=,      ,,,          
                            =:  tYIIIIVI=                       
                            ,+   .,:.i,                         
                             ==     ;,                          
                              ,;;;;:                            
''',PURPLE)
    def banner(self):
        '''mst banner :)'''
        en=self.getplunums('exploit')
        pn=self.getplunums('payload')
        mn=self.getplunums('multi')
        choice([self.ban1,self.ban2,self.ban3,self.ban4])()
        #print u'          =[ 感谢作者的开源'.encode('gb2312')
        print '         +=[',
        color.cprint('MST::For Android By Mr.x ',GREEN)
        print '        -+=[',
        color.cprint('VER::%s'%ver,CYAN)                
        print '    + -- +=[',
        color.cprint('PLU::Exploits::%s Payloads::%s Multis::%s'%(en,pn,mn),YELLOW)
        
    def printmst(self):
        '''print mst..'''
        global mstcs
        color.cprint(mstcs,GREY,0)
        
    def execmd(self,cmd):
        '''run system command'''
        color.cprint('[*] EXEC:%s'%cmd,RED)
        system(cmd)
        
    def cls(self):
        '''clear'''
        if name == 'nt':
            system("cls")
        else:
            system("clear")

    def errmsg(self,msg):
        '''show error msg'''
        color.cprint("[!] Err:%s"%msg,RED)
        
    def mainexit(self):
        '''exit app'''
        color.cprint("\n[*] GoodBye :)",RED)
        exit(0)

if __name__=='__main__':
    print __doc__
else:
    cache=cache()
    #cache.start()
