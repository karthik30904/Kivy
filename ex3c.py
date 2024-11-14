from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label

class MyToggleApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Create a label to show the state of the toggle button
        self.label = Label(text="Button is in Normal state")

        # Create the ToggleButton
        toggle_button = ToggleButton(text="Toggle Me", size_hint=(.5, .5))

        # Bind the state change event to a function
        toggle_button.bind(state=self.on_state_change)

        # Add the label and button to the layout
        layout.add_widget(self.label)
        layout.add_widget(toggle_button)

        return layout

    # Function to handle the state change event
    def on_state_change(self, instance, value):
        if value == 'down':
            self.label.text = "Button is Pressed"
        else:
            self.label.text = "Button is in Normal state"

if __name__ == "__main__":
    MyToggleApp().run()
