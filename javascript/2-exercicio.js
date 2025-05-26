//Peça para o usuario informar um número, se o numero for maior que 10, 
// repita a pergunta até que ele informe um número menor ou igual a 10.
const readline = require('readline-sync');

soma = 0;
let nota = 0;

for (let i = 0; i < 3; i++) {
    do {
        nota = readline.questionInt('Informe uma nota: ');
    } while (nota < 0 || nota > 10);
    soma += nota;
}

let media = soma / 2;

console.log(`A média das notas é: ${media}`);