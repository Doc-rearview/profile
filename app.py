from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Your HTML with the button

@app.route('/download-cv')
def download_cv():
    return send_from_directory('static', 'pdf/cv.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
