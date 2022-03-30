import cryptography
import emoji
from secure import PSHs, fencrypt, fdecrypt
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2

        self.password = TextInput(password=False, multiline=False,font_size=128,font_name="seguiemj")
        self.ebutton = Button(text="Encrypt")
        self.dbutton = Button(text="Decrypt")
        self.emptyPop = Popup(title='Error', content=Label(text='Empty Password!'),size=(100, 100), auto_dismiss=True)
        self.alreadyDecPop = Popup(title='Error', content=Label(text='File is Already Decrypted Or the password is incorrect'), size=(100, 100), auto_dismiss=True)

        self.ebutton.bind(on_press=self.eClick)
        self.dbutton.bind(on_press=self.dClick)

        self.add_widget(self.ebutton)
        self.add_widget(self.dbutton)
        self.add_widget(self.password)



    def eClick(self,ebutton):
        if self.password.text == '':
            self.emptyPop.open()
        else:
            fencrypt(PSHs(emoji.demojize(self.password.text)))
            self.password.text = ''
    def dClick(self,ebutton):
        if self.password.text == '':
            self.emptyPop.open()
        else:
            try:
                fdecrypt(PSHs(emoji.demojize(self.password.text)))
            except cryptography.fernet.InvalidToken:
                self.alreadyDecPop.open()
            self.password.text = ''

class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
