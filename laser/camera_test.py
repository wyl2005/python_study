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
        #print( r.text );
        if( r.status_code==200 ):
            #print("Test OK")
            img = r.content
            path = './%s.jpg' % name
            with open(path, 'wb') as f:
                f.write(img)
            return True
        else:
            #sys.exit(1);
            print('error: r.status_code = %s' % r.status_code)
            return False



#python upgrade_stm32_tools.py --filename="stm32_laser_cutter_beta09.bin"

def main(argv):
    device_ip = "201.234.3.1"
    action = ""
    filename = ""
    timeout = 10
    
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
    i = 0

    while True: 
        i = i + 1
        ret = httpRequest( url = "http://201.234.3.1:8329/snap", to = 20, name = i)
        #print(ret)
        if ret == True:
            print('Test OK %s' % i)
        else:
            print('Test failed!!! %s' % i)
        time.sleep(3*60)


    sys.exit(0);
   
if __name__ == "__main__":
    main(sys.argv[1:])
   
   
   
