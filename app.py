import gradio as gr
import os
import torch
import torchvision

print("Starting...", flush=True)

model = torchvision.models.efficientnet_b2(weights=None)

print("EfficientNet created...", flush=True)

model = model.to("cpu")

print("Model moved to CPU...", flush=True)

demo = gr.Interface(
    fn=lambda x: "Model loaded successfully!",
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(),
)

print("Starting Gradio...", flush=True)

demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 10000))
)
