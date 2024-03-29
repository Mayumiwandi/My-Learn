# -*- coding: utf-8 -*-
"""Time_Series_Denpasar_bali.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttaGG3WPWc7dvD8LjuC1Ab0RRCYIMyXx
"""

from google.colab import files

files.upload()

!pip install -q kaggle

!mkdir ~/.kaggle
!cp kaggle.json ~/.kaggle
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d cornflake15/denpasarbalihistoricalweatherdata

import zipfile
zip_ref = zipfile.ZipFile('/content/denpasarbalihistoricalweatherdata.zip', 'r')
zip_ref.extractall('/content/sets')
zip_ref.close()

import pandas as pd
# /content/sets/openweatherdata-denpasar-1990-2020.csv


df = pd.read_csv('/content/sets/openweatherdata-denpasar-1990-2020v0.1.csv')
df.head(10)

total_data = df.shape

print('Total datasets adalah sebanyak', total_data)

df.isnull().sum()

df_new = df[["dt_iso","temp"]]
df_new

df_new.columns =["data", 'temp']
df_new

df_new["data"] = pd.to_datetime(df_new["data"])
df_new.head()

data_world = df_new[['data','temp']].copy()
data_world['data'] = data_world['data'].dt.date

data_world.set_index('data', inplace= True)

data_world.head(10)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (0, 1))
data_1 = scaler.fit_transform(data_world)

import matplotlib.pyplot as plt
plt.figure(figsize=(20, 5))
plt.plot(data_1)
plt.title('temperature diBali', fontsize=20)
plt.show()

train_size = int(len(data_1) * 0.8)

test_size = len(data_1) - train_size


X_data, y_data = data_1[0:train_size, :], data_1[train_size:len(data_1), :1]

print("Training set size:", train_size)
print("Testing set size:", test_size)

import tensorflow as tf
import numpy as np
def dataset(dataset, time_step=1):
    X, Y = [], []
    for i in range(len(dataset)-time_step-1):
        a = dataset[i:(i+time_step), 0]
        X.append(a)
        Y.append(dataset[i + time_step, 0])
    return np.array(X), np.array(Y)

X_train, y_train = dataset(X_data, 100)
X_test, y_test = dataset(y_data, 100)

X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Bidirectional, Dropout


model = Sequential([
    LSTM(64, return_sequences = True, input_shape=(100, 1)),
    Dropout(0.1),
    LSTM(64, return_sequences = True),
    Dropout(0.1),
    Bidirectional(LSTM(64)),
    Dropout(0.1),
    Dense(8, activation = 'relu'),
    Dense(1)
])

model.summary()

x = (data_1.max() - data_1.min()) * 10/100
print(x)

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('mae')< 0.1 and logs.get('val_mae')< 0.1 ):
      print("\nMAE dari model < 10% skala data")
      self.model.stop_training = True
callbacks = myCallback()

optimizer = tf.keras.optimizers.SGD(learning_rate=1.0000e-04, momentum=0.9)
model.compile(loss=tf.keras.losses.Huber(),
              optimizer=optimizer,
              metrics=["mae"]
)

history = model.fit(
    X_train, y_train,
    validation_data = (X_test, y_test),
    epochs = 10,
    batch_size = 1000,
    callbacks=[callbacks],
    verbose = 1
)

plt.plot(history.history['loss'], label='Training loss')
plt.plot(history.history['val_loss'], label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.plot(history.history['mae'], label='Training loss')
plt.plot(history.history['val_mae'], label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()



