from newspaper import Article #llamamos a la funcion Article de newsaper
from gtts import gTTS #importaos la libreria gtts y a la vez traemos su funcion gTTS 
from gtts.lang import tts_langs #importamos todos los idiomas de traduccion 
from playsound import playsound #interprete de mp3 
import nltk #libreria de tokenizacion de texto
from nltk.tokenize import sent_tokenize #importacion de divisor para cadena de token y poder leer el sistema


nltk.download('punkt') #identifica las limitaciones naturales del texto para dividir




def obtener_texto_url(url): #funcion de lectura de linck

    articulo = Article(url,language='es') #descarga y lee el articulo del linck

    articulo.download()#descarga articulo
    articulo.parse()#Extrae título y texto limpio

    titulo = articulo.title #dividimos por texto de articulo
    texto = articulo.text #y por titulo de articulo

    return titulo,texto #llamamos a mostrar tanto titulo como articulo

def procesar_texto(texto):

    #Divide el texto en oraciones y las une en una sola cadena
    #para que gTTS lo lea de forma más natural.
    oraciones = sent_tokenize(texto,language='spanish')  
    return" ".join(oraciones) 

def idiomas():
    idiomas_disponibles = tts_langs() 

    #Muestra los idiomas disponibles y permite al usuario elegir uno.
    #Retorna el código de idioma seleccionado o 'es' por defecto.

    print("Idiomas disponibles a traduccion") 
    for codigo , nombre in idiomas_disponibles.items(): 
        print(f"{codigo}:{nombre}") 
    
    idioma = input("Ingrese el codigo del idiomas ej: es,fr,").strip() #elige el usuario y con strip() sacamos tanto los espacios de delante como al final

    if idioma not in idiomas_disponibles: #si el idioma no existe o no esta soportado por el sistema, dejamos el castellano por defecto
        print("Idioma no soportado se usara espaniol por defecto")
        idioma = 'es' #aca igualamos el idioma en la variable por defecto
    return idioma 


def convertir_de_texto_a_audio(texto,archivo_mp3,idioma='es'): 
    tts = gTTS(text=texto,lang= idioma) # genera el texto plano a mp3 en el idioma elegido
    tts.save(archivo_mp3) # guardamos la lectura  del texo plano en mp3 
    print(f"Texto guardado en archivo {archivo_mp3}")

import os #interfaz para comunicarse con el S.O

def convertir_articulo_a_audio(url): 
    titulo,texto = obtener_texto_url(url)
    idioma = idiomas()
    texto_procesado = procesar_texto(texto)
    
    os.makedirs("data/audio",exist_ok=True) #Crear carpeta de audios si no existe

    #Limpiar título para nombre de archivo (evita errores con caracteres raros
    archivo_mp3=os.path.join("data/audio",f"{titulo}.mp3") #construimos ruta de archivo
    convertir_de_texto_a_audio(texto_procesado,f"{titulo}.mp3",idioma)

    playsound(archivo_mp3)    

