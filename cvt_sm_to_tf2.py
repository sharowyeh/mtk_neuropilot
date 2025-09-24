import tensorflow as tf

print("Acutally we dont need to do this, mtk converter support saved model folder as input")

# Load the SavedModel
converter = tf.lite.TFLiteConverter.from_saved_model("mobilenet-v3-tf2")

# (Optional) Optimize for size/speed
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# (Optional) Restrict to int8 quantization if you want APU acceleration
# converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
# converter.inference_input_type = tf.uint8
# converter.inference_output_type = tf.uint8

# Convert to TFLite
tflite_model = converter.convert()

# Save to file
with open("mobilenet_v3.tflite", "wb") as f:
    f.write(tflite_model)

