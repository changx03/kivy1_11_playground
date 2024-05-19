from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string("""
<CustomLayout>
    canvas.before:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

<RootWidget>
    CustomLayout:
        AsyncImage:
            source: 'https://i.redd.it/w39i1e7xka1d1.jpeg'
            size_hint: 1, .5
            pos_hint: {'center_x':.5, 'center_y': .5}
    AsyncImage:
        source: 'https://i.redd.it/aqzzbz0qa91d1.jpeg'
        size_hint: 1, .5
        pos_hint: {'center_x':.5, 'center_y': .5}
    CustomLayout
        AsyncImage:
            source: 'https://i.redd.it/vd8139zkc91d1.jpeg'
            size_hint: 1, .5
            pos_hint: {'center_x':.5, 'center_y': .5}
""")


class RootWidget(BoxLayout):
    pass


class CustomLayout(FloatLayout):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
