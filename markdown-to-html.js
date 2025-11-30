function convertMarkdown() {
    const inputElement = document.getElementById('markdown-input');

    if (!inputElement) {
        return '';
    }
    
    const input = inputElement.value;
    let html = input;
    html = html.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img alt="$1" src="$2">');
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/__(.+?)__/g, '<strong>$1</strong>');
    html = html.replace(/\*([^*]+?)\*/g, '<em>$1</em>');
    html = html.replace(/_([^_]+?)_/g, '<em>$1</em>');
    html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
    html = html.replace(/^# (.+)$/gm, '<h1>$1</h1>');
    html = html.replace(/^> (.+)$/gm, '<blockquote>$1</blockquote>');
    
    return html;
}


document.addEventListener('DOMContentLoaded', function() {
    const markdownInput = document.getElementById('markdown-input');
    const htmlOutput = document.getElementById('html-output');
    const preview = document.getElementById('preview');
    
    if (markdownInput && htmlOutput && preview) {
        markdownInput.addEventListener('input', function() {
            const htmlResult = convertMarkdown();
            htmlOutput.textContent = htmlResult;
            preview.innerHTML = htmlResult;
        });
        
        const htmlResult = convertMarkdown();
        htmlOutput.textContent = htmlResult;
        preview.innerHTML = htmlResult;
    }
});