/*console.clear()
const readlineSync = require('readline-sync');



let login = readlineSync.question("Digite seu login:");
let senha = parseInt(readlineSync.question("Digite sua senha:"));

while (true) {
    if (senha === 123456 && login === "victor") {
        console.log(`Bem-vindo à rede social`);
        break;
    } else {
        console.log(`Login ou senha inválidos`);
        login = readlineSync.question("Digite seu login:");
        senha = parseInt(readlineSync.question("Digite sua senha:"));
    }
}*/

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio do formulário

    const usuario = document.getElementById('usuario').value;
    const senha = document.getElementById('senha').value;
    const mensagem = document.getElementById('mensagem');

    if (usuario == 'victor' && senha == '1234') {
        mensagem.textContent = 'Login realizado com sucesso!';
        mensagem.style.color = 'green';
    } else {
        mensagem.textContent = 'Usuário ou senha incorretos!';
        mensagem.style.color = 'red';
    }
});