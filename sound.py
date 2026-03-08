#sound.py

import numpy as np
import sounddevice as sd
from scipy import signal
import notes

class Sound:
    def __init__(self, duration, amplitude, sample_rate = 44100):
        self.duration:float= duration
        self.amplitude:float= amplitude
        self.sample_rate:int= sample_rate 
        
    def play(self, mysound):
        sd.play(mysound)
        sd.wait()


    def white_noise(self)->np.ndarray:
        #calculate the number of samples needed to be read and outputted for the duration and sample rate
        n_samples = int(self.duration*self.sample_rate)

        #create random numbers between -1 and 1 to represent the amplitude of the wave for the number of samples needed
        noise = np.random.uniform(-1,1, n_samples)

        noise *= self.amplitude
        return noise
    
    def sine_wave(self, frequency:float)->np.ndarray:
        n_samples = int(self.duration*self.sample_rate)

        #linespace function creates an array that acts like a line on a grid
        #create evenly space time points with the number of samples for the duration specific
        time_points = np.linspace(0,self.duration, n_samples,False)

        #convert the frequency into angular frequency in radians per second
        #this is then translated onto each time point on the linespace
        sine = np.sin(2*np.pi*frequency*time_points)

        sine *= self.amplitude
        return sine
    
    def square_wave(self, frequency:float)->np.ndarray:
        n_samples = int(self.duration*self.sample_rate)

        time_points = np.linspace(0,self.duration, n_samples,False)

        #using the sine wave function as a condition to create the square wave
        #return either 1 or -1 based on if the wave is positive or negative
        square = np.where(np.sin(2*np.pi*frequency*time_points)>=0, 1,-1)

        #the code doesn't like me shortening this for some reason
        square = (square * self.amplitude)
        return square

    def sawtooth_wave(self, frequency:float, width:float = 1)->np.ndarray:
        #cutoff changes where the angle of the sawtooth changes.
        #this allows for a different timbre of sawtooth and also allows for a triangle wave.
        
        n_samples = int(self.duration*self.sample_rate)

        time_points = np.linspace(0,self.duration, n_samples,False)

        #scipy's sawtooth function 
        sawtooth = signal.sawtooth(2*np.pi*frequency*time_points, width)

        sawtooth *= sawtooth
        return sawtooth

