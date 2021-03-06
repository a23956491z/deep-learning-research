from keras.datasets import mnist
from keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255
train_labels = to_categorical(train_labels)

test_images = train_images.reshape((60000, 28*28))
test_images = train_images.astype('float32') / 255
test_labels = to_categorical(test_labels)

from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
				loss='categorical_crossentropy',
				metrics=['accuracy'])

network.fit(train_images, train_labels, epochs=5, batch_size=128)
