#NEA_Synthesizer

from guizero import App, Text, PushButton, Slider
from sound import Sound
from ADSR import ADSR
from notes import notes

piano = {}

app = App(title="Synthesizer")

def current_note(note):
  current_note = note


for note in range 1, notes:
  if "#" in notes[note]:
    piano[f"key{note}"] = PushButton(app, 
    

amplitude1 = slider(app, end = 1, horizontal = false)
amplitude2 = slider(app, end = 1, horizontal = false)

duration1
duration2

wave1 = Sound
wave2
