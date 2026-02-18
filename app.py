from flask import Flask, request, jsonify
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    file = request.files["image"]
    img = Image.open(file.stream)
    text = pytesseract.image_to_string(img)
    return jsonify({"text": text})

@app.route("/")
def home():
    return "OCR Server Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
