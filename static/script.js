document.addEventListener('DOMContentLoaded', function() {
    listarArchivos();
});

document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var formData = new FormData(this);
    var fileInput = document.querySelector('input[type="file"]');
    var fileName = fileInput.files[0].name;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/transcripcion', true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            document.getElementById('message').innerText = response.message;
            var transcriptionPath = response.transcription_path;
            var link = document.createElement('a');
            link.href = transcriptionPath;
            link.innerText = 'Ruta del archivo de transcripción: ' + transcriptionPath;
            link.target = '_blank';
            document.getElementById('transcription').innerHTML = '';
            document.getElementById('transcription').appendChild(link);
        } else {
            document.getElementById('message').innerText = 'Error al subir el archivo.';
        }
    };
    xhr.send(formData);
    document.getElementById('message').innerText = 'Subiendo archivo: ' + fileName;
});

function validateInputs() {
    var textInput1 = document.getElementById('textInput1').value.trim();
    var textInput2 = document.getElementById('textInput2').value.trim();
    var downloadButton = document.getElementById('downloadButton');
    downloadButton.disabled = textInput1 === '' || textInput2 === '';
}

document.getElementById('textInput1').addEventListener('input', validateInputs);
document.getElementById('textInput2').addEventListener('input', validateInputs);

document.getElementById('downloadButton').addEventListener('click', function() {
    var userInput1 = document.getElementById('textInput1').value;
    var userInput2 = document.getElementById('textInput2').value;

    // Crear el JSON con la estructura especificada
    var consulta = {
        "nombres": userInput1,
        "audio": userInput2
    };

    // Enviar el JSON al servidor
    fetch('/descargar_audio', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(consulta)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Respuesta del servidor:', data);

        // Mostrar una alerta indicando que la descarga se realizó correctamente
        alert('Descarga realizada correctamente');

        // Refrescar la página
        location.reload();
    })
    .catch(error => {
        console.error('Error al enviar el JSON al servidor:', error);
    });
});

// Función para limpiar el formulario de subida
document.getElementById('clearUploadForm').addEventListener('click', function() {
    document.querySelector('input[type="file"]').value = '';
    document.getElementById('message').innerText = '';
    document.getElementById('transcription').innerHTML = '';
});

// Función para limpiar los campos de texto
document.getElementById('clearTextInput').addEventListener('click', function() {
    document.getElementById('textInput1').value = '';
    document.getElementById('textInput2').value = '';
    validateInputs();
});

// Función para listar archivos TXT
function listarArchivos() {
    fetch('/listar_txt')
        .then(response => response.json())
        .then(data => {
            const listaArchivos = document.getElementById('lista-archivos');
            listaArchivos.innerHTML = '';
            data.archivos_txt.forEach(archivo => {
                const li = document.createElement('li');
                const link = document.createElement('a');
                link.href = `/uploads/${archivo}`;
                link.textContent = archivo;
                link.target = '_blank';
                li.appendChild(link);
                listaArchivos.appendChild(li);
            });
        })
        .catch(error => console.error('Error:', error));

}