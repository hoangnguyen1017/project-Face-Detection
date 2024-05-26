import numpy as np
import os
from PIL import Image as PILImage
from keras import utils
from keras import layers, models
def training_data ():
    Train_data = 'dataset'
    Xtrain = []
    ytrain = []

    for whatever in os.listdir(Train_data):
        whatever_path = os.path.join(Train_data, whatever)
        for filename in os.listdir(whatever_path):
            filename_path = os.path.join(whatever_path, filename)
            label = filename_path.split(os.sep)[1].split('_')[0]
            img = PILImage.open(filename_path).convert('RGB')
            
            Xtrain.append(img)
            ytrain.append(label)

    Xtrain = np.array(Xtrain)
    ytrain = np.array(ytrain)

    ytrain = utils.to_categorical(ytrain)

    num_classes = ytrain.shape[1]
    model_training_first = models.Sequential([
        layers.Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.15),

        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.2),

        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.2),

        layers.Flatten(),
        layers.Dense(1000, activation='relu'),
        layers.Dense(256, activation='relu'),
        layers.Dense(num_classes, activation='softmax'),
    ])

    model_training_first.compile(optimizer='adam',
                                loss='categorical_crossentropy',
                                metrics=['accuracy'])

    model_training_first.fit(Xtrain, ytrain, epochs=10)

    model_training_first.save('model_face_10epochs.keras')

    model_loaded = models.load_model('model_face_10epochs.keras')

#training_data()