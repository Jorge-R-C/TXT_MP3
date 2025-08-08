# Lector de Artículos a Audio

Este proyecto toma un artículo desde una URL, extrae su contenido, lo procesa y lo convierte en un archivo de audio (.mp3) utilizando herramientas como `newspaper3k`, `gTTS` y `nltk`.


Tegnologia utilizadas

Python:
- [newspaper3k](https://newspaper.readthedocs.io/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
- [NLTK (Natural Language Toolkit)](https://www.nltk.org/)
- `playsound` para reproducir el archivo generado

Funcionalidades:

- Extrae el título y contenido del artículo automáticamente desde una URL.
- Procesa el texto para mejorar su calidad antes de convertirlo a voz.
- Elige automáticamente el idioma adecuado para la conversión.
- Convierte el texto en un archivo de audio `.mp3` y lo reproduce.


Como usarlo

1. Clona el repositorio 
  
  bash
git clone https://github.com/tu-usuario/nombre-repo.git

2. Instala las dependencias necesarias:

pip install -r requirements.txt

3. Ejecuta el archivo proncipal de tu entorno:

  python main.py


##Requisitos previos
  - Python 3.10 o superior 
  - pip instalado 
  - (opcional) utilizar entornos venv o conda 

