import google.generativeai as genai

GEMINI_API_KEY = "API_GENIMI"
genai.configure(api_key=GEMINI_API_KEY)
modelo = genai.GenerativeModel("gemini-2.0-flash")

def obtener_analisis_ia(mensaje):
    """
    Obtiene un análisis de personalidad desde la IA de Google
    
    Args:
        mensaje (str): El mensaje con las respuestas del test
        
    Returns:
        str: El análisis de personalidad generado por la IA
    """
    try:
        respuesta = modelo.generate_content(mensaje)
        return respuesta.text.strip()
    except Exception as e:
        print(f"Error al generar respuesta: {e}")
        return "Lo siento, hubo un problema al procesar tu análisis de personalidad. Por favor, intenta nuevamente más tarde."
