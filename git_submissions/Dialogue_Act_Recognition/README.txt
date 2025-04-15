Run the files using the Google Colab.
The text features were extracted using Colab.
I had to extract the speech features on my local machine, as it was faster, but I included the exact script and output I used in the Colab as well.

Be sure to change the file paths for the train, valid, and test sets, as the paths are relative to my own drive.

features_csv copy link:
https://drive.google.com/drive/folders/1m8os7t0RJL13IHFvxAxseshLHrQQhI3c?usp=drive_link

Features.ipynb:
------------------------------------------------------------------------------------------------------
Libraries to Download:
tqd, pandas, sklearn, nltk, textblob, transformers, string, torch, matplotlib, os, parselmouth, numpy
------------------------------------------------------------------------------------------------------
Specific Packages:
from tqdm import tqdm
* used for progress bars
import pandas as pd
* used for dataframes

from sklearn.feature_extraction.text import CountVectorizer
* used to get bigram/trigram counts

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
* used to get POS tags

from textblob import TextBlob
* used to get sentiments of transcripts

from transformers import BertTokenizer, BertModel
from string import punctuation
import torch
* used to use BERT encodings (did not end up using in final script)

import matplotlib.pyplot as plt
* used to plot hypothesis

import os
* used to access wav folder 

import parselmouth as pm
from parselmouth.praat import call
* used to call praat functions

import numpy as np
* used to take mean of large vectors (e.g. formant vectors)
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
Classification.ipynb
------------------------------------------------------------------------------------------------------
Libraries to Download:
tensorflow, sklearn, numpy, pandas, tqdm, matplotlib
------------------------------------------------------------------------------------------------------
import tensorflow as tf
from tensorflow.keras import layers, models
* used to build multilayer perceptron neural network model

from sklearn.preprocessing import LabelEncoder, StandardScaler
* used to encode and scale labels/data inputs for model to use in fitting

from sklearn.metrics import f1_score, accuracy_score
* used to get f1 and accuracy scores

import numpy as np
import pandas as pd
* used to utilize dataframes and vector operations

from tqdm import tqdm
* used for progress bars

from tensorflow.keras.optimizers import Adam
* used to compile model and have a learning rate

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report
* used to generate confusion_matrix

import matplotlib.pyplot as plt
* used to plot confusion_matrix