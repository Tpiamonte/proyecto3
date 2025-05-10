function mostrarGrafica(numero) {
  const graficas = document.querySelectorAll('.grafica');

  graficas.forEach((grafica, index) => {
    if (index === numero - 1) {
      grafica.style.display = 'block';
      setTimeout(() => {
        grafica.classList.add('visible');
      }, 10); // pequeño delay para activar el transition
    } else {
      grafica.classList.remove('visible');
      setTimeout(() => {
        grafica.style.display = 'none';
      }, 600); // esperar a que termine la transición
    }
  });
}

document.getElementById('graficaDe1').addEventListener('click', () => mostrarGrafica(1));
document.getElementById('graficaDe2').addEventListener('click', () => mostrarGrafica(2));
document.getElementById('graficaDe3').addEventListener('click', () => mostrarGrafica(3));



document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('modal');
  const modalImg = document.getElementById('img-ampliada');
  const cerrar = document.querySelector('.cerrar');

  document.querySelectorAll('.zoomable').forEach((img) => {
    img.addEventListener('click', function () {
      modal.style.display = 'block';
      modalImg.src = this.src;
      modalImg.alt = this.alt;
    });
  });

  cerrar.onclick = function () {
    modal.style.display = 'none';
  };

  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = 'none';
    }
  };
});

