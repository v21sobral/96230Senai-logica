const notas = [];
const notaInput = document.getElementById('notaInput');
const listaNotas = document.getElementById('listaNotas');
const resultado = document.getElementById('resultado');

function adicionarNota() {
  const nota = parseFloat(notaInput.value);
  
  if (isNaN(nota) || nota < 0 || nota > 10) {
    alert('Digite uma nota válida entre 0 e 10.');
    return;
  }

  if (notas.length >= 4) {
    alert('Você já inseriu 4 notas.');
    return;
  }

  notas.push(nota);
  atualizarListaNotas();
  notaInput.value = '';
  notaInput.focus();

  if (notas.length === 4) {
    calcularMedia();
  }
}

function atualizarListaNotas() {
  listaNotas.innerHTML = '';
  notas.forEach((n, i) => {
    const item = document.createElement('li');
    item.textContent = `Nota ${i + 1}: ${n}`;
    listaNotas.appendChild(item);
  });
}

function calcularMedia() {
  const soma = notas.reduce((acc, val) => acc + val, 0);
  const media = soma / notas.length;
  resultado.textContent = `Média final: ${media.toFixed(2)}`;
}
