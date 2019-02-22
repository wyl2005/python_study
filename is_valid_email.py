#!/usr/bin/python

import re


def is_valid_email(addr):
    if re.match(r'[0-9a-zA-Z\_\.]+\@[0-9a-zA-Z\_]+.com', addr):
        print('email addr OK')
        return True
    else:
        print('email addr fail')
        return False



assert is_valid_email('someone@gmail.com')
assert is_valid_email('someone@gmail.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
#assert is_valid_email('someone@gmail.com')
