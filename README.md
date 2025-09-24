mtk public docs: https://neuropilot-developer.mediatek.com/resources/public/latest/en/docs/readme

i just kept 8.13.0 files here for testing on evk g1200

# env (mtk converter) #

- mtk converter 8.13.0 requres protobuf==3.20.3
- for dependency issue, tensorflow==2.12.0
- for tensorflow gpu support, tensorflow-gpu==2.12.0

# tf model #

actually we dont need to convert tensorflow saved model to tflite file for mtk converter,
the mtk converter supports saved model folder as input and does itself.

test model: https://www.kaggle.com/models/google/mobilenet-v3/tensorFlow2/large-075-224-classification

labels: https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt
  - from kaggle model card

# env (android native sample) #

mtk samples default using windows environment, compiling with mingw64 for ndk

 
