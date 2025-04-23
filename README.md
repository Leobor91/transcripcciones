# Proyecto de Transcripción y Descarga de Audio

Este proyecto permite subir archivos de audio para transcripción y descargar archivos de audio desde una URL especificada. Utiliza Flask para el backend y JavaScript para el frontend.

## Requisitos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)
- Flask
- pydub
- requests
- speech_recognition

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Leobor91/transcripcciones.git
cd proyecto-audio

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

pip install Flask pydub requests speechrecognition

proyecto-audio/
│
├── [app.py](http://_vscodecontentref_/2)
├── [audio_processor.py](http://_vscodecontentref_/3)
├── templates/
│   └── index.html
├── static/
│   └── style.css
│   └── script.js
├── uploads/
├── descargas/
└── [README.md](http://_vscodecontentref_/4)

Archivos Principales
app.py
Este archivo contiene la configuración del servidor Flask y las rutas para manejar la transcripción y la descarga de audio.

audio_processor.py
Este archivo contiene la lógica para descargar archivos de audio desde una URL.

templates/index.html
Este archivo contiene el HTML para la interfaz de usuario.

static/style.css
Este archivo contiene los estilos CSS para la interfaz de usuario.

static/script.js
Este archivo contiene el JavaScript para manejar la lógica del frontend, incluyendo la subida de archivos, la descarga de audio y la limpieza de formularios.

Uso
Ejecuta el servidor Flask:

python [app.py](http://_vscodecontentref_/5)

Abre tu navegador web y navega a http://127.0.0.1:5000.

Para subir un archivo de audio para transcripción:

Haz clic en "Choose File" y selecciona un archivo de audio.
Haz clic en "Subir".
Para descargar un archivo de audio desde una URL:

Ingresa el nombre del usuario en el primer campo de texto.
Ingresa la ruta del audio en el segundo campo de texto.
Haz clic en "Descargar".
Para limpiar los formularios:

Haz clic en el botón "Clear" correspondiente.

Notas
Asegúrate de que las carpetas uploads y descargas existan en el directorio raíz del proyecto. Si no existen, el servidor Flask las creará automáticamente.
El archivo de audio subido se convierte a formato WAV y se verifica que cumpla con los requisitos (mono, 16 bits, 16 kHz) antes de ser transcrito.
La transcripción se realiza utilizando la API de Google Speech Recognition.
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría realizar.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


Este archivo [README.md](http://_vscodecontentref_/6) proporciona una guía completa para configurar y ejecutar el proyecto, así como una descripción de los archivos y su funcionalidad. Asegúrate de ajustar cualquier detalle específico de tu proyecto según sea necesario.

agrgar ka ruta de la carpeta ffmpeg-7.0.2-essentials_build/bin al path de las variables de entorno
