import subprocess
import time
import os
import signal

HTTP_PORT = 7868

process = subprocess.Popen(f"python -m http.server {HTTP_PORT}", shell=True, preexec_fn=os.setsid)


def get_html(model_path=None, port=HTTP_PORT):
    if model_path is None:
        q = ''
    else:
        q = f'?model={model_path}'
    html = '''
<head>
<style>
    .iframe-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50vh; /* 使容器占满整个视口的高度 */
        background-color: #f2f2f2;
    }
    iframe {
        width: 100%;
        height: 100%;
        border: none; /* 去掉边框 */
    }
</style>
</head>
<div class="iframe-container">
<iframe src="'''+ f'http://localhost:{port}/viewer.html{q}' + '''" width="100%" height="100%" frameborder="0" scrolling="no"></iframe>
</div>
'''
    return html

def show_model(model_path):
    return get_html(os.path.join('assets', model_path))

import gradio as gr 
with gr.Blocks() as demo:
    gr.Markdown('# Demo of Better Gradio Model3D')
    gr_html = gr.HTML(get_html())
    gr_radio = gr.Radio(['armadillo.obj', 'armadillo.glb', 'bunny.obj', 'bunny.ply', 'bunny.stl'], label='Model')
    gr_radio.select(show_model, inputs=[gr_radio], outputs=[gr_html])

demo.launch()

os.killpg(os.getpgid(process.pid), signal.SIGINT)
print("HTTP Server Stopped")
print("!!You might need PRESS CTRL-C to stop the demo!!")