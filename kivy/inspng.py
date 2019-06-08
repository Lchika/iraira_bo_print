# coding:utf-8

from PIL import Image, ImageDraw, ImageFont

def make_png(time, score, path):
    im = Image.open("/home/pi/work/iraira/iraira_bo_print/kivy/game_result_label62.png")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf', 200, encoding='unic')
    draw.multiline_text((450,940), 'Time : ' + str(time), fill=(0, 0, 0), font=font)
    draw.multiline_text((450,1240), 'Score :' + str(score), fill=(0, 0, 0), font=font)
    im.save(path, quality=95)

