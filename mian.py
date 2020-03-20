from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
#from kivy.base import runTouchApp
import os

class LoginScreen(GridLayout):
    dropdown = DropDown() # 下拉列表类实例化
    apkList = []
    current_path = r"C:\Users\Topjoy\Downloads"#下载文件夹下的路径
    newFileTime = 0 #最新文件的修改时间
   

    def __init__(self, **kwargs):
        self.setApkList(self.current_path,"apk")
        def install_apk(instance):
            cmd = "adb install -r " + "\"" + self.current_path+ "\\" + self.mainbutton.text + "\""
            print(cmd) 
            os.system(cmd)

            #如果当前apk是yk包，则自动打开
            #判断当前名称是否为yk开头，*且复选框为true状态
            #从config中，根据yk，找到包名和活动名
            #cmd命令开启


        def refreshApkList(instance):
            #self.resetApkList()
            print("No Finish")

        ##创建布局
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 2

        ##创建刷新按钮
        self.btn_refresh = Button(text="Refresh ApkList",font_size = 14)
        self.btn_refresh.bind(on_release = refreshApkList)

        ##创建安装按钮
        self.btn = Button(text="Install apk",font_size = 14,width = 100)
        self.btn.bind(on_release = install_apk)

            
        ##创建下拉列表
        for i in range (len(self.apkList)):
            btn = Button(text=str(self.apkList[i]), size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.mainbutton = Button(text=str(self.apkList[0]), size_hint_y=None,width = 280)
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        ##创建状态面板
        self.statePanel = Label(text = "1")


        ##装入布局
        self.add_widget(Label(text='V 0.3'))
        #self.add_widget(self.statePanel)
        self.add_widget(Label()) 
        self.add_widget(self.btn_refresh)
        self.add_widget(Label()) 
        self.add_widget(self.mainbutton)
        self.add_widget(self.btn)

        
    #将path下所有的factor_type文件，设置到下拉列表中
    def setApkList(self,path,factor_type):
        files = os.listdir(path)
        for file in files:
            if file[len(file) - 3:len(file)] == factor_type:
                np = path + "\\" + file  #nowPath
                print(np)
                #apklist判空
                if len(self.apkList) == 0:
                    self.newFileTime = os.stat(np).st_mtime
                    self.apkList.append(file)
                else:
                    #根据时间进行排序，以设定默认（列头）文件
                    if self.newFileTime > os.stat(np).st_mtime:
                        self.apkList.append(file)
                    else: 
                        self.newFileTime = os.stat(np).st_mtime
                        self.apkList.insert(0,file)

    def resetApkList(self):
        print(1)
        # self.apkList = []
        # self.remove_widget(self.mainbutton)
        # self.setApkList()
        # for i in range (len(self.apkList)):
        #     btn = Button(text=str(self.apkList[i]), size_hint_y=None, height=30)
        #     btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
        #     self.dropdown.add_widget(btn)

        # self.mainbutton = Button(text=str(self.apkList[0]), size_hint_y=None,width = 280)
        # self.mainbutton.bind(on_release=self.dropdown.open)
        # self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))
        # self.add_widget(self.mainbutton)
        



class MyApp(App):

    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()

