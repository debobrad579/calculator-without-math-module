document.querySelector('button').addEventListener('click', () => {
    const equation = document.querySelector('input').value;
    displaySolution(equation);
})

function displaySolution(equation) {
    fetch(`/api?equation=${equation.replace('+', 'Ψ')}`)
    .then(response => response.json())
    .then(data => {
        document.querySelector('h2').innerHTML = data.equation;
    });
}
