from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from actions import get_content, convert_to_json, export_to_json

#sets background colour
Window.clearcolor = (97/255, 60/255, 102/255, 1)
inputs=[]
class WeScrapeApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.screen1 = Screen(name='first')
        self.screen2 = Screen(name='second')
        self.sm.add_widget(self.screen1)
        self.sm.add_widget(self.screen2)
        self.layout = BoxLayout(orientation='vertical',padding=100,spacing=15)
        self.logo = Label(text='WeScrape',font_size=40)
        self.html = TextInput(text='Enter site url here!',size_hint=(0.9,None),height=30,multiline=False)
        inputs.append(self.html)
        self.insideLayout = BoxLayout(orientation='horizontal')
        self.submitbutton = Button(background_color = [0, 240, 123, 0.5], text='Extract to JSON File', pos_hint={'center_x':0.5},size_hint=(None,None), width=150,height=50, on_press=self.submit) 
        addbutton = Button(background_color = [0, 240, 123, 1], text='+', pos_hint={'center_x':0.5},size_hint=(None,None), width=30,height=30, on_press=self.addlink) 
        #adds widget to screen
        self.layout.add_widget(self.logo)
        self.insideLayout.add_widget(self.html)
        self.insideLayout.add_widget(addbutton)
        self.layout.add_widget(self.insideLayout)
        self.layout.add_widget(self.submitbutton)
        self.screen1.add_widget(self.layout)
        self.returnButton = Button(background_color = [0, 240, 123, 0.5], text='Return', pos_hint={'center_x':0.5},size_hint=(None,None), width=150,height=50, on_press=self.retToHome) 
        box = BoxLayout(orientation='vertical',padding=100,spacing=15)
        box.add_widget(self.returnButton)
        self.screen2.add_widget(box)
        return self.sm   
    
    # Gets html content and extracts the needed information which is stored in a JSON file
    def addlink(self,obj):
        new_html = TextInput(text='Enter another site url here!',size_hint=(0.95,None),height=30,multiline=False)
        inputs.append(new_html)
        self.layout.remove_widget(self.submitbutton)
        self.layout.add_widget(new_html)
        self.layout.add_widget(self.submitbutton)

    def retToHome(self,obj):
        self.sm.switch_to(self.screen1, direction='right')

    def submit(self,obj):
        urls = []
        for widget in inputs:
            urls.append(widget.text)
        self.sm.switch_to(self.screen2, direction='left')
        content = get_content(urls)
        json_array = convert_to_json(content)
        export_to_json(json_array)


if __name__ == '__main__':
    WeScrapeApp().run()
    
