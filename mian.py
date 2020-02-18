from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        def install_apk(instance):
            current_path = r"C:\Users\Topjoy\Downloads\PingTools.apk"
            #files = os.listdir(current_path)
            file = r"C:\Users\Topjoy\Downloads\PingTools.apk"
            cmd = "adb install -r " + "\"" + file + "\""
            os.system(cmd)
            # for file in files:
            #     if file[len(file) - 3:len(file)] == "apk":
            #         cmd = "adb install -r " + "\"" + file + "\""
            #         os.system(cmd)

        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='V 0.1'))
       
        self.btn = Button(text="Install apk",font_size = 14)
        self.btn.bind(on_release = install_apk)
        self.add_widget(self.btn)

    # def test(instance,value):
    #     print('The button <%s> is being pressed' % instance.text)



class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()

