from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        def test(instance, value):
             print('My button')
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='V 0.1'))
       
        self.btn = Button(text="Install apk",font_size = 14)
        self.btn.bind(state = test)
        self.add_widget(self.btn)

    def test(instance):
        print('The button <%s> is being pressed' % instance.text)



class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()

