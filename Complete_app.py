from flask import Flask, request, render_template
import os
import hashlib
import requests
import re

UPLOAD_FOLDER = '/var/www/html/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Compute SHA256 hash of the saved file
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)

    file_hash = sha256_hash.hexdigest()

    # Identify flagged malware
    url = "https://www.virustotal.com/api/v3/files/"
    complete_url = url + str(file_hash)
    headers = {
    "accept": "application/json",
    "x-apikey": "a076c992eeae14dc25c91425d01619338f7a7381c6421383036269407428"
    }
    response = requests.get(complete_url, headers=headers)
    output = response.text
    match = re.search(r'"malicious":\s*(\d+)', output)
    number = str(match.group(1))
    return f"This file was flagged by {number} security vendors"
