const respuestas = JSON.parse(localStorage.getItem("respuestasTest"));
const resultadoDiv = document.getElementById("resultado");

if (!respuestas) {
  resultadoDiv.innerHTML =
    '<p>No se encontraron respuestas. Vuelve al <a href="/Templates/index.html">test</a>.</p>';
} else {
  let textoResultado = "";

  if (respuestas.pregunta1 === "extrovertido") {
    textoResultado += "<p>Eres una persona sociable y activa.</p>";
  } else {
    textoResultado += "<p>Prefieres la tranquilidad y la introspección.</p>";
  }

  if (respuestas.pregunta2 === "organizado") {
    textoResultado += "<p>Te gusta la planificación y el orden.</p>";
  } else {
    textoResultado += "<p>Eres más espontáneo y flexible.</p>";
  }

  if (respuestas.pregunta3 === "logico") {
    textoResultado += "<p>Tomas decisiones con lógica y razón.</p>";
  } else {
    textoResultado +=
      "<p>Dejas que tus emociones influyan en tus decisiones.</p>";
  }

  if (respuestas.pregunta4 === "curioso") {
    textoResultado +=
      "<p>Eres una persona curiosa y con mentalidad abierta.</p>";
  } else {
    textoResultado += "<p>Prefieres lo práctico y lo conocido.</p>";
  }

  resultadoDiv.innerHTML = textoResultado;
}
