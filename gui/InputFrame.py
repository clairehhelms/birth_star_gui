"""The first frame shown, establishes the entire root system. Called from Window."""

from tkinter import Label, Tk


STAR = "\U0001F31F"


class InputFrame:
    """Gives the user the intro message! And sets up the root system as Tk()."""
    introduction: Label
    root = Tk()
    root.geometry('610x410')
    greeting: str = ("When you see a star in the sky, the light travelled many years to reach you."
                     "\n Your birthday star is a star whose light is reaching Earth now... "
                     "\n but was created around the time you were born! "
                     "\n Let's meet yours!")

    def __init__(self, root: Tk, introduction: Label):
        """Initializes InputFrame by providing the first label seen."""
        root.title(STAR + "MEET YOUR BDAY STAR" + STAR)
        root.configure(background='black')
        self.introduction = Label(text=self.greeting, bg="black", fg="yellow")
        self.empty_label = Label(bg="black").pack()
        self.introduction.pack()