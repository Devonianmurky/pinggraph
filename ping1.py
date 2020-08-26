from pylab import *
import time
import socket
from pythonping import ping
URL = input('Enter URL')
duration = float(input('Enter the duration of work'))
number_of_pings = float(input('Enter the number of pings'))
gap = duration/number_of_pings
cnt = 0
lst = []
while cnt < number_of_pings:
    a = (ping(socket.gethostbyname(URL))).rtt_avg_ms
    lst.append(a)
    time.sleep(gap)
    cnt+=1
# узнали значения пинга
x = []
cnt = 0
for i in lst:
    cnt +=gap
    x.append(cnt)
fig = plt.figure()
plot(x, lst, 'r')
xlabel('try')
ylabel('ping')
title('ping_changes')
fig.savefig('мой график')
#создали график
import requests
import base64

headers = {
    'Authorization': 'Client-ID 707b7e215c5b85b',
}

params = {
  'image': base64.b64encode(open('мой график.png', 'rb').read())
}

r = requests.post(f'https://api.imgur.com/3/image', headers=headers, data=params)
#print('status:', r.status_code)
data = r.json()
ImgUrl = data['data']['link']
ImgUrl = 'https://i.imgur.com/crXrimz.png'
#загрузили график на имгур
from skpy import Skype
sk = Skype("username", "password") # connect to Skype
content=ImgUrl
ch = sk.contacts["adushandrii"].chat
ch.sendMsg(content)
#отправили сообщение в скайп
