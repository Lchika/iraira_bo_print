# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import datetime
import random

def make_png(time, miss, path):
    image_num = random.randint(1,4)
    im = Image.open("/home/pi/work/iraira/iraira_bo_print/kivy/game_result_label" + str(image_num) + ".png")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf', 100, encoding='unic')
    draw.multiline_text((760,420), str(time) + u' 秒', fill=(0, 0, 0), font=font)
    draw.multiline_text((760,550), str(miss) + u' 回', fill=(0, 0, 0), font=font)
    draw.multiline_text((110,1470), datetime.datetime.today().strftime("%Y-%m-%d %H:%M"), fill=(0, 0, 0), font=font)
    im.save(path, quality=95)

