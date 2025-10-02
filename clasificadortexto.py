
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS  
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Descargas necesarias
nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir solicitudes externas

# Ruta principal (evita error 404)
@app.route("/", methods=["GET"])
def home():
    return "<h1>API de Clasificación de Texto</h1><p>Usa /predict para obtener una categoría.</p>"

# Ruta para evitar error 405 si alguien hace POST en "/"
@app.route("/", methods=["POST"])
def root_post():
    return jsonify({"message": "Usa /predict para clasificar un texto"}), 400

# Carga el modelo y vectorizador al inicio
model = joblib.load('modelo.pkl')
vectorizer = joblib.load('vectorizador.pkl')

# Preprocesamiento
stemmer = SnowballStemmer('spanish')
stop_words = set(stopwords.words('spanish'))

def tokenize_stemmer(text):
    tokens = word_tokenize(text.lower())
    stems = [stemmer.stem(token) for token in tokens if token.isalpha() and token not in stop_words]
    return ' '.join(stems)

# Ruta para clasificación de texto
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or "text" not in data:  
        return jsonify({"error": "No se proporcionó texto"}), 400

    text = data.get("text", "")
    processed_text = tokenize_stemmer(text)
    transformed = vectorizer.transform([processed_text])
    prediction = model.predict(transformed)[0]

    return jsonify({"category": prediction})

# Ejecución del servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
