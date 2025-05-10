""" from flask import Flask, render_template, request, redirect, url_for
from inteligencia import obtener_analisis_ia

app = Flask(__name__)

@app.route("/", endpoint="home")
def index():
    return render_template("index.html")

@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        datos = request.form

        prompt = "Estoy realizando un análisis de personalidad basado en las siguientes respuestas:\n\n"
        for pregunta, respuesta in datos.items():
            prompt += f"Pregunta: {pregunta}\nRespuesta: {respuesta}\n\n"
        prompt += "Estoy realizando un análisis de personalidad con base en las siguientes respuestas. Por favor, analiza el conjunto completo (no pregunta por pregunta) y elige una sola categoría de personalidad de las siguientes (sin combinar varias): Analistas: Arquitecto (pensador imaginativo), Lógico (inventor), Comandante (líder audaz e imaginativo), Innovador (pensador inteligente y curioso). Diplomáticos: Abogado (callado, místico e idealista), Mediador (poético, amable y altruista), Protagonista (líder carismático e inspirador), Activista (espíritu libre, entusiasta y social). Centinelas: Logista (práctico y enfocado en los hechos), Defensor (protector, dedicado y cálido), Ejecutivo (administrador responsable), Cónsul (popular y sociable). Exploradores: Virtuoso (audaz y práctico), Aventurero (artista flexible y encantador), Emprendedor (perceptivo e inteligente), Animador (espontáneo, enérgico y entusiasta).  Basado en el estilo general del usuario, elige solo una personalidad y descríbela con claridad, sin mencionar las otras categorías. El análisis debe ser en un solo párrafo y directo, sin listas ni encabezados"

        analisis = obtener_analisis_ia(prompt)

        # Detectar categoría
        titulo, clave_categoria = detectar_categoria(analisis)

        # Cargar imagen desde /static/images/<clave_categoria>.png
        imagen_url = url_for('static', filename=f'images/{clave_categoria}.png')

        return render_template("resultado.html", analisis=analisis, titulo=titulo, imagen=imagen_url, Tipo_persona = nombreTipo )

    return render_template("formulario.html")

def detectar_categoria(analisis):
    categorias = {
        "arquitecto": "Arquitecto",
        "logico": "Lógico",
        "comandante": "Comandante",
        "innovador": "Innovador",
        "abogado": "Abogado",
        "mediador": "Mediador",
        "protagonista": "Protagonista",
        "activista": "Activista",
        "logista": "Logista",
        "defensor": "Defensor",
        "ejecutivo": "Ejecutivo",
        "consul": "Cónsul",
        "virtuoso": "Virtuoso",
        "aventurero": "Aventurero",
        "emprendedor": "Emprendedor",
        "animador": "Animador"
    }

    analisis_lower = analisis.lower()

    for clave, nombre in categorias.items():
        if clave in analisis_lower:
            nombreTipo = nombre
            return nombre, clave  # clave la usamos para cargar la imagen
    return "Tipo desconocido", "desconocido"



if __name__ == "__main__":
    app.run(debug=True)
 """
 
from flask import Flask, render_template, request, url_for
from inteligencia import obtener_analisis_ia

app = Flask(__name__)

# Detecta la categoría en el texto de la IA
def detectar_categoria(analisis):
    categorias = {
        "arquitecto": "Arquitecto",
        "logico": "Lógico",
        "comandante": "Comandante",
        "innovador": "Innovador",
        "abogado": "Abogado",
        "mediador": "Mediador",
        "protagonista": "Protagonista",
        "activista": "Activista",
        "logista": "Logista",
        "defensor": "Defensor",
        "ejecutivo": "Ejecutivo",
        "consul": "Cónsul",
        "virtuoso": "Virtuoso",
        "aventurero": "Aventurero",
        "emprendedor": "Emprendedor",
        "animador": "Animador"
    }

    analisis_lower = analisis.lower()
    for clave, nombre in categorias.items():
        if clave in analisis_lower:
            return nombre, clave  # nombre legible, clave para imagen
    return "Tipo desconocido", "desconocido"

@app.route("/", endpoint="home")
def index():
    return render_template("index.html")

@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        datos = request.form

        # ✅ Prompt mejorado
        prompt = (
            "Estoy realizando un análisis de personalidad con base en las siguientes respuestas. "
            "Por favor, analiza el conjunto completo (no pregunta por pregunta) y elige una sola categoría de personalidad "
            "de las siguientes (sin combinar varias):\n\n"
            "Analistas: Arquitecto, Lógico, Comandante, Innovador.\n"
            "Diplomáticos: Abogado, Mediador, Protagonista, Activista.\n"
            "Centinelas: Logista, Defensor, Ejecutivo, Cónsul.\n"
            "Exploradores: Virtuoso, Aventurero, Emprendedor, Animador.\n\n"
            "Elige solo una personalidad y descríbela claramente. No menciones otras categorías. "
            "Escribe el tipo de personalidad al inicio del párrafo entre asteriscos (por ejemplo: *Arquitecto*). "
            "Luego continúa con un análisis breve y directo en un solo párrafo.\n\n"
        )

        # Agregar respuestas del usuario al prompt
        for pregunta, respuesta in datos.items():
            prompt += f"{pregunta}: {respuesta}\n"

        #  Obtener análisis de la IA
        analisis = obtener_analisis_ia(prompt)

        #  Detectar tipo de personalidad
        titulo, clave_categoria = detectar_categoria(analisis)

        #  Imagen personalizada (ubicada en /static/images/)
        imagen_url = url_for('static', filename=f'images/{clave_categoria}.png')

        #  Mostrar resultado personalizado
        return render_template("resultado.html", analisis=analisis, titulo=titulo, imagen=imagen_url)

    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
