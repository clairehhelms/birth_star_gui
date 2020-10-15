"""The app portion. This is the model and it's main job is to read the csv and return bday star.

I created a csv file from the data from this link:
http://www.atlasoftheuniverse.com/50lys.html.
"""

from tkinter import Label, Button
import csv
from .InputFrame import InputFrame
from typing import Optional

STAR = "\U0001F31F"


class App:
    """Model of mcv, does the big comparison and reads a csv."""

    def match_input(self, user_age: int) -> Optional[str]:
        """Takes collected data from OptionMenu, compares to starss.csv, and returns the end labels/button!"""
        with open('gui/starss.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                if int(line[0]) == user_age:
                    return_str = (f"Your birthday star is {line[1]},{line[2]}!")
                    return_label = Label(text=return_str, bg="black", fg="yellow", font="Helvetica 18")
                    blank_label = Label(bg="black")
                    blank_label.pack()
                    return_label.pack()
                    end_label = Label(text="Thanks for playing!", bg="black", fg="yellow")
                    blank_label = Label(bg="black")
                    blank_label.pack()
                    end_label.pack()
                    Button(text="END", fg="red", command=InputFrame.root.destroy).pack()
                    star_label = Label(text=STAR)
                    star_label.pack()
        csv_file.close