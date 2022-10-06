
import requests
import os
import sys
import random
import string

FILTERS = [
    "smile",
    "smile_2",
    "hot",
    "old",
    "young",
    "female",
    "male"
]

def upload_photo(path, filter_name, out_path):
    deviceID = ''.join(random.choice(string.ascii_letters) for i in range(8))
    headers = {'User-agent': "FaceApp/1.0.229 (Linux; Android 4.4)", 'X-FaceApp-DeviceID': deviceID}
    res = requests.post('https://node-01.faceapp.io/api/v2.3/photos', headers=headers, files={'file': open(path, "rb")})
    code = res.json().get('code')
    if not code:
        print ('Error getting code')
        sys.exit(1)
    res2 = requests.get('https://node-01.faceapp.io/api/v2.3/photos/%s/filters/%s?cropped=%s' % (code, filter_name, "1"), headers=headers)
    if 'x-faceapp-errorcode' in res2.headers:
        print ("Error %s" % res2.headers['x-faceapp-errorcode'])
        sys.exit(1)
    open(out_path, 'wb').write(res2.content)

upload_photo('tatti.jpg', 'young', 'tatt.jpg')