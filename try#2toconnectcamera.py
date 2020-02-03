import urllib3
http = urllib3.PoolManager()
r = http.request('GET', "http://192.168.86.21/jpg", preload_content=False)

with open("lala.jpg", 'wb') as out:
    while True:
        data = r.read(1024)
        if not data:
            break
        out.write(data)

r.release_conn()
