// Função para adicionar um valor ao visor
function adicionar(valor) {
  var visor = document.getElementById('visor');
  visor.value += valor;
}

// Função para limpar o visor
function limpar() {
  document.getElementById('visor').value = '';
}

// Função para apagar o último caractere
function apagar() {
  var visor = document.getElementById('visor');
  visor.value = visor.value.slice(0, -1);
}

// Função para calcular o resultado
function calcular() {
  var visor = document.getElementById('visor');
  try {
    let expressao = visor.value
      .replace(/√([0-9.]+)/g, 'Math.sqrt($1)');
    visor.value = eval(expressao);
  } catch (error) {
    visor.value = 'Erro';
  }
}