
const readlineSync = require('readline-sync');



let numero = parseInt(readlineSync.question("Digitte um numero:"));


if (numero == 0) {
    console.log(`${numero} é neutro`);
}
else if (numero % 2 == 0) {
    console.log(`${numero} é par`);
    
} 
else  {
    console.log(`${numero} é impar`);
}



