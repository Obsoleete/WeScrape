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
import random

#sets background colour
Window.clearcolor = (97/255, 60/255, 102/255, 1)
#creates an array that will hold all input boxes 
inputs=[]

class WeScrapeApp(App):
    def build(self):
        #create 2 screens and a manager to hold the screens
        self.sm = ScreenManager()
        self.screen1 = Screen(name='first')
        self.screen2 = Screen(name='second')

        #links screens to manager
        self.sm.add_widget(self.screen1)
        self.sm.add_widget(self.screen2)

        #creates a layout adding items top to bottom of the page
        self.layout = BoxLayout(
                                orientation='vertical',
                                padding=100,
                                spacing=15)
        #Creates the title of page
        self.logo = Label(
                                text='WeScrape',
                                font_size=40)
        #Creates an input box for user to give a website to scrape
        self.html = TextInput(
                                text='Enter site url here!',
                                size_hint=(0.9,None),
                                height=30,
                                multiline=False)

        inputs.append(self.html)

        #creates another layout inside the previous one to store things horizontally
        self.insideLayout = BoxLayout(orientation='horizontal')

        #creates submit button when user enters link
        self.submitbutton = Button(
                                    background_color = [0, 240, 123, 1], 
                                    color = [0,0,0,1],
                                    text='Extract to JSON File', 
                                    pos_hint={'center_x':0.5},
                                    size_hint=(None,None), 
                                    width=150,
                                    height=50, 
                                    on_press=self.submit) 
        #creates a button that creates more input boxes for users entering more than 1 link                          
        addbutton = Button(
                            background_color = [0, 240, 123, 1], 
                            color = [0,0,0,1], 
                            text='+', 
                            pos_hint={'center_x':0.5},
                            size_hint=(None,None), 
                            width=30,
                            height=30, 
                            on_press=self.addlink) 

        #adds widgets to inner layout
        self.insideLayout.add_widget(self.html)
        self.insideLayout.add_widget(addbutton)

        #adds widgets to outer layout 
        self.layout.add_widget(self.logo)
        #adds inner layout to outer layout 
        self.layout.add_widget(self.insideLayout)
        self.layout.add_widget(self.submitbutton)

        #adds everything to the first screen
        self.screen1.add_widget(self.layout)

        #creates layout for second screen
        box = BoxLayout(
                        orientation='vertical',
                        padding=100,
                        spacing=15)

        #creates a return button when sent to the second screen if users wants to scrape again
        self.returnButton = Button(
                                    background_color = [0, 240, 123, 1],
                                    color = [0,0,0,1], 
                                    text='Return', 
                                    pos_hint={'center_x':0.5},
                                    size_hint=(None,None), 
                                    width=150,
                                    height=50, 
                                    on_press=self.retToHome) 
        #adds return button to second screen
        box.add_widget(self.returnButton)
        #adds layout to screen2
        self.screen2.add_widget(box)

        return self.sm   
    
    #Creates a new input box and adds it to the first screen
    def addlink(self,obj):
        new_html = TextInput(
                            text='Enter another site url here!',
                            size_hint=(0.95,None),
                            height=30,
                            multiline=False)
        inputs.append(new_html)
        #removes and re-adds submit button to fix layout
        self.layout.remove_widget(self.submitbutton)
        self.layout.add_widget(new_html)
        self.layout.add_widget(self.submitbutton)

    #sends user back to first screen and changes the bg colour
    def retToHome(self,obj):
        self.sm.switch_to(self.screen1, direction='right')
        r = random.randrange(1,255)/255
        g = random.randrange(1,255)/255
        b = random.randrange(1,255)/255
        Window.clearcolor = (r,g,b, 1)
        #removes success/failure message
        self.screen2.remove_widget(self.screen2.children[-2])


    # Gets html content and extracts the needed information which is stored in a JSON file and switches to second screen
    def submit(self,obj):
        urls = []
        self.sm.switch_to(self.screen2, direction='left')
        #loops through all the input boxes to store the urls in a list
        for widget in inputs:
            urls.append(widget.text)
        try:
            content = get_content(urls)
            json_array = convert_to_json(content)
            export_to_json(json_array)
            self.screen2.add_widget(Label(text='JSON data downloaded successfully :)',font_size=40))
        except:
            self.screen2.add_widget(Label(text='Sorry something went wrong. :(',font_size=40))



if __name__ == '__main__':
    WeScrapeApp().run()
    
