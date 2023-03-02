from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window

# This sets the size of the screen
Window.size = (480, 480)


# This is the main class that contains all the different interfaces.
# Using a widget means you can easily use different layout design and rearrange them on the screen
class MainInterface(Widget):
    # Here are the different variables for storing values to later be viewed and evaluated
    output = ''
    eval_output = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # This function adds the numbers pressed to a variable that is then used to
    # evaluate and show the result
    def Enter_Number(self, name, ID):
        print(self.output)
        self.output += name
        self.output = str(self.output.replace('*', 'x'))
        self.eval_output = self.output
        ID.text = self.output
        print(self.output)

    # This function clears all the data entered so far by setting all variables
    # empty lists and strings
    def clear_all(self, ID, ID2):
        self.output = ''
        ID.text = self.output
        ID2.text = ''

    # Todo, there is a strange syntax error here caused by a invalid decimal literal,
    #  Identifiers cant start with numbers
    def clear_nums(self, ID):
        self.output = eval(str(self.eval_output))
        ID.text = str(self.output)
        print(self.output)

    def calculation(self, ID):
        self.eval_output = eval(self.output)
        ID.text = str(self.eval_output)
        print(self.output)
        

class MyApp(App):
    pass


MyApp().run()
