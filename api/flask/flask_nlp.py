from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Benvenuto nell'applicazione di preprocessing del testo!"

# Rimozione degli spazi
@app.route('/remove_spaces')
def remove_spaces():
    text = request.args.get('text', '')
    processed_text = text.replace(" ", "")
    return jsonify({"original": text, "processed": processed_text})

# Conversione in minuscolo
@app.route('/to_lower')
def to_lower():
    text = request.args.get('text', '')
    processed_text = text.lower()
    return jsonify({"original": text, "processed": processed_text})

# Rimozione della punteggiatura
@app.route('/remove_punctuation')
def remove_punctuation():
    import string
    text = request.args.get('text', '')
    processed_text = text.translate(str.maketrans('', '', string.punctuation))
    return jsonify({"original": text, "processed": processed_text})

@app.route('/full_clean')
def full_clean():
    import string
    text = request.args.get('text', '')
    processed_text = text.replace(" ", "").lower().translate(str.maketrans('', '', string.punctuation))
    return jsonify({"original": text, "processed": processed_text})

if __name__ == "__main__":
    app.run(debug=True)