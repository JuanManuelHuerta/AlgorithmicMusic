import pyaudio
import numpy as np
import random

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 0.60   # in seconds, may be float

def distort(X):
    y=np.array([1.0 if x >= 0.0 else -1.0 for x in X])
    return y

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

correct=0
wrong=0
#mapper={' ':110,'a':440,'s':660,'d':880,'f':1220,'g':1660}
mapper={' ':110,'c':523,'d':587,'e':659,'f':698,'g':784,'a':880,'b':988}
distort_seq=0

while True:
    distort_seq+=1
    z=list(raw_input( "Enter note a s d:"))
    if z==[]:
        z=['a','z']
    samples=None
    for x in z:
        if x in mapper:
            f3=mapper[x]
        else:
            f3=random.random()*880
        if samples is None:
            samples = distort(np.sin(2*np.pi*np.arange(fs*duration)*f3/fs)).astype(np.float32)
        else:
            samples += distort(np.sin(2*np.pi*np.arange(fs*duration)*f3/fs)).astype(np.float32)
    stream.write(volume*samples)

