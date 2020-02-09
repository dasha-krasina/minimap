import urllib3
http = urllib3.PoolManager()

for i in range(0, 5):
    print("saving image #: " + str(i))
    r = http.request('GET', "http://192.168.86.20/jpg", preload_content=False)
    filename = "image-" + str(i) + ".jpg"
    with open(filename, 'wb') as out:
        while True:
            data = r.read(1024)
            if not data:
                break
            out.write(data)

    r.release_conn()
# This code did not work
