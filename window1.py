# -*- coding: utf-8 -*
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class Window1(BoxLayout):
    
    def button_press(self):
        popup_content = GridLayout(cols = 1)

        popup_close = Button(
            text = 'OK',
            size_hint_y = None,
            height = 40)

        popup_content.add_widget(Label(text = 'ウィンドウ 1 ポップアップ'))
        popup_content.add_widget(popup_close)
        popup = Popup(
            title = 'Test popup',
            size_hint = (None, None),
            size = (256, 256),
            content = popup_content)
        popup_close.bind(on_release = popup.dismiss)

        popup.open()
