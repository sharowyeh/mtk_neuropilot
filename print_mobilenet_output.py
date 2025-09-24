import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="mobilenet_v3_int8.tflite")
interpreter.allocate_tensors()
output_details = interpreter.get_output_details()
print(output_details)

