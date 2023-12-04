import os
from flask import  Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Write load_form function below to Open and redirect to default upload webpage
@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_video():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join('static/', filename))
    return render_template('upload.html')

@app.route('/display/<filename>')
def display_video(filename):
    return redirect(url_for('static', filename=filename))
def upload_video():
    source = cv2.VideoCapture('static/' + filename)
    frame_width = int(source.get(3))
    size = (frame_width, frame_height)

    result = cv2.VideoWriter('static/'+'blackandwhite.mp4'
    cv2.VideoWriter_forucc(*'mp4v'),
    30, size, 0)

    try:
        while True:
            status, frame_image = source.read()
            gray = cv2.cvtColor(frame_image, cv2.COLOR_BGR2GRAY)
                result.white(gray)
                video_file = 'blackandwhite.mp4'
gray = write()





@app.route('/download')
def download_file():
    converted_video_path = "static/blackandwhite.mp4"
    return send_file(converted_video_path, as_attatchment=True)
if __name__ == "__main__":
    app.run()