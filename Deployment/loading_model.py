
# Saving Model
from tensorflow.keras.models import load_model
model.save('Model.h5')
savedModel=load_model('Model.h5')



#Saving Model Weights
model.save_weights('ModelWeights.h5')
print('Model Saved!')
# load model
savedModel = model.load_weights('ModelWeights.h5')
print('Model Loaded!')
