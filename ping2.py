import argparse
import base64
import os
import socket
import time
import requests

from pylab import *
from pythonping import ping
from skpy import Skype
from settings import *

parser = argparse.ArgumentParser(description='Ping_Check')
parser.add_argument('URL', type=str, help='Input URL')
parser.add_argument('duration', type=str, help='Input duration of work')
parser.add_argument('number_of_pings', type=str, help='Input number of pings')
args = parser.parse_args()
URL = args.URL
duration = float(args.duration)
number_of_pings = float(args.number_of_pings)
gap = duration/number_of_pings


def find_ping(ping_number, delay):
    cnt = 0
    lst = []
    while cnt < ping_number:
        current_ping = ping(socket.gethostbyname(URL)).rtt_avg_ms
        lst.append(current_ping)
        time.sleep(delay)
        cnt += 1
    return lst


def create_plot(ping_values):
    axis_x = []
    cnt = 0
    for ping_number in ping_values:
        cnt += 1
        axis_x.append(cnt)
    fig = plt.figure()
    plot(axis_x, ping_values, 'r')
    xlabel('try')
    ylabel('ping')
    title(PLOT_TITLE)
    fig.savefig(IMG_NAME)


def imgur_upload():
    headers = {
        'Authorization': os.environ['IMGUR_ID'],
    }

    params = {
        'image': base64.b64encode(open(('%s.png' % (IMG_NAME,)), 'rb').read())
    }

    r = requests.post(f'https://api.imgur.com/3/image', headers=headers, data=params)
    data = r.json()
    img_url = data['data']['link']
    return img_url


def skp_msg(image_url):
    sk = Skype(os.environ['SKP_USERNAME'], os.environ['SKP_PSW'])  # connect to Skype
    content = image_url
    ch = sk.contacts[USER_TO_SEND].chat
    ch.sendMsg(content)


create_plot(find_ping(number_of_pings, gap))
skp_msg(imgur_upload())
print('DONE')
