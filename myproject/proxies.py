import pymongo,requests,json
from multiprocessing import Pool

def run(i):

    ip={'http':'http:%s'%i}
    n = 3
    while n>0:
        try:
            requests.get('https://github.com/qiyeboy/IPProxyPool',proxies=ip,timeout=1)
        except:
            print('剩余次数%s'%(int(n)-1))
            n-=1
        else:
            print('sucessful',ip)
            client=pymongo.MongoClient()
            db=client['proxies']
            collection=db['ip']
            ips={'ip':'%s'%i}
            collection.insert(ips)
            print('is alredy in the file')
            break
        if n==0:
            print('need remove %s'%ip)

if __name__=='__main__':
    n=110
    r = requests.get('http://127.0.0.1:8000/?types=0&count={}&country=国内'.format(n))
    ip_ports = json.loads(r.text)
    p = Pool()

    for i in range(n):
        ip = ip_ports[i][0]
        port = ip_ports[i][1]
        ips=('%s:%s'%(ip,port))
        #print(ips)
        p.apply_async(run,(ips,))
    p.close()
    p.join()












