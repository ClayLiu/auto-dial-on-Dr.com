from time import sleep
from subprocess import run


with open('config.txt', 'r') as f:
    username = f.readline().strip('\n')
    password = f.readline().strip('\n')
    waittime = int(f.readline().strip('\n'))


while True:
    res = run('ping www.baidu.com', shell = True)

    if res.returncode:
        run('rasdial Dr.com /DISCONNECT', shell = True)
        run('rasdial Dr.com {} {}'.format(username, password), shell = True)
    
    sleep(waittime)