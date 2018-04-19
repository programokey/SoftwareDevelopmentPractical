from datetime import datetime
import threading
import traceback
import time
from configparser import ConfigParser
cf = ConfigParser()
cf.read('network.conf')
market_port = int(cf.get('DataReceive','port'))

def receive_data():
    import socket
    try:
        s = socket.socket()
        s.bind(('', market_port))
        s.listen(5)

        while True:
            try:
                client, addr = s.accept()  # 接受连接
                recv = ''
                state = 0
                while state != 2:
                    segment = client.recv(1024 * 512)
                if len(segment) == 0:
                    time.sleep(0.1)
                    client.close()
                    break
                if '|' in segment:
                    state = 1
                    recv = segment[segment.find('|') + 1:]
                elif state == 1:
                    recv += segment
                    if '&' in segment:
                        state = 2
                recv = recv[:-1]
    except Exception as e:
        f = open('network.error', 'a')
        f.write(str(datetime.now()) + '\n' + traceback.format_exc(e))
        f.close()