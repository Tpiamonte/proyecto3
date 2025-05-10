document.getElementById('formulario').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const respuestas = {
      pregunta1: document.querySelector('input[name="pregunta1"]:checked').value,
      pregunta2: document.querySelector('input[name="pregunta2"]:checked').value,
      pregunta3: document.querySelector('input[name="pregunta3"]:checked').value,
      pregunta4: document.querySelector('input[name="pregunta4"]:checked').value
    };
  
    localStorage.setItem('respuestasTest', JSON.stringify(respuestas));
    window.location.href = 'resultado.html';
  });
  