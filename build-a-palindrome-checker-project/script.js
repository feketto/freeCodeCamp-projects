const textInput = document.getElementById('text-input');
const checkBtn = document.getElementById('check-btn');
const resultEl = document.getElementById('result');

const cleanString = (str) => {
    return str.toLowerCase().replace(/[^a-z0-9]/g, '');
};

const isPalindrome = (str) => {
    const reversedStr = str.split('').reverse().join('');
    return str === reversedStr;
};

const checkPalindrome = () => {
    const originalInput = textInput.value;

    if (originalInput.trim() === '') {
        resultEl.innerHTML = '<span>Please input a value</span>';
        alert('Please input a value');
        resultEl.className = 'text-lg font-medium';
        return;
    }

    const cleanedInput = cleanString(originalInput);
    
    const result = isPalindrome(cleanedInput);

    const resultMessage = `<strong class="text-cyan-400">${originalInput}</strong> is ${result ? '' : 'not '}a palindrome.`;

    resultEl.innerHTML = resultMessage;

    if (result) {
        resultEl.className = 'text-lg font-medium text-green-400';
    } else {
        resultEl.className = 'text-lg font-medium text-red-400';
    }
};

checkBtn.addEventListener('click', checkPalindrome);

textInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        checkPalindrome();
    }
});
