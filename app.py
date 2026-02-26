import gradio as gr
import time

# Simulated pipeline functions
def fetch_code():
    time.sleep(1)
    return "✅ Source code fetched from repository"

def build_project():
    time.sleep(1)
    return "🔧 Build completed successfully"

def run_tests():
    time.sleep(1)
    return "🧪 All tests passed"

def deploy_app():
    time.sleep(1)
    return "🚀 Application deployed to server"


with gr.Blocks(title="CI/CD Pipeline Demo") as demo:
    gr.Markdown("# CI/CD Pipeline Demonstration")

    with gr.Tabs():
        
        with gr.Tab("Source"):
            btn1 = gr.Button("Fetch Code")
            out1 = gr.Textbox(label="Status")
            btn1.click(fetch_code, outputs=out1)

        with gr.Tab("Build"):
            btn2 = gr.Button("Build Project")
            out2 = gr.Textbox(label="Status")
            btn2.click(build_project, outputs=out2)

        with gr.Tab("Test"):
            btn3 = gr.Button("Run Tests")
            out3 = gr.Textbox(label="Status")
            btn3.click(run_tests, outputs=out3)

        with gr.Tab("Deploy"):
            btn4 = gr.Button("Deploy Application")
            out4 = gr.Textbox(label="Status")
            btn4.click(deploy_app, outputs=out4)

demo.launch()