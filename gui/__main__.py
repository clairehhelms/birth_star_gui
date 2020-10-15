"""Entrypoint of App program.

This program is meant to show a user what their current "birthday star" is
and to describe what a "birthday star" even is. I learned about this concept
when I worked at the planetarium, and I think it's so fun!! 

The user interaction is somewhat limited because I had a tough time just getting
started with this project (understanding MCV was challenging!), but each 
dropdown menu option corresponds to a birthday star, so feel free to try out as
many as you would like! (also buttons are interactive, but straightforward)

If I had more time, I would definitley add descriptions with a fun fact about
each star if I could find them. I wanted to add a google search bar to give users
the ability to search their star, but I don't think tkinter has the capability.

I would also like to expand this to include major world events alongside birthdays
(for example: the light currently seen emanating from Cygnus X was created around when
the pyramids were built on Earth!!). I also wanted to expand my csv file and play with
it using pandas, but I ran out of time.

Although my app is simple, I am proud of what I made, so please enjoy! <3

To run: 'python -m gui' in terminal.
""" 

from gui.App import App
from gui.Window import Window

model = App()
view_controller = Window(model)