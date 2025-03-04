import onnxruntime as ort

def infer(input_data):
    session = ort.InferenceSession("ai_model.onnx")
    inputs = {session.get_inputs()[0].name: input_data}
    outputs = session.run(None, inputs)
    return outputs

# Example inference
print(infer([[0.5, 0.2, 0.1]]))

