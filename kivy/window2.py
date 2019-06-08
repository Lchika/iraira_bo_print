# -*- coding: utf-8 -*
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
import subprocess
import shlex
import inspng

class Window2(BoxLayout):
    print_data = None
    popup = Popup(title='進捗状況', content=Label(text='ラベル印刷中...', font_size='40sp'),
                  size_hint=(None, None), size=(400, 400))

    def on(self):
        self.popup.open()
        Clock.schedule_once(self.on_impl)
    
    def on_impl(self, dt):
        print('print.')
        if self.print_data != None:
            inspng.make_png(self.print_data['score']['time'], self.print_data['score']['score'], './result.png')
            cmd = "brother_ql print -l 62 --red ./result.png"
            cmd = shlex.split(cmd)
            ret = subprocess.check_output(cmd)
        self.popup.dismiss()

    def off(self):
        print('not print.')

    def set_print_data(self, data):
        self.print_data = data

