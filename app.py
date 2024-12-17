from flask import Flask, render_template, request, jsonify, send_from_directory
import speech_recognition as sr
import os
import wave
from pydub import AudioSegment
from audio_processor import procesar_audio

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/transcripcion', methods=['POST'])
def transcripcion():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file:
        input_file = os.path.join('uploads', file.filename)
        file.save(input_file)
        output_file = os.path.splitext(input_file)[0] + ".wav"
        convertir_audio(input_file, output_file)
        verificar_audio(output_file)
        segmentos = dividir_audio(output_file)
        transcripcion_completa = ""
        for segmento in segmentos:
            texto = transcribir_segmento(segmento)
            transcripcion_completa += texto + "\n"
        archivo_transcripcion = guardar_transcripcion(output_file, transcripcion_completa)
        return jsonify({'message': 'Archivo subido y transcrito exitosamente.', 'transcription_path': archivo_transcripcion})

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(app.root_path, 'uploads')
    return send_from_directory(directory=uploads, path=filename)

@app.route('/descargar_audio', methods=['POST'])
def descargar_audio():
    consulta = request.json
    ruta_salida_webm = procesar_audio(consulta)
    return jsonify({"message": "Archivo descargado exitosamente", "ruta": ruta_salida_webm})

@app.route('/listar_txt', methods=['GET'])
def listar_txt():
    try:
        uploads = os.path.join(app.root_path, 'uploads')  # Corregido aquí
        archivos_txt = [f for f in os.listdir(uploads) if f.endswith('.txt')]
        return jsonify({'archivos_txt': archivos_txt})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def convertir_audio(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")

def verificar_audio(archivo_audio):
    try:
        with wave.open(archivo_audio, 'rb') as audio:
            canales = audio.getnchannels()
            frecuencia = audio.getframerate()
            duracion = audio.getnframes() / frecuencia
            if canales != 1 or frecuencia != 16000:
                print("Advertencia: El archivo de audio no está en el formato recomendado (mono, 16000 Hz).")
    except wave.Error as e:
        print(f"Error al abrir el archivo de audio: {e}")

def transcribir_segmento(audio_segmento):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_segmento) as source:
        audio = recognizer.record(source)
    try:
        texto = recognizer.recognize_google(audio, language='es-ES')
        return texto
    except sr.UnknownValueError:
        return "No se pudo entender el audio"
    except sr.RequestError as e:
        return f"Error en la solicitud: {e}"

def dividir_audio(archivo_audio, duracion_segmento=60):
    audio = AudioSegment.from_wav(archivo_audio)
    segmentos = []
    for i in range(0, len(audio), duracion_segmento * 1000):
        segmento = audio[i:i + duracion_segmento * 1000]
        archivo_segmento = f"{os.path.splitext(archivo_audio)[0]}_segmento_{i // 1000}.wav"
        segmento.export(archivo_segmento, format="wav")
        segmentos.append(archivo_segmento)
    return segmentos

def guardar_transcripcion(archivo_audio, texto):
    ruta_audio = os.path.dirname(archivo_audio)
    nombre_archivo_salida = os.path.splitext(os.path.basename(archivo_audio))[0] + '.txt'
    archivo_salida = os.path.join(ruta_audio, nombre_archivo_salida)
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(texto)
    return archivo_salida

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('descargas'):
        os.makedirs('descargas')
    app.run(debug=True)