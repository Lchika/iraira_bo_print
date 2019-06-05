# -*- coding: utf-8 -*
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import subprocess
import shlex
import inspng

class Window2(BoxLayout):
    print_data = None

    def on(self):
        print('on!')
        if self.print_data != None:
            inspng.make_png(self.print_data['TIME'], self.print_data['SCORE'], './result.png')
            cmd = "brother_ql print -l 62 --red ./result.png"
            cmd = shlex.split(cmd)
            ret = subprocess.check_output(cmd)
 
    def off(self):
        print('off!')

    def set_print_data(self, data):
        self.print_data = data
