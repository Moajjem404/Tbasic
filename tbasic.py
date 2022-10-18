import os, time, sys
os.system('clear')

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

logo2='''

\033[1;32;40m
████████╗\033[1;33;40m██████╗░░█████╗░░██████╗██╗░█████╗░
\033[1;32;40m╚══██╔══╝\33[1;33;40m██╔══██╗██╔══██╗██╔════╝██║██╔══██╗
\033[1;32;40m░░░██║░░░\033[1;33;40m██████╦╝███████║╚█████╗░██║██║░░╚═╝
\033[1;32;40m░░░██║░░░\033[1;33;40m██╔══██╗██╔══██║░╚═══██╗██║██║░░██╗
\033[1;32;40m░░░██║░░░\033[1;33;40m██████╦╝██║░░██║██████╔╝██║╚█████╔╝
\033[1;32;40m░░░╚═╝░░░\033[1;33;40m╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░╚════╝░
\033[1;32;40m
'''

print(logo2)
slowprint('\n Welcome To \033[1;31;40mTermux \033[1;33;40mBasic Installer\n')
time.sleep(1)

s = ' \033[1;31;40m[\033[1;33;40m1\033[1;31;40m] \033[1;36;40mStart Basic Installation \n \033[1;31;40m[\033[1;33;40m2\033[1;31;40m] \033[1;36;40mShow all package \n \033[1;31;40m[\033[1;33;40m3\033[1;31;40m] \033[1;36;40mFollow on Facebook \n \033[1;31;40m[\033[1;33;40m4\033[1;31;40m] \033[1;36;40mGithub \n \033[1;31;40m[\033[1;33;40m5\033[1;31;40m] \033[1;36;40mExit \n'
print(s)


mo = input('\033[1;33;40mEnter \033[1;31;40m>>>\033[1;33;40m ')
  
  
if mo == '1':
  os.system('clear')
  print ('Allow the Button For Access the Storage in Termux')
  os.system('termux-setup-storage')
  os.system ("apt upgrade -y")
  os.system('pkg install python2')
  os.system('pip install --upgrade pip')
  os.system('pip install requests')
  os.system('pip install mechanize')
  os.system('pip2 install requests')
  os.system('pip2 install mechanize')
  os.system('pip2 install bs4')
  os.system('pip install lolcat')
  os.system('pip2 install lolcat')
  os.system('pkg install wget')
  os.system('pkg install php -y')
  os.system('pkg install nano -y')
  os.system('pkg installcurl -y')
  os.system('pkg install tor -y')
  os.system('pkg install openssh')
  os.system('pkg install bash')
  os.system ("apt install python-dev -y")
  os.system('apt install ruby -y')
  os.system('apt install perl -y')
  os.system('apt install nmap -y')
  os.system('apt install clang -y')
  os.system('apt install jq -y')
  os.system('apt install macchanger -y')
  os.system('apt install tar -tar')
  os.system('apt install zip -y')
  os.system('apt install unzip -y')
  os.system('apt install bmon -y')
  os.system ("apt install proot -y")
  os.system ("apt install java -y")
  os.system ("apt install figlet -y")
  os.system('xdg-open https://www.facebook.com/Md.Moajjem.Hossen.4O4')
  os.system('clear')
  print(logo2)
  input('\nPress the enter key to exit ')
  
elif mo == '2':
  os.system('clear')
  print(logo2)
  slowprint('''
[01]  termux-setup-storage
[02]  apt upgrade -y
[03]  pkg install python2
[04]  pip install --upgrade pip
[05]  pip install requests
[06]  pip install mechanize
[07]  pip2 install requests
[08]  pip2 install mechanize
[09]  pip2 install bs4
[10]  pip install lolcat
[11]  pip2 install lolcat
[12]  pkg install wget
[13]  pkg install php -y
[14]  pkg install nano -y
[15]  pkg installcurl -y
[16]  pkg install tor -y
[17]  pkg install openssh
[18]  pkg install bash
[19]  apt install python-dev -y
[20]  apt install ruby -y
[21]  apt install perl -y
[22]  apt install nmap -y
[23]  apt install clang -y
[24]  apt install jq -y
[25]  apt install macchanger -y
[26]  apt install tar -tar
[27]  apt install zip -y
[28]  apt install unzip -y
[28]  apt install bmon -y
[29]  apt install proot -y
[30]  apt install java -y
[31]  apt install figlet -y
  ''')
  m = input('Enter To Continue ')
  if m == '':
    os.system('python tbasic.py')
  
elif mo == '3':
  os.system('xdg-open https://www.facebook.com/Md.Moajjem.Hossen.4O4')
elif mo == '4':
  os.system('xdg-open https://www.github.com/Moajjem404')
elif mo == '5':
  os.system('exit')
  
