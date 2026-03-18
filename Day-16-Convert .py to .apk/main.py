from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:

    MDTopAppBar:
        title: "My App"
        pos_hint: {"top": 1}
        elevation: 4

    MDBoxLayout:
        orientation: "vertical"
        spacing: "20dp"
        padding: "20dp"
        pos_hint: {"center_y": .5}

        MDLabel:
            text: "Welcome to My Website 👋"
            halign: "center"
            font_style: "H4"

        MDLabel:
            text: "This is your first beautiful KivyMD app"
            halign: "center"
            theme_text_color: "Secondary"

        MDRaisedButton:
            text: "Click Me 🚀"
            pos_hint: {"center_x": 0.5}
            on_release: app.show_message()

        MDTextField:
            hint_text: "Enter your name"
            pos_hint: {"center_x": 0.5}
            size_hint_x: 0.8
'''

class Main_App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV)

    def show_message(self):
        print("Button Clicked 😎")

if __name__ == '__main__':
    Main_App().run()