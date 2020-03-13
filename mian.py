from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
import os

class LoginScreen(GridLayout):
    dropdown = DropDown()
    apkList = []
    current_path = r"C:\Users\Topjoy\Downloads"
    files = os.listdir(current_path)
    #file = r"C:\Users\Topjoy\Downloads\PingTools.apk"
    
    newFileTime = 0
    for file in files:
        if file[len(file) - 3:len(file)] == "apk":
            np = current_path + "\\" + file 
            print(str(np))
            
            print(os.stat(np).st_mtime)

            #apklist判空
            if len(apkList) == 0:
                newFileTime = os.stat(np).st_mtime
                apkList.append(file)
            else:
                if newFileTime > os.stat(np).st_mtime:
                    apkList.append(file)
                else: 
                    newFileTime = os.stat(np).st_mtime
                    apkList.insert(0,file)
            #cmd = "adb install -r " + "\"" + current_path+ "\\" + file + "\""
            #print(cmd) 
            #os.system(cmd)



    def __init__(self, **kwargs):
        def install_apk(instance):
            print(self.mainbutton.text)
            # current_path = r"C:\Users\Topjoy\Downloads"
            # files = os.listdir(current_path)
            # #file = r"C:\Users\Topjoy\Downloads\PingTools.apk"
            # for file in files:
            #     if file[len(file) - 3:len(file)] == "apk":
            #         self.apkList.append(file)

            
            # cmd = "adb install -r " + "\"" + self.current_path+ "\\" + self.mainbutton.text + "\""
            # print(cmd) 
            # os.system(cmd)


        def playAgain(instance):
            pass

        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Label(text='V 0.2'))

        for i in range (len(self.apkList)):
            btn = Button(text=str(self.apkList[i]), size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.mainbutton = Button(text=str(self.apkList[0]), size_hint=(None, None),width = 280)
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))


        self.btn = Button(text="Install apk",font_size = 14)
        self.btn.bind(on_release = install_apk)
        self.add_widget(self.mainbutton)
        self.add_widget(self.btn)
        

    # def test(instance,value):
    #     print('The button <%s> is being pressed' % instance.text)



class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()

