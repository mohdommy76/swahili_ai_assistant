function getChatResponse() {
    const inputText = document.getElementById('user_input').value;
    document.getElementById('loading').style.display = 'block';
    fetch(`https://your-app-name.onrender.com/chat?input_text=${inputText}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('chat_response').innerText = data.response;
        })
        .catch(() => {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('chat_response').innerText = 'Error fetching response.';
        });
}
