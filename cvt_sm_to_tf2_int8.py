import tensorflow as tf
import numpy as np

print("Acutally we dont need to do this, mtk converter support saved model folder as input")

# Load the SavedModel
converter = tf.lite.TFLiteConverter.from_saved_model("mobilenet-v3-tf2")

# (Optional) Optimize for size/speed
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# (Optional) Restrict to int8 quantization if you want APU acceleration
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.uint8
converter.inference_output_type = tf.uint8

# ✅ Representative dataset function is REQUIRED for full INT8 quantization
# This should yield sample input tensors with the same shape as model input
def representative_data_gen():
    for _ in range(100):  # 100 samples is usually enough
        # Example: MobileNetV3 expects 224x224x3 images
        dummy_input = np.random.randint(0, 256, size=(1, 224, 224, 3), dtype=np.uint8)
        yield [dummy_input.astype(np.float32)]  # some TF versions want float32 here

converter.representative_dataset = representative_data_gen

# Convert to TFLite
tflite_model = converter.convert()

# Save to file
with open("mobilenet_v3_int8.tflite", "wb") as f:
    f.write(tflite_model)

