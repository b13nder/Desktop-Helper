from flask import Flask, request, jsonify
from PIL import Image
import pytesseract
import json
import openai

app = Flask(__name__)
openai.api_key = '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'

@app.route('/api/v1/ocr', methods=['POST'])
def ocr_api():
    if 'img' not in request.files:
        return jsonify({'error': 'No image in request.files'}), 400
    try:
        img = Image.open(request.files['img'])
        text = pytesseract.image_to_string(img)
        filtered_text = filter_browser_content(text)
        response = chat_gpt_api(filtered_text)
        return jsonify({'response': response}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

def filter_browser_content(text):
    filtered_text = text.strip().replace('\n', ' ')
    return filtered_text

def chat_gpt_api(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
