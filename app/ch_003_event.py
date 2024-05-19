from kivy import require
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

require("1.11.1")


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Button(text="Btn 1"))
        my_btn = CustomBtn()
        my_btn.bind(position=self.btn_pressed)
        self.add_widget(my_btn)
        self.add_widget(Button(text="Btn 2"))

    def btn_pressed(self, instance, pos):
        print("pos: Printed from root widget: {pos}".format(pos=pos))


class CustomBtn(Widget):
    position = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.position = touch.pos
            return True
        return super().on_touch_down(touch)

    def on_position(self, instance, pos):
        print("pressed at {pos}".format(pos=pos))


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MyApp().run()
