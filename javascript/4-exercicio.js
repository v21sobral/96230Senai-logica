// Criando vetor

const frutas = ['Maçã', 'Banana', 'Laranja'];

console.log('\nExibindo apenas um elemento dentro do vetor.');
console.log(frutas[0]);
console.log(frutas[2]);

console.log('\nAdicionando elemento ao vetor.');
frutas.push('Uvas'); // Corrigido de 'pus' para 'push'
console.log(frutas);

console.log('\nRemovendo o primeiro elemento do vetor.');
frutas.shift();
console.log(frutas);

console.log('\nPercorrendo vetor.');
frutas.forEach((fruta, index) => { // Corrigida a sintaxe do forEach
    console.log(`${++index}: ${fruta}`);
});


