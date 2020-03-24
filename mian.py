from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
#from kivy.base import runTouchApp
import os
import pyperclip

class LoginScreen(GridLayout):
    dropdown = DropDown() # 下拉列表类实例化
    dropdown_acc = DropDown()
    apkList = []
    accountList = []
    root_path = os.path.abspath('.') #根目录 
    current_path = r"C:\Users\Topjoy\Downloads"#下载文件夹下的路径
    accountLib_path = root_path+"\AccountLib" #账号仓库目录
    newFileTime = 0 #最新文件的修改时间
    yk_activityName = "com.topjoy.aspida.jp/com.topjoy.aspida.jp.MainActivity"
    yk_packageName = "com.topjoy.aspida.jp"
   

    def __init__(self, **kwargs):
        self.setApkList(self.current_path,self.apkList,"apk")
        self.setApkList(self.accountLib_path,self.accountList,"txt")
        def install_apk(instance):
            #卸载应用
            if self.mainbutton.text[0:2] == "yk":
                print("yk_uninstall")
                cmd = "adb uninstall " + self.yk_packageName
                print(cmd)
                os.system(cmd)

            #安装应用
            cmd = "adb install -r " + "\"" + self.current_path+ "\\" + self.mainbutton.text + "\""
            print(cmd) 
            os.system(cmd)

            #如果当前apk是yk包，则自动打开
            ##判断当前名称是否为yk开头，*且复选框为true状态
            if self.mainbutton.text[0:2] == "yk":
                print ("yk_start")
                #从config中，根据yk，找到包名和活动名
                cmd = "adb shell am start -n " + self.yk_activityName
                os.system(cmd)
            
        
        def tryAdb(instance):
            cmd = "adb devices"
            print(cmd) 
            os.system(cmd)



        def copy_accountJson(instance):
            f = open(self.root_path+"\AccountLib\\"+self.accountButton.text,"r")
            data = f.read()
            pyperclip.copy(data)
            print("Copy done")


        def refreshApkList(instance):
            #self.resetApkList()
            print("No Finish")

        ##创建布局
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 3

        ##创建刷新按钮
        self.btn_refresh = Button(text="Refresh ApkList",font_size = 14)
        self.btn_refresh.bind(on_release = refreshApkList)

        ##创建安装按钮
        self.btn_install = Button(text="Install apk",font_size = 14,width = 100,height = 40)
        self.btn_install.bind(on_release = install_apk)

        ##创建复制账号json按钮
        self.btn_accountCopy = Button(text="AccountJson Copy",font_size = 14,width = 100,height = 40)
        self.btn_accountCopy.bind(on_release = copy_accountJson)

        ##尝试连接ADB
        self.btn_tryAdb = Button(text="TryAdb devices",font_size = 14,width = 100,height = 40)
        self.btn_tryAdb.bind(on_release = tryAdb)

            
        ##创建下拉列表_apk
        for i in range (len(self.apkList)):
            btn = Button(text=str(self.apkList[i]), size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        self.mainbutton = Button(text=str(self.apkList[0]), size_hint_y=None,width = 280)
        self.mainbutton.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.mainbutton, 'text', x))

        ##创建下拉列表_账号仓库
        for i in range (len(self.accountList)):
            btn = Button(text=str(self.accountList[i]), size_hint_y=None, height=30)
            btn.bind(on_release=lambda btn: self.dropdown_acc.select(btn.text))
            self.dropdown_acc.add_widget(btn)

        self.accountButton = Button(text=str(self.accountList[0]), size_hint_y=None,width = 280)
        self.accountButton.bind(on_release=self.dropdown_acc.open)
        self.dropdown_acc.bind(on_select=lambda instance, x: setattr(self.accountButton, 'text', x))



        ##创建状态面板
        self.statePanel = Label(text = "1")


        ##装入布局
        self.add_widget(Label(text='V 0.6'))
        #self.add_widget(self.statePanel)
        self.add_widget(Label()) 
        self.add_widget(self.btn_tryAdb) 
        #self.add_widget(self.btn_refresh) #功能未完成
        self.add_widget(self.accountButton)
        self.add_widget(self.mainbutton)
        self.add_widget(Label()) 
        self.add_widget(self.btn_accountCopy)
        self.add_widget(self.btn_install)      

        
    #将path下所有的factor_type文件，设置到下拉列表中
    def setApkList(self,path,list,factor_type):
        files = os.listdir(path)
        for file in files:
            if file[len(file) - 3:len(file)] == factor_type:
                np = path + "\\" + file  #nowPath
                print(np)
                #apklist判空
                if len(list) == 0:
                    self.newFileTime = os.stat(np).st_mtime
                    list.append(file)
                else:
                    #根据时间进行排序，以设定默认（列头）文件
                    if self.newFileTime > os.stat(np).st_mtime:
                        list.append(file)
                    else: 
                        self.newFileTime = os.stat(np).st_mtime
                        list.insert(0,file)

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

