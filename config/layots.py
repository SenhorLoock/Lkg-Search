import random

def banner():
    n = random.randint(1,3)
    if n == 1:
        art = """\033[2;31m
…………..$……………………………………..$…………..
…………$$……………………………………..$$…………
…………$$……………………………………..$$…………
…………..$$s………………………………s$$…………..
…………….$$$$……………………….$$$$…………….
………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………
………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..
………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………
…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………
…………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………
…………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………
………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..
………………..¶¶……..¶¶¶¶……….¶……………………
………………..¶¶……..¶¶¶¶……….¶¶…………………  𝐋𝐊𝐆_𝐒𝐄𝐀𝐑𝐂𝐇.
………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….
………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………………….
……………………….¶¶¶¶¶¶¶¶¶…………………………
……………………….¶..¶..¶..¶..¶…………………………
…………¶…………..¶…………..¶…………..¶………….. \033[7;31mCriador:\033[0;32mL\033[0;31mo\033[0;32mo\033[0;31mc\033[0;32mk\033[0;31m_\033[0;32mA\033[0;31mn\033[0;32md\033[0;31me\033[0;32mr\033[0;31ms\033[0;32mo\033[0;31mn\033[0;31m
……….¶¶……………………………………….¶¶…………     \033[7;31mVersão :\033[0;33m1.0\033[0;31m
……….¶¶……………………………………….¶¶…………   
……….¶¶…………..¶¶……….¶¶…………..¶¶…………
……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………
……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶……..
….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……
……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶……..\033[0;m
        """
        print (art)
    elif n == 2:
        art = '''\033[2;33m
______________¶¶¶
_____________¶¶_¶¶¶¶
____________¶¶____¶¶¶
___________¶¶¶______¶¶
___________¶¶¶_______¶¶
__________¶¶¶¶________¶¶
__________¶_¶¶_________¶¶
__________¶__¶¶_________¶¶____¶¶
__________¶__¶¶__________¶¶¶¶¶¶¶
_________¶¶__¶¶¶______¶¶¶¶¶¶___¶
_________¶¶___¶¶__¶¶¶¶¶¶__¶¶
_______¶¶_¶____¶¶¶¶________¶¶
______¶¶__¶¶___¶¶__________¶¶
_____¶¶____¶¶___¶¶__________¶¶
___¶¶_______¶¶___¶¶_________¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_________¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶________¶¶
¶¶__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶______¶¶
¶¶¶¶¶___¶______¶___¶¶¶¶¶_____¶¶
________¶¶¶¶¶¶¶¶______¶¶¶¶¶_¶¶
______¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶
______¶¶¶¶¶¶¶¶¶¶¶¶
______¶__¶¶_¶¶¶¶¶¶  𝐋𝐊𝐆_𝐒𝐄𝐀𝐑𝐂𝐇.
_____¶¶______¶___¶  \033[7;31mCriador:\033[0;32mL\033[0;31mo\033[0;32mo\033[0;31mc\033[0;32mk\033[0;31m_\033[0;32mA\033[0;31mn\033[0;32md\033[0;31me\033[0;32mr\033[0;31ms\033[0;32mo\033[0;31mn\033[0;33m
_____¶¶_____¶¶___¶  \033[7;31mVersão :\033[0;33m1.0\033[0;33m
_____¶______¶¶___¶
____¶¶______¶¶___¶¶
____¶¶______¶¶___¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶
__¶¶________¶¶¶____¶¶
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\033[0;m

        '''
        print (art)
    else:
        art = '''\033[2;32m____________________$___$
_____________________$$$
_____________________$_$
_____________________$_$
___________________$$$_$$$
_________________$$__$$$__$$$
_______________$$__$$$$$$$___$
______________$_______________$
_____________$_________________$
_____________$_________________$
_____________$_____$$$$$$$$$$$$$$$
_____________$____$_______________$
_____________$____$___$$$$$$$$$$$$$
_____________$___$___$___________$$$
_____________$___$___$_$$$___$$$__$$
_____________$___$___$_$$$___$$$__$$
_____________$___$___$___________$$$
_____________$____$___$$$$$$$$$$$$$
_____________$_____$$$$$$$$$$$$$$
_____________$_________________$   𝐋𝐊𝐆_𝐒𝐄𝐀𝐑𝐂𝐇. 
_____________$____$$$$$$$$$$$$$$
_____________$___$__$__$__$__$      \033[7;31mCriador:\033[0;32mL\033[0;31mo\033[0;32mo\033[0;31mc\033[0;32mk\033[0;31m_\033[0;32mA\033[0;31mn\033[0;32md\033[0;31me\033[0;32mr\033[0;31ms\033[0;32mo\033[0;31mn\033[0;32m
_____________$__$$$$$$$$$$$$$$      \033[7;31mVersão :\033[0;33m1.0\033[0;32m
_____________$__$___$__$__$__$
_____________$___$$$$$$$$$$$$$$$
____________$$$_________________$$$
__________$$___$$$_________$$$$$___$$
________$$________$$$$$$$$$__________$$$
_______$__$$_____________________$$$$___$$
____$$$$$___$$$$$$$$______$$$$$$$_______$_$
__$______$$_________$$$$$$______________$_$$
_$____$____$____________________________$_$_$
_$_____$___$______________$$$$$$$$$$$___$_$_$$
_$$$____$___$__$$$$$$$$$$$$__________$___$_$_$$
$___$$$$____$__$_____________________$___$_$$_$
$$$____$___$$__$_____________________$$__$_$__$
$___$__$__$$___$______________________$__$$$__$
$_____$$_$$____$_______________$$$____$__$_$__$\033[0;m

        '''
        print (art)
def main():
    Main = '''\033[2;33m
    [\033[2;35m01\033[2;33m]\033[2;32m Consultar Ipv4    \033[0;32m (ONN)\033[2;33m
    [\033[2;35m02\033[2;33m]\033[2;32m Consultar Cep      \033[0;32m(ONN)\033[2;33m
    [\033[2;35m03\033[2;33m]\033[2;32m Gerar Malware      \033[0;32m(ONN)\033[2;33m
    [\033[2;35m04\033[2;33m] \033[2;32mCtr. Malware       \033[0;32m(ONN)\033[2;33m
    [\033[2;35m05\033[2;33m] \033[2;32mCreditos           \033[0;32m(ONN)\033[2;33m
    [\033[2;35m00\033[2;33m] \033[2;31mExit\033[0;m
    '''
    print (Main)
    
def cursor():
    PS1= '\033[2;32m>\033[2;33m>\033[2;32m>\033[0m'
    response = input(PS1)
    return response
    
def ipsearch():
    
    layot = '''
\033[0;36m
Digite o Ip Abaixo:\033[0;m
    '''
    print (layot)
    
def page_home():
    layot = '''
\033[0;31mDeseja Voltar Ao Menu Inicial? \033[0;33mPrecione Enter!\033[0;m
    '''
    print (layot)
    response = cursor()
    return response
    
def cepsearch():
    
    layot = '''
\033[0;36m
Digite o Cep Abaixo:\033[0;m
    '''
    print (layot)
def gn_malware():
    layot = '\033[0;36mDigite o porta Abaixo:\033[0;m'
    print (layot)
def ctr_malware():
    layot = '\033[0;36mDigite o Comando Abaixo:\033[0;m'
    print (layot)
    