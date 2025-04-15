import parselmouth as pm 
import csv
import os
import matplotlib.pyplot as plt 
import pandas as pd
from parselmouth.praat import call
import speech_recognition as sr

#take in directory of .wav files samples
#returns dictionary of emotions mapped to pm sound objects
def get_sounds(directory=None):
    if directory is None:
        directory = os.getcwd()
    samples=os.listdir(directory)
    sounds={}
    for wav in samples:
        if wav[-4:]!=".wav":
            continue
        else:
            name=wav.split('.')
            emotion=name[0]
        wav= directory+ "/" +wav
        sounds[emotion]=pm.Sound(wav)  
    return sounds

def get_pitch_min(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        pitch = call(audio, "To Pitch (ac)...", 0.0, 75.0, 15, "off", 0.09, 0.5, 0.055, 0.35, 0.14, 600.0)
        pmin=call(pitch, "Get minimum...", 0.0, 0.0, "Hertz", "Parabolic",)
        df.loc[df['Speech File'].str.lower() == emotion, 'Min Pitch'] = pmin

    #write pmin to csv
    df.to_csv(csv_file_path, index=False)

def get_pitch_max(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        pitch = call(audio, "To Pitch (ac)...", 0.0, 75.0, 15, "off", 0.09, 0.5, 0.055, 0.35, 0.14, 600.0)
        pmax=call(pitch, "Get maximum...", 0.0, 0.0, "Hertz", "Parabolic",)
        df.loc[df['Speech File'].str.lower() == emotion, 'Max Pitch'] = pmax

    #write to csv
    df.to_csv(csv_file_path, index=False)
    
def get_pitch_mean(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        pitch = call(audio, "To Pitch (ac)...", 0.0, 75.0, 15, "off", 0.09, 0.5, 0.055, 0.35, 0.14, 600.0)
        pmean=call(pitch, "Get mean...", 0.0, 0.0, "Hertz")
        df.loc[df['Speech File'].str.lower() == emotion, 'Mean Pitch'] = pmean
    
    #write to csv
    df.to_csv(csv_file_path, index=False)

def get_pitch_sd(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        pitch = call(audio, "To Pitch (ac)...", 0.0, 75.0, 15, "off", 0.09, 0.5, 0.055, 0.35, 0.14, 600.0)
        psd=call(pitch, "Get standard deviation...", 0.0, 0.0, "Hertz")
        df.loc[df['Speech File'].str.lower() == emotion, 'Sd Pitch'] = psd
    
    #write to csv
    df.to_csv(csv_file_path, index=False)

def get_intensity_min(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        intensity = call(audio, "To Intensity...", 100.0, 0.0)
        imin=call(intensity, "Get minimum...", 0, 0, "Parabolic")
        df.loc[df['Speech File'].str.lower() == emotion, 'Min Intensity'] = imin
    
    #write to csv
    df.to_csv(csv_file_path, index=False)

def get_intensity_max(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        intensity = call(audio, "To Intensity...", 100.0, 0.0)
        imax=call(intensity, "Get maximum...", 0, 0, "Parabolic")
        df.loc[df['Speech File'].str.lower() == emotion, 'Max Intensity'] = imax
    
    #write to csv
    df.to_csv(csv_file_path, index=False) 

def get_intensity_mean(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        intensity = call(audio, "To Intensity...", 100.0, 0.0)
        imean=call(intensity, "Get mean...", 0, 0, "Energy")
        df.loc[df['Speech File'].str.lower() == emotion, 'Mean Intensity'] = imean
    
    #write to csv
    df.to_csv(csv_file_path, index=False)

def get_intensity_sd(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        intensity = call(audio, "To Intensity...", 100.0, 0.0)
        isd=call(intensity, "Get standard deviation...", 0.0, 0.0)
        df.loc[df['Speech File'].str.lower() == emotion, 'Sd Intensity'] = isd
    
    #write to csv
    df.to_csv(csv_file_path, index=False)


def get_speaking_rate(csv_file_path, directory=None): 
    #initialize word count flag to see if using my own recordings
    word_count=0
    if directory is None:
        directory = os.getcwd()
        word_count=1
    samples=os.listdir(directory)

    emotion_word_count = {
        "surprised": 16,
        "angry": 13,
        "disgusted": 25,
        "afraid": 31,
        "happy": 19,
        "neutral": 10,
        "sad": 15
    }

    df = pd.read_csv(csv_file_path)
    for wav in samples:
        if wav.endswith(".wav"):  # Only process .wav files
            emotion = wav[:-4]
            wav_path = os.path.join(directory, wav)

            length = pm.Sound(wav_path).xmax
            if word_count > 0:
                number_words=9
            else:
                number_words = emotion_word_count.get(emotion)            
            rate = number_words / length

            df.loc[df['Speech File'].str.lower() == emotion.lower(), 'Speaking Rate'] = rate

    df.to_csv(csv_file_path, index=False)
        

def get_jitter(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        pitch = call(audio, "To Pitch...", 0.0, 75.0, 600.0)
        point_process = call(pitch, "To PointProcess")
        jitter = call(point_process, "Get jitter (local)", 0.0, 0.0, 0.0001, 0.02, 1.3)
        df.loc[df['Speech File'].str.lower() == emotion, 'Jitter'] = jitter
    
    #write to csv
    df.to_csv(csv_file_path, index=False)

def get_shimmer(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        pitch = call(audio, "To Pitch...", 0.0, 75.0, 600.0)
        point_process = call(pitch, "To PointProcess")
        shimmer = call([audio, point_process], "Get shimmer (local)", 0.0, 0.0, 0.0001, 0.02, 1.3, 1.6)
        df.loc[df['Speech File'].str.lower() == emotion, 'Shimmer'] = shimmer
    
    #write to csv
    df.to_csv(csv_file_path, index=False)

def get_HNR(sounds, csv_file_path):
    df = pd.read_csv(csv_file_path)
    for emotion in list(sounds.keys()):
        audio=sounds[emotion]
        hnr = call(audio, "To Harmonicity (cc)...", 0.01, 75, 0.1, 1.0)
        avg_hnr= call(hnr, "Get mean", 0.0, 0.0)
        df.loc[df['Speech File'].str.lower() == emotion, 'HNR'] = avg_hnr
    
    #write to csv
    df.to_csv(csv_file_path, index=False)

def main():
    #get from terminal/user input
    directory=int(input("Enter 0 to work with custom wav files, 1 to work with MSP files: "))
    if directory==1:
        sounds=get_sounds('MSP_samples')
        csv='msp_features.csv'
        get_speaking_rate(csv, "MSP_samples")
        print("MSP")
    else:
        sounds=get_sounds()
        csv= 'my_features.csv'
        get_speaking_rate(csv)
        print("NONE")
    get_pitch_min(sounds, csv)
    get_pitch_max(sounds, csv)
    get_pitch_mean(sounds, csv)
    get_pitch_sd(sounds, csv)

    get_intensity_min(sounds, csv)
    get_intensity_max(sounds, csv)
    get_intensity_mean(sounds, csv)
    get_intensity_sd(sounds, csv)
    
    get_jitter(sounds, csv)
    get_shimmer(sounds, csv)
    get_HNR(sounds, csv)

if __name__=="__main__":
    main()