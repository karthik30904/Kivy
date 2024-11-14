from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Click Me")
        btn.bind(on_press=self.on_button_click)  # Bind the button to the event
        layout.add_widget(btn)
        return layout

    def on_button_click(self, instance):
        print("Button clicked!")

if __name__ == "__main__":
    MyApp().run()
