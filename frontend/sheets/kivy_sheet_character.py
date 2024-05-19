from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class CharacterSheet(GridLayout):
    def __init__(self, **kwargs):
        super(CharacterSheet, self).__init__(**kwargs)
        self.cols = 2
        self.padding = 10
        self.spacing = 10

        # Character Section
        self.add_widget(Label(text='Name:'))
        self.name_input = TextInput(multiline=False)
        self.add_widget(self.name_input)

        self.add_widget(Label(text='Race:'))
        self.race_input = TextInput(multiline=False)
        self.add_widget(self.race_input)

        self.add_widget(Label(text='Current Career:'))
        self.current_career_input = TextInput(multiline=False)
        self.add_widget(self.current_career_input)

        self.add_widget(Label(text='Previous Careers:'))
        self.previous_careers_input = TextInput(multiline=False)
        self.add_widget(self.previous_careers_input)

        # Personal Details Section
        self.add_widget(Label(text='Age:'))
        self.age_input = TextInput(multiline=False)
        self.add_widget(self.age_input)

        self.add_widget(Label(text='Gender:'))
        self.gender_input = TextInput(multiline=False)
        self.add_widget(self.gender_input)

        self.add_widget(Label(text='Height:'))
        self.height_input = TextInput(multiline=False)
        self.add_widget(self.height_input)

        self.add_widget(Label(text='Weight:'))
        self.weight_input = TextInput(multiline=False)
        self.add_widget(self.weight_input)

        self.add_widget(Label(text='Eyes Color:'))
        self.eyes_color_input = TextInput(multiline=False)
        self.add_widget(self.eyes_color_input)

        self.add_widget(Label(text='Hair Color:'))
        self.hair_color_input = TextInput(multiline=False)
        self.add_widget(self.hair_color_input)

        self.add_widget(Label(text='Star Sign:'))
        self.star_sign_input = TextInput(multiline=False)
        self.add_widget(self.star_sign_input)

        self.add_widget(Label(text='Number of Siblings:'))
        self.siblings_input = TextInput(multiline=False)
        self.add_widget(self.siblings_input)

        self.add_widget(Label(text='Birthplace:'))
        self.birthplace_input = TextInput(multiline=False)
        self.add_widget(self.birthplace_input)

        self.add_widget(Label(text='Distinguishing Marks:'))
        self.marks_input = TextInput(multiline=False)
        self.add_widget(self.marks_input)

        # Character Profile Section
        profile_layout = GridLayout(cols=8, spacing=10, size_hint_y=None)
        profile_layout.bind(minimum_height=profile_layout.setter('height'))

        stats = ['WS', 'BS', 'S', 'T', 'Ag', 'Int', 'WP', 'Fel']
        profile_layout.add_widget(Label(text="Character Profile", size_hint_y=None, height=40))
        for stat in stats:
            profile_layout.add_widget(Label(text=stat, size_hint_y=None, height=40))

        for i in range(3):  # Assuming 3 rows for Starting, Advance, Current
            for j in range(8):  # 8 stats columns
                profile_layout.add_widget(TextInput(multiline=False, size_hint_y=None, height=40))

        self.add_widget(profile_layout)

class CharacterSheetApp(App):
    def build(self):
        return CharacterSheet()

if __name__ == '__main__':
    CharacterSheetApp().run()
