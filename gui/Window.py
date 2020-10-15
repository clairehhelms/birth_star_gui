"""The view and the controller, Window executes the main functionality of the program."""


from .InputFrame import InputFrame
from tkinter import Label, Button, IntVar, OptionMenu
from gui.App import App
from typing import List
from datetime import date


class Window:
    """The largest portion of the program. Responsible for majority of view and controller."""
    model: App
    input_frame: InputFrame
    greet: Label
    year_options: List[int] = list(range(1970, 2020))
    drop: OptionMenu

    def __init__(self, model: App):
        """Initializes Window! and begins the app with the mainloop."""
        self.model = model
        self.greet = Label()
        InputFrame(InputFrame.root, self.greet)
        GoButton = Button(text="Let's go!", fg="blue", font="Helvetica 14 bold", command=self.clicked_go)
        GoButton.place(x=270, y=120)

        InputFrame.root.mainloop()

    def clicked_go(self) -> None:
        """Contains the prompts for the user and collects data from the button/drop click."""
        self.age_label = Label(text="In what year were you born?").pack()
        parent = self.age_label
        self.clicked = IntVar()
        self.clicked.set(self.year_options[0])
        self.drop = OptionMenu(parent, self.clicked, *self.year_options).pack()
        AgeButton = Button(text="Show me my birthday star!", font="Helvetica 14 bold", fg="blue", command=self.Age)
        AgeButton.pack()

    def Age(self) -> int:
        """Calculates age by comparing to today's year, then calls to the matcher."""
        today = date.today()
        current_year = today.strftime("20" + "%y")
        age: int = int(current_year) - int(self.clicked.get())
        matched = App.match_input(age, age)
        AgeLabel = Label(text=matched, bg="black", fg="yellow")
        AgeLabel.pack()
        return age