from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.label import Label

#from kivy.network.urlrequest import UrlRequest
#import requests

#Builder.load_file('WeScrape.kv')

#sets background colour
Window.clearcolor = (97/255, 60/255, 102/255, 1)

class WeScrapeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical',padding=100,spacing=15)
        self.logo = Label(text='WeScrape',font_size=40)
        self.html = TextInput(text='Enter site url here!',size_hint=(1,0.1),multiline=False)
        submit = Button(background_color = [0, 240, 123, 0.5], text='Submit', pos_hint={'center_x':0.5},size_hint=(None,None), width=150,height=50, on_press=self.submit) 
        #adds widget to screen
        self.layout.add_widget(self.logo)
        self.layout.add_widget(self.html)
        self.layout.add_widget(submit)
        return self.layout   
    
    def submit(self,obj):
        self.output = TextInput(text="test",size_hint=(None,None), width=150,height=50,multiline=False)
        self.layout.add_widget(self.output)


if __name__ == '__main__':
    WeScrapeApp().run()
    
