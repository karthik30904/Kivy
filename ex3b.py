from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Label to display the value of the slider
        self.label = Label(text="Slider Value: 0")
        layout.add_widget(self.label)

        # Create the slider widget
        slider = Slider(min=0, max=100, value=0)
        slider.bind(value=self.on_value_change)  # Bind the slider's value change event
        layout.add_widget(slider)
        
        return layout

    def on_value_change(self, instance, value):
        # Update the label with the current slider value
        self.label.text = f"Slider Value: {int(value)}"

if __name__ == "__main__":
    MyApp().run()
