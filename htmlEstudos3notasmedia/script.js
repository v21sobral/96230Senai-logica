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

  if (notas.length >= 3) {
    alert('Você já inseriu 3 notas.');
    return;
  }

  notas.push(nota);
  atualizarListaNotas();
  notaInput.value = '';
  notaInput.focus();

  if (notas.length === 3) {
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
  let status = '';
  let classe = '';

  if (media <= 4) {
    status = 'Reprovado';
    classe = 'reprovado';
  } else if (media < 7) {
    status = 'Recuperação';
    classe = 'recuperacao';
  } else {
    status = 'Aprovado';
    classe = 'aprovado';
  }

  resultado.textContent = `Média final: ${media.toFixed(2)} - ${status}`;
  resultado.className = classe;
}

function reiniciar() {
  notas.length = 0; // esvazia o array
  listaNotas.innerHTML = '';
  resultado.textContent = '';
  resultado.className = '';
  notaInput.value = '';
  notaInput.focus();
}