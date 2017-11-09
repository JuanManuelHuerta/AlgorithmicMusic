import pyaudio
import numpy as np
import random
p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float
f2 = 445.0        # sine frequency, Hz, may be float


stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
#stream.write(volume*samples)

correct=0
wrong=0
for i in range(10):
    print "try number:", i+0
    print "correct:", correct
    print "wrong:", wrong
    x=random.random()
    print x
    if  x>0.5:
        f3=f2
    else:
        f3=f

    samples2 = (np.sin(2*np.pi*np.arange(fs*duration)*f3/fs)).astype(np.float32)

    stream.write(volume*samples)
    stream.write(volume*samples2)

    z=raw_input( "Same? [y/n]:")

# play. May repeat with different volume values (if done interactively) 

    if ('y' in z and x<=0.5) or ('n' in z and x > 0.5):
        correct+=1
        print "right!"
    else:
        wrong+=1
        print "wrong!"

        


    



stream.stop_stream()


stream.close()

p.terminate()

print "Your score.  Correct:", correct, "wrong", wrong
