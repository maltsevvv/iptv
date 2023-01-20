# iptvscan
# Script for scanning and saving IPTV playlist.
# Python v.3 required for using. https://www.python.org/downloads/

# Author: joddude <joddude@gmail.com>
# python3 iptvsearch.py
#------------------------------------------------------------------------------

# A1 Belarus (udp://@233.81.116.1)
protocol = 'udp'
ip_start = '233.81.116.1'
ip_end =   '233.81.116.255'
port = [1234]

timeout=1   # seconds
random_search = False   # False or True

#------------------------------------------------------------------------------

import socket
import struct
import os, sys
import time, datetime
from random import shuffle

#------------------------------------------------------------------------------

def main():
    ip_list = ip_range(ip_start, ip_end)
    if random_search:
        shuffle(ip_list)
    playlist_name = 'IPTV-'+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.m3u'
    found_channels = 0
    print('IP from', ip_start, 'to', ip_end, '('+str(len(ip_list))+')')
    print('Port:', port)
    print('Playlist name:', playlist_name)
    with open(playlist_name, "w") as file:
        print('#EXTM3U', file=file)
        print('', file=file)
        update_progress(0, 'Scan '+ip_start)
        for port1 in port:
            for counter, ip in enumerate(ip_list, start=1):
                if iptv_test(ip, port1, timeout):
                    print('#EXTINF:-1,'+ip, file=file)
                    print(protocol+'://@'+ip+':'+str(port1), file=file)
                    print('', file=file)
                    found_channels +=1
                    time.sleep(1)
                update_progress(counter/len(ip_list), 'Scan '+ip + ':' + str(port1), '(Found '+str(found_channels)+' channels)    ')
    print('Found '+str(found_channels)+' channels')

#------------------------------------------------------------------------------

def iptv_test(ip, port, timeout=1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(timeout)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    mreq = struct.pack("4sl", socket.inet_aton(ip), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    try:
        if sock.recv(10240):
            return True
        else:
            return False
    except socket.timeout:
        return False

#------------------------------------------------------------------------------

def ip_range(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []
    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1
        ip_range.append(".".join(map(str, temp)))
    return ip_range

#------------------------------------------------------------------------------

def update_progress(progress, title='Progress', status = ''):
    barLength = 50
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt"+" "*21+"\r\n"
    if progress >= 1:
        progress = 1
        status = "Done"+" "*21+"\r\n"
    block = int(round(barLength*progress))
    text = '\r'+title+': [{0}] {1}% {2}'.format( '#'*block + '-'*(barLength-block), round(progress*100), status)
    sys.stdout.write(text)
    sys.stdout.flush()

#------------------------------------------------------------------------------

if __name__ == '__main__':
    try:
        print('IPTV scan started. Press Ctrl+C to stop.')
        main()
    except KeyboardInterrupt:
        print()
        print('You pressed Ctrl+C. Stop')
        sys.exit()
    except:
        import sys
        print(sys.exc_info()[0])
        import traceback
        print(traceback.format_exc())
    finally:
        print('IPTV scan finished. Press Enter to exit ...')
        input()