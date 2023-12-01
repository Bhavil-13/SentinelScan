import gradio as gr
from PIL import Image

# Define your visual recognition model function
def recognize_image(image):
    # Assuming you have a model.predict function
    predictions = model.predict(image)
    return predictions

# Create the Gradio interface
iface = gr.Interface(
    fn=recognize_image,
    inputs=gr.Image(),  # Gradio automatically handles image uploads
    outputs=gr.Textbox(),  # Display predictions in a textbox
    live=True,
)

# Launch the interface
iface.launch(share=True)
