# Better Gradio Model3D Component

https://github.com/user-attachments/assets/d8b33ce6-6980-4960-b00b-cf750375b0ac

This is a better version of the [Gradio](https://www.gradio.app/) Model3D component that only utilize the Gradio HTML Component and [Online 3D Viewer](https://3dviewer.net/).
It first starts a http server to render the 3D model within a HTMLfile. Then, the HTML(viewer) is displayed in a Gradio HTML component to achieve a better rendering experience.

Compared to the original Gradio Model3D component, our version has the following improvements:

- Free camera roation and zooming
- No Lighting effects
- More formats supported

## Usage
Doneload this project and install gradio.
Then, you only need to 
```
python demp.py
```
to start a demo with our improved Gradio Model3D component.
It can be easily modified to support your own 3D application.

You can modify the `viewer.html` to get different rendering effects, such as changing the background color and default model.
