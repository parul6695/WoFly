import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
import FinalWoFly

class HomePage(Screen):     
    pass
        
class OptionPage(Screen):
    pass

class RegisterPage(Screen):     
    def validateLogIn(self):
        self.username = self.ids.username.text
        self.password = self.ids.password.text
        self.repassword = self.ids.repassword.text
 
        print("username:", self.username, "password:", self.password)
        return self.username != "" and self.password != "" and self.repassword!= "" and self.password == self.repassword

class SignInPage(Screen):     
    def validateLogIn(self):
        self.username = self.ids.username.text
        self.password = self.ids.password.text
        return self.username != "" and self.password != ""

        
        
class ResultsPage(Screen):     
    pass

class ScreenManagement(ScreenManager):
    pass


kv_file = Builder.load_string("""
ScreenManagement:
    HomePage:
    OptionPage:
    RegisterPage:
    SignInPage:
    ResultsPage:
    
<MyTextInput@TextInput>:
    background_color: (1,1,1,1) if self.focus else (0,0,0,0)
    
<HomePage>:
    name : "home"
    BoxLayout:
        Button:
            text: 'Welcome'
            font_size: "60"
            background_normal: ''
            background_color: .1, .3, .4, .95
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'option'
                
<OptionPage>:
    name: 'option'
    GridLayout:
        cols: 1
        Button:
            text: 'Sign In'
            font_size: "60"
            background_normal: ''
            background_color: .1, .6, .9, .95
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'sign in'
        Button:
            text: 'Register'
            font_size: "60"
            background_normal: ''
            background_color: .1, .3, .4, .95
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'register'
    
<SignInPage>:
    name: "sign in"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text:  "Enter username: "
                font_size: "50"
            TextInput:
                id: username
                multiline: False
                
            Label: 
                text: "Enter password: "
                font_size: "50"
            TextInput:
                id: password
                multiline: False
            
        Button:
            text:  "Sign in: "  
            font_size: "70"
            background_normal: ''
            background_color: .1, .3, .2, .95
            on_press:  
                root.manager.transition.direction = 'left'
                root.manager.current = 'results' if root.validateLogIn()==True else 'sign in' 
                
        Button:
            text:  "Back to menu"  
            font_size: "70"
            background_normal: ''
            background_color: .1, .3, .4, .95
            on_press:  
                root.manager.transition.direction = 'right'
                root.manager.current = 'option' 
                
<RegisterPage>:
    name: "register"
    GridLayout:
        cols: 1
        GridLayout:
            cols: 2
            Label:
                text:  "Enter username: "
                font_size: "80"
            TextInput:
                id: username
                multiline: False
                
            Label: 
                text: "Enter password: "
                font_size: "80"
            TextInput:
                id: password
                multiline: False
            Label: 
                text: "Re-enter password: "
                font_size: "80"
            TextInput:
                id: repassword
                multiline: False
            
        Button:
            text:  "Sign up: "  
            font_size: "70"
            background_normal: ''
            background_color: .1, .1, .6, .95
            on_press:  
                root.manager.transition.direction = 'left'
                root.manager.current = 'results' if root.validateLogIn()==True else 'register'
        Button:
            text:  "Back to menu"  
            font_size: "70"
            background_normal: ''
            background_color: .1, .3, .4, .95
            on_press:  
                root.manager.transition.direction = 'right'
                root.manager.current = 'option' 

<ResultsPage>:
    name: "results"
    GridLayout:
        cols: 1
        Label: 
            text: "[ref=https://www.cottagehealth.org/services/womens-health]cottagehealth[/ref]"  
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://www.premiumcaremd.com/services/womens-health]premiumcaremd[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://www.noozhawk.com/article/womens_march_santa_barbara_20200118]noozhawk[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://www.noozhawk.com/article/safety_net_health-care_providers_uninsured_20130918]noozhawk[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://keyt.com/lifestyle/2020/01/18/thousands-show-up-for-santa-barbaras-womens-march/]com/lifestyle/2020/01/18/thousands-show-up-for-santa-barbaras-womens-march[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://lacannabisnews.com/womens-health-and-cannabis-this-santa-barbara-based-female-run-cannabis-cultivator-is-changing-the-game/]com/womens-health-and-cannabis-this-santa-barbara-based-female-run-cannabis-cultivator-is-changing-the-game[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://sbclinics.org]sb clinics[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://www.countyofsb.org/phd/]countyofsb[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://www.sansumclinic.org/]sansumclinic[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://www.frontiersin.org/articles/10.3389/fnhum.2019.00224/full]frontiersin[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://accounts.google.com/ServiceLogin%3Fcontinue%3Dhttps://www.google.com/search%253Fq%253Dsanta%252Bbarbara%252Blatest%252Bwoman%252Bhealth%252Bnews%2526oq%253Dsanta%252Bbarbara%252Blatest%252Bwoman%252Bhealth%252Bnews%2526aqs%253Dchrome.0.69i59.3983j0j7%2526sourceid%253Dchrome%2526ie%253DUTF-8%26hl%3Den]google[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
        Label:
            text: "[ref=https://www.google.com/preferences?hl=en]google[/ref]"
            markup: True
            on_ref_press:
                import webbrowser
                webbrowser.open(args[1])
            
        GridLayout:
            cols: 2
            Button:
                text: "Back to home"
                on_press:  
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'home'
            Button:
                text: "Log out"
                on_press:  
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'home'
        
""")



class myApp(App):
    def build(self):
        return kv_file
 
if __name__ == "__main__":
    myApp().run()
        