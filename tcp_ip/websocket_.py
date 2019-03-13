#!/usr/bin/python

def read_msg(data):
    logging.debug(data)

    msg_len =  data [1] & 127
