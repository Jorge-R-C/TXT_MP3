from converter import convertir_articulo_a_audio # llamamos la funcion desde converter.py

url=input("Ingrese el linck del articulo a leer :").strip() #pregunta al usuario para que pegue el linck qeu quiere convertir a audio
convertir_articulo_a_audio(url) #llamamos a la funcion que genera toda la accion del codigo