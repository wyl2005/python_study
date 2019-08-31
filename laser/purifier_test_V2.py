#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, getopt
import requests
import time
#http://docs.python-requests.org/en/latest/user/quickstart/#post-a-multipart-encoded-file


def httpRequest( url, filename = "", to = 3 , name = "photo"):
    try:
        if ( filename is "" ):
            r = requests.get( url, timeout = to );
        else:
            with open( filename, 'rb' ) as f:
                r = requests.post( url, data = f.read(), timeout = to )
                
    except requests.exceptions.ConnectionError:
        print( "connection error" );
        #sys.exit(1);
        return False
    except requests.exceptions.HTTPError as e:
        print( "Error code:", e.response.status_code );
        #sys.exit(1);
        return False
    except requests.exceptions.Timeout:
        print( "time out" );
        #sys.exit(1);
        return False
    except IOError as e:
        print( "Error msg:", e);
        #sys.exit(1);
        return False
    except:
        print( "unknown error" );
        #sys.exit(1);
        return False
    else:

        #print(r.text['result'])
        #if( r.status_code==200 ):
        #if( r.text=="{"result":"ok"}"):
        if "ok" in r.text:
            #print("Test OK")
            #img = r.content
            #path = './%s.jpg' % name
            #with open(path, 'wb') as f:
            #    f.write(img)
            print( r.text );
            return True
        #else if "failed" in r.text:
        else:
            #sys.exit(1);
            print('error: r.status_code = %s' % r.status_code)
            print( r.text );
            return False



#python upgrade_stm32_tools.py --filename="stm32_laser_cutter_beta09.bin"

def main(argv):
    device_ip = "201.234.3.1"
    action = ""
    filename = ""
    timeout = 10

    print('test')
    try:
        opts, args = getopt.getopt(argv,"ha:f:t:d:",["action=","filename=","timeout=","device_ip="])
        
    except getopt.GetoptError:
        print('net_tools.py -a/--action <action> -f/--filename <filename> -t/--timeout <timeout>')
        sys.exit(2)
        
    for opt, arg in opts:
        if opt == '-h':
            print('net_tools.py -a/--action <action> -f/--filename <filename> -t/--timeout <timeout>')
            sys.exit()
        elif opt in ("-a", "--action"):
            action = arg
        elif opt in ("-f", "--filename"):
            filename = arg
        elif opt in ("-t", "--timeout"):
            timeout = arg
        elif opt in ("-d", "--device_ip"):
            device_ip = arg
            
    #httpRequest( url = "http://"+device_ip+":8329/snap, to = 20 )
    close = 0
    open = 0

    while True:
        #close
        print(' ')
        close = close + 1
        print('close times: %s' % close)
        ret = httpRequest( url = "http://"+device_ip+":8080/"+"cnc/cmd?cmd=M17 P0", to = 30 )
        if ret == True:
            print('close OK %s' % close)
        else:
            print('close failed!!! %s' % close)
        time.sleep(30)

        print(' ')
        open = open + 1
        print('open times: %s' % open)
        ret = httpRequest( url = "http://"+device_ip+":8080/"+"cnc/cmd?cmd=M17 P1", to = 30 )
        if ret == True:
            print('open OK %s' % open)
        else:
            print('open failed!!! %s' % open)
        time.sleep(30)
        print('aaa')

    sys.exit(0);
   
if __name__ == "__main__":
    main(sys.argv[1:])
   
   
   
