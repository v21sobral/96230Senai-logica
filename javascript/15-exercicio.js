// Exercício

console.clear()
const readline = require('readline-sync');

const listaPositivos = [];
const listaNegativos = [];
const numero = [];

for (let i = 0; i <= 4; i++) {
  const numero = readline.questionFloat(`Digite o ${i + 1}o numero: `);
  if (numero > 0) {
    listaPositivos.push(numero);
  } else {
    listaNegativos.push(numero);
  }

}


console.log(`\nQuantitades de pares: ${listaNegativos.length}`);
console.log(`\nQuantitades de impares: ${listaImpar.length}`);



