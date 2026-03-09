#adsr.py

import numpy as np
import sounddevice as sd
from sound import Sound 
from notes import notes


#ADSR class allows the user to create multiple different adsr envelopes to apply to different sounds

class ADSR():
    def __init__(self, attack:float, decay:float, sustain:float, release:float):
        self.adsr = [attack, decay, sustain, release]

    def apply_envelope(
            self, 
            sound: np.array,
            sample_rate: int=44100
            ):

        #calculate number of samples for each of the adsr stages
        attack_samples = int(self.adsr[0]*sample_rate)
        decay_samples = int(self.adsr[1]*sample_rate)
        release_samples = int(self.adsr[3]*sample_rate)

        #sustain is different in the sense that it isn't fixed and depends on how long the user holds the sound for,
        sustain_samples = len(sound) - (attack_samples+decay_samples+release_samples)

        #multiply linearly for the initial attack for the amount of samples required
        sound[:attack_samples] *= np.linspace(0,1,attack_samples)

        #multiply linearly down to the sustain level from the 
        sound[attack_samples:attack_samples+decay_samples] *= np.linspace(1,self.adsr[2],decay_samples)

        #multiply the sustain samples by the sustained amplitude
        sound[attack_samples+decay_samples:attack_samples+decay_samples+sustain_samples] *= self.adsr[2]

        #release
        sound[attack_samples+decay_samples+sustain_samples:] *= np.linspace(self.adsr[2], 0, release_samples)

        return sound

s1 = Sound(3.0,0.7)
sound = s1.sine_wave(notes["C4"])

e1 = ADSR(1.0,0.3,0.7,0.5)
sound = e1.apply_envelope(sound)
sd.play(sound)
sd.wait()
