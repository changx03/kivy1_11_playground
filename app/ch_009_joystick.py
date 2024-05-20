"""
Cannot trigger `Window.bind` event with xbox controller connected.

"""

import kivy
import pygame
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.11.1")

Builder.load_string("""
<JoystickLogger>
    orientation: 'vertical'
                    
    Label:
        id: lbl_left_joystick
        text: 'PH'
    Label:
        id: lbl_right_joystick
        text: 'PH'
    Label:
        id: lbl_left_trigger
        text: 'PH'
    Label:
        id: lbl_right_trigger
        text: 'PH'
    Label:
        id: lbl_hat
        text: 'PH'
    Label:
        id: lbl_btn
        text: 'PH'
""")


class JoystickLogger(BoxLayout):
    # 0 Left Stick - Horizontal
    # 1 Left Stick - Vertical
    # 2 Left Trigger
    # 3 Right Stick - Horizontal
    # 4 Right Stick - Vertical
    # 5 Right Trigger
    joystick_axis = ListProperty([0, 0, 0, 0, 0, 0])
    button_reg = NumericProperty(defaultvalue=-1)
    dpad_reg = ListProperty([0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        pygame.joystick.init()

        self.joystick = None
        if pygame.joystick.get_count() > 0:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            print(f"Initialized Joystick: {self.joystick.get_name()}")
        else:
            print("No joystick found")

        self.update_lbls()
        Clock.schedule_interval(self.poll_joystick, 1 / 60)

    def poll_joystick(self, dt):
        if not self.joystick:
            return

        need_update = False
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                self.joystick_axis[event.axis] = event.value
                need_update = True
            elif event.type == pygame.JOYHATMOTION:
                self.dpad_reg = list(event.value)
                need_update = True
            elif event.type == pygame.JOYBUTTONDOWN:
                self.button_reg = event.button
                need_update = True
            elif event.type == pygame.JOYBUTTONUP:
                self.button_reg = -1
                need_update = True
        if need_update:
            self.update_lbls()

    def update_lbls(self):
        # update joysticks
        lx, ly, lt, rx, ry, rt = self.joystick_axis
        self.ids.lbl_left_joystick.text = f"Left: {lx:.3f}, {ly:.3f}"
        self.ids.lbl_right_joystick.text = f"Right: {rx:.3f}, {ry:.3f}"
        self.ids.lbl_left_trigger.text = f"Left Trigger: {lt:.2f}"
        self.ids.lbl_right_trigger.text = f"Right Trigger: {rt:.2f}"

        # update d-pad
        dpad_dict = {
            (0, 0): "None",
            (-1, 0): "Left",
            (1, 0): "Right",
            (0, 1): "Up",
            (0, -1): "Down",
        }
        self.ids.lbl_hat.text = f"D-Pad position: {dpad_dict[tuple(self.dpad_reg)]}"

        # update button press
        btn_dict = {
            -1: "None",
            0: "A",
            1: "B",
            2: "X",
            3: "Y",
            4: "LB",
            5: "RB",
            6: "Back",
            7: "Start",
            8: "Xbox",
            9: "L3",
            10: "R3",
            11: "Share",
        }
        self.ids.lbl_btn.text = f"Button: {btn_dict[self.button_reg]}"


class MyApp(App):
    def build(self):
        self.title = 'Xbox Controller Demo'
        return JoystickLogger()


if __name__ == "__main__":
    MyApp().run()
