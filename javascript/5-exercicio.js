//Criando vetor com objetos

const usuarios = [
    {nome: 'Ana', idade: 25},
    {nome: 'Marta', idade: 32},
    {nome: 'Maria', idade: 45},
];

console.log('Exibindo todos os elementos do vetor');
usuarios.forEach(usuario => {
    console.log(`${usuario.nome} tem ${usuario.idade} anos`);
});

console.log('\nFiltrando usuário.');
console.log('Apenas usuários até 30 anos.');
const menorQueTrintaAnos = usuarios.filter(usuario => usuario.idade <= 30);
menorQueTrintaAnos.forEach(usuario => {
    console.log(`${usuario.nome} tem ${usuario.idade} anos`);
});

console.log('Exibindo apenas o nome dos usuários.');
const nomes = usuarios.map(usuario => usuario.nome);
nomes.forEach(nome => {
    console.log(`Nome: ${nome}`);
});

console.log('Exibindo o nome dos usuários com numeração.');
nomes.forEach((nome, index) => {
    console.log(`${++index}: ${nome}`);
});

console.log('\nEncontrar um usuário.');
const usuarioEncontrado = usuarios.find(usuario => usuario.nome === 'Marta');
console.log(`Nome: ${usuarioEncontrado.nome}, idade: ${usuarioEncontrado.idade}`);

console.log('\nMostra a soma de todas as idades.')
const somaIdades = usuarios.reduce((total, usuario) => total + usuario.idade, 0)
console.log(`Total: ${somaIdades}`)