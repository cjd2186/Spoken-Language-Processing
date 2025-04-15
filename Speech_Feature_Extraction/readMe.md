
Program Usage:
Run in terminal 'python get_features.py'
Follow prompt, and check csv files for updated cells.
I do not make the csv from scratch, but rather populate an existing csv file (see template.csv [MSP_features.csv with no value], and renamed the template).
My program takes in user input from the terminal:
    0: find features on the MyFeatures wav files [current working directory]
    1: find features on the MSP Podcast wav files [MSP Samples directory]

The program first creates a dictionary of each emotion mapped to sound objects for each wav file.
This sound dictionary is passed into each function, along with the csv file that is being populated. This allows each function to get the statistics for every emotion for each dataset.
Each emotion in the dictionary is iterated through to go through every file/emotion for the given dataset.
Each function simply uses Parselmouth Praat Calls to get the necessary feature, with parameters according to the HW1 Feature Extraction Notes specifications. 

Pitches: make pitch object, get pitch feature, enter feature into csv.
Intensity: make intensity object, get intensity feature, enter feature into csv.
Jitter: make pitch object, get pointprocess object from pitch, get jitter (local) from Point process, enter feature into csv
Shimmer: make pitch object, get pointprocess object from pitch, get shimmer (local) from Point process and audio, enter feature into csv
HNR: make Harmoncity (cc) object, get mean harmonicity, enter feature into csv

Speaking Rate: my own sentences all were 9 words long. I transcribed the MSP sentences as shown below, and counted the words, accounting for repeated words. These values were then divided by the length of each sound (xmax time) to get the speaker rate. Rates were then entered into the proper csv file for the emotion found.

My Sentence:
•	Emotion.wav:
o	“My name is Christopher and today is my birthday.”
o	9 words
MSP:
•	Surprised.wav:
o	“And Im Im watching people go wait a minute you mean, you mean, Dr. Carson is.”
o	16 words
•	Angry.wav:
o	“This process that I walked this path to her as she came out.”
o	13 words
•	Disgusted.wav:
o	“I mean the more politicians speak, the more I want to turn it off because they’re all a bunch of liars and thieves and crooks.”
o	25 words
•	Afraid.wav:
o	“And I I think about Trump, if he gets power, I mean if he actually gets elected, I fear for this country's future I fear for the future of human Liberty”
o	31 words
•	Happy.wav:
o	“we we have two eyes and two ears and fingernails and I’m like oh my gosh that’s so adorable.”
o	19 words
•	Neutral.wav:
o	“Printing more than two hundred footnotes and thirty classic texts.”
o	10 words
•	Sad.wav:
o	“Our producer Keith had family issues and then things kind of kept on falling apart.”
o	15 words