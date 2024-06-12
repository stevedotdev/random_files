document.getElementById('search-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const regexInput = document.getElementById('regex-input').value;
    const textInput = document.getElementById('text-input').value;
    const resultDiv = document.getElementById('result');

    try {
        const regex = new RegExp(regexInput, 'g');
        const highlighted = textInput.replace(regex, '<span class="highlight">$&</span>');

        resultDiv.innerHTML = highlighted;
    } catch (e) {
        console.error('Invalid regular expression', e);
        resultDiv.innerText = 'Invalid regular expression';
    }
});
