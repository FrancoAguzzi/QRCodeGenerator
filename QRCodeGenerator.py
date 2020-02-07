#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyqrcode
from pyqrcode import QRCode
import png

def generatesQRCode(baseURL, file_name, file_type='svg'):
    # supports .svg (default) and .png files
    if (file_type == 'png'):
        # generates .png file
        url = pyqrcode.create(baseURL, mode='binary')
        QRimg = url.png(file_name + '.png', scale=8)
    else:
        # generates .svg file
        url = pyqrcode.create(baseURL)
        QRimg = url.svg(file_name + '.svg')
    return QRimg


# TO GENERATE THE QR CODE
# generatesQRCode('https://www.google.com/', 'google', 'png')

