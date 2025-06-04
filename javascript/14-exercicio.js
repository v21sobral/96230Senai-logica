// Exercício

console.clear()
const readline = require('readline-sync');

const listaPar = [];
const listaImpar = [];
const numero = [];


for (let i = 0; i <= 5; i++) {
  const numero = readline.questionFloat(`Digite o ${i + 1}o numero: `);
  if (numero % 2 === 0) {
    listaPar.push(numero);
  } else {
    listaImpar.push(numero);
  }

}


console.log(`\nQuantitades de pares: ${listaPar.length}`);
console.log(`\nQuantitades de impares: ${listaImpar.length}`);



