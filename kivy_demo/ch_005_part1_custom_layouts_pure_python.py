from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage


class RootWidget(BoxLayout):
    pass


class CustomLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(0, 1, 0, 1)  # green
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


class MainApp(App):
    def build(self):
        root = RootWidget()
        custom_layout = CustomLayout()
        source = "https://i.redd.it/w39i1e7xka1d1.jpeg"
        custom_layout.add_widget(
            AsyncImage(
                source=source,
                size_hint=(1, 0.5),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        root.add_widget(custom_layout)

        source = "https://i.redd.it/aqzzbz0qa91d1.jpeg"
        root.add_widget(
            AsyncImage(
                source=source,
                size_hint=(1, 0.5),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )

        custom_layout = CustomLayout()
        source = "https://i.redd.it/vd8139zkc91d1.jpeg"
        custom_layout.add_widget(
            AsyncImage(
                source=source,
                size_hint=(1, 0.5),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        root.add_widget(custom_layout)

        return root


if __name__ == "__main__":
    MainApp().run()
