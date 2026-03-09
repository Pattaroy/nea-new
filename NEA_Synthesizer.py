#NEA_Synthesizer

from guizero import App, Text, PushButton, Slider
from sound import Sound
from ADSR import ADSR
from notes import notes

piano = {}

app = App(title="Synthesizer", layout="grid")


def current_note(note):
  current_note = note


for note in range (len(notes)):
  
  if "#" in notes[note]:
    piano[f"key{note}"] = PushButton(app, current_note(), note,f"{notes[note]}",grid=[1,1])

app.display

amplitude1 = Slider(app, end = 1, horizontal = False)
amplitude2 = Slider(app, end = 1, horizontal = False)

#duration1
#duration2

#wave1 = Sound
#wave2
