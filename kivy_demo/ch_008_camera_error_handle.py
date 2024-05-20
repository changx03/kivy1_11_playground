from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.logger import Logger
import time


class CameraClick(BoxLayout):
    def __init__(self, **kwargs):
        super(CameraClick, self).__init__(**kwargs)
        self.orientation = "vertical"

        try:
            # Create and add the Camera widget
            # By default, the camera uses `index=0`
            self.camera = Camera(resolution=(640, 480), play=False)
            self.add_widget(self.camera)

            # Create and add the ToggleButton to play/pause the camera
            self.toggle_button = ToggleButton(
                text="Play", size_hint_y=None, height="48dp"
            )
            self.toggle_button.bind(on_press=self.toggle_camera)
            self.add_widget(self.toggle_button)

            # Create and add the Button to capture an image
            self.capture_button = Button(
                text="Capture", size_hint_y=None, height="48dp"
            )
            self.capture_button.bind(on_press=self.capture)
            self.add_widget(self.capture_button)
        except Exception as e:
            # Log the exception and display an error message
            Logger.error(f"CameraClick: Failed to initialize the camera: {e}")
            self.add_widget(Label(text="Camera not available"))

    def toggle_camera(self, instance):
        self.camera.play = not self.camera.play
        self.toggle_button.text = "Play" if not self.camera.play else "Pause"

    def capture(self, *args):
        """
        Function to capture the images and give them the names
        according to their captured time and date.
        """
        if self.camera.play:
            timestr = time.strftime("%Y%m%d_%H%M%S")
            self.camera.export_to_png("IMG_{}.png".format(timestr))
            Logger.info("Captured")


class TestCamera(App):
    def build(self):
        return CameraClick()


if __name__ == "__main__":
    TestCamera().run()
