import tensorflow as tf
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten, BatchNormalization, Dropout
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.utils import plot_model
from tensorflow.keras.losses import binary_crossentropy
from sklearn.model_selection import cross_val_score
from model import SolNet

def train():
  batch_size = 32
  location = 'dataset/'
  label_mode = 'binary'
  seed = 10 #changed for each fold made manually
  epochs=30
  class_names = ['clean', 'dirty']

  tr_dataset = image_dataset_from_directory(directory=location, label_mode= label_mode, class_names=class_names,
                                            seed=seed, labels='inferred', image_size=in_size[:-1], 
                                            subset = 'training', batch_size=batch_size, validation_split=.2)

  val_dataset = image_dataset_from_directory(directory=location, label_mode= label_mode, class_names=class_names,
                                            seed=seed, labels='inferred', image_size=in_size[:-1],
                                            subset = 'validation', batch_size=batch_size, validation_split=.2)

  in_size = [227, 227, 3]
  SolNet = SolNet(in_size)
  history = SolNet.fit(tr_dataset, validation_data=val_dataset, epochs=epochs, batch_size=batch_size)
  return history

if __name__ == "__main__":
  train()