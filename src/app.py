from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

base64_image = None  # Variable to store the base64 image

@app.route("/")
def index():
    return render_template('index2.html')

@app.route('/upload', methods=['POST'])
def upload():
    global base64_image

    # Get the file from the request
    uploaded_file = request.files['file']

    if uploaded_file:
        # Read the content of the file and encode it in base64
        file_content = uploaded_file.read()
        base64_image = base64.b64encode(file_content).decode('utf-8')

        return jsonify({'image': base64_image})
    else:
        return jsonify({'error': 'No file provided'})

if __name__ == '__main__':
    app.run(debug=True)
