from src.converter import procesar_texto

def test_procesar_texto():
    texto = "Hola a todos, esto es una prueba"
    resultado = procesar_texto(texto)
    assert "Hola a todos" in resultado