from pydub import AudioSegment
import os
import requests

def descargar_archivo(url, ruta_salida):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        with open(ruta_salida, 'wb') as archivo:
            archivo.write(respuesta.content)
        print(f"Archivo descargado y guardado en: {ruta_salida}")
    else:
        print(f"Error al descargar el archivo: {respuesta.status_code}")

def procesar_audio(consulta):
    base_url = "https://cumi.gotelemedicina.co:8443"
    audio_path = consulta["audio"]
    audio_url = base_url + audio_path

    nombre_paciente = consulta["nombres"].replace(" ", "_")
    ruta_salida_webm = os.path.join('descargas', f'{nombre_paciente}.webm')

    # Descargar el archivo de audio
    descargar_archivo(audio_url, ruta_salida_webm)

    return ruta_salida_webm