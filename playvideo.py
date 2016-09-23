#!/usr/bin/python2
from time import sleep
import Adafruit_SSD1306
from PIL import Image
import sys
import cv2
import cStringIO

video = cv2.VideoCapture(sys.argv[1]);

RST = 24

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()

success = True
count = 0
while success:
  count += 1
  success,imgbuf = video.read()
  if success == 0:
    continue
  if count % 4 != 0:
    continue

  print 'Read a new frame: ', success, ' Frame: ' , count
  retval, pngbuf = cv2.imencode('.png', imgbuf);
  image = Image.open(cStringIO.StringIO(pngbuf)).resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
  disp.image(image)
  disp.display()
