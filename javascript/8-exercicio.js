
const readlineSync = require('readline-sync');

multiplicacao = 0;
soma = 0;
let numero1 = parseInt(readlineSync.question("Digitte um numero:"));
let numero2 = parseInt(readlineSync.question("Digitte um numero:"));

if (numero1 == numero2) {
    soma = numero1 + numero2;
    console.log(`A soma dos número é: ${soma}`);
    
} 
else if (numero1 != numero2) {
    multiplicacao = numero1 * numero2;
    console.log(`A multiplicação dos número é: ${multiplicacao}`);
}



