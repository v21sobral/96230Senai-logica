
const readlineSync = require('readline-sync');



let numero = parseInt(readlineSync.question("Digitte um numero:"));


if ( numero > 2 && numero < 7) {
    console.log(`${numero} é dia util`);
}
else if (numero == 7 || numero == 1) {
    console.log(`${numero} é final de semana`);
    
} 
else  {
    console.log(`${numero} numero invalido`);
}



