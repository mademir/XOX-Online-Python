from ftplib import FTP
from time import sleep
import os, requests

def getftppass(): #Fetch the server log in password
    r=requests.get("https://dlptest.com/ftp-test/").content.decode()
    return(r[r.index('Password:')+10:].split('<')[0])

## Initialize the ftp connection
f=FTP('ftp.dlptest.com')
f.login(user='dlpuser@dlptest.com',passwd=getftppass())

## Create, upload and delete an empty server file
open('xox_reset','w+b')
f.storbinary('STOR mistik',open('xox_reset', 'rb'))
f.quit()
os.remove('xox_reset')

##Inform via console
print('DONE')
sleep(1)
