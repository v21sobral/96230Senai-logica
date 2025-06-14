function gerarTabuada() {
    // Pegar o valor do input do HTML
    const numeroInput = document.getElementById('numeroInput');
    let numero = parseInt(numeroInput.value);
    
    console.log("Número digitado:", numero); // Debug
    
    if (isNaN(numero)) {
        alert("Por favor, digite um número válido");
        return;
    }

    // Mostra o resultado onde a tabela deve ser exibida
    const resultadoDiv = document.getElementById('resultadoTabuada');
    resultadoDiv.innerHTML = '';

    // Adiciona um título para tabuada
    resultadoDiv.innerHTML += `<h2>Tabuada do ${numero}</h2>`;

    // Laço de repetição para gerar a tabuada
    for (let i = 0; i <= 10; i++) {
        let resultado = numero * i;
        // Adicionar cada linha da tabuada com um parágrafo
        resultadoDiv.innerHTML += `<p>${numero} x ${i} = ${resultado}</p>`;
    }
}

// A função gerarTabuada será executada quando clicar no botão
document.addEventListener('DOMContentLoaded', function() {
    const gerarBotao = document.getElementById('gerarBotao');
    gerarBotao.addEventListener('click', gerarTabuada);
    console.log("Event listener adicionado"); // Debug
});