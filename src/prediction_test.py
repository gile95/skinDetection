from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.models import load_model

# dimensions of our images.
img_width, img_height = 65, 65
model_path = './my_model.h5'
pic_path = 'set path'

model = load_model(model_path)

predict_datagen = ImageDataGenerator(rescale=1./255)

prediction_generator = predict_datagen.flow_from_directory(
            pic_path,
            target_size=(img_width, img_height),
            batch_size=32,
            class_mode=None,
            shuffle=False)

output = model.predict_generator(prediction_generator, 9)
print output

rounded = [round(x) for x in output]
print(rounded)
