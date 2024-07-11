from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form['text']
    target_language = request.form['target_language']

    if not text or not target_language:
        return render_template('index.html', error="Please provide text and target language.")

    try:
        translator = Translator(to_lang=target_language)
        translated_text = translator.translate(text)
        return render_template('index.html', translated_text=translated_text, original_text=text)
    except Exception as e:
        return render_template('index.html', error=f"Translation error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
