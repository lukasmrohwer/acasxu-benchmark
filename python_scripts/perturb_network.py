import onnx
import numpy as np

def perturb_network(onnx_path, perturbed_onnx_path, p, seed):
    with open(onnx_path, "rb") as f:
        onnx_model = onnx.load(f)

    np.random.seed(seed)
    
    for i in range(len(onnx_model.graph.initializer)):
        tensor = onnx.numpy_helper.to_array(onnx_model.graph.initializer[i])

        noise = np.random.normal(loc=0.0, scale=p, size=tensor.shape).astype(tensor.dtype)

        perturbed_tensor = tensor + noise

        new_tensor = onnx.numpy_helper.from_array(perturbed_tensor, name=onnx_model.graph.initializer[i].name)
        
        onnx_model.graph.initializer[i].CopyFrom(new_tensor)

    onnx.save(onnx_model, perturbed_onnx_path)