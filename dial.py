from time import sleep
from subprocess import run


with open('config.txt', 'r') as f:
    username = f.readline().strip('\n')
    password = f.readline().strip('\n')
    waittime = int(f.readline().strip('\n'))


while True:
    res = run('ping www.baidu.com -n 1', shell = True)  # 增加 -n 1 的参数，防止运行时间太长

    if res.returncode:
        # run('rasdial Dr.com /DISCONNECT', shell = True)   # 注释该条，以观察现象 2021-4-15 13:23:41
        run('rasdial Dr.com {} {}'.format(username, password), shell = True)
    
    sleep(waittime)
