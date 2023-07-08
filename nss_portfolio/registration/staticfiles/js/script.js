document.addEventListener('DOMContentLoaded', function() {
    var chatBody = document.getElementById('chat-body');
    var userInput = document.getElementById('user-input');
    var sendBtn = document.getElementById('send-btn');
  
    sendBtn.addEventListener('click', function() {
      var message = userInput.value;
      if (message.trim() !== '') {
        appendMessage('user', message);
        userInput.value = '';
        // Send user message to the backend or ChatGPT API for processing
        // Handle the response and append it to the chat body
      }
    });
  
    function appendMessage(sender, message) {
      var messageElement = document.createElement('div');
      messageElement.classList.add('message');
      messageElement.classList.add(sender);
      messageElement.innerText = message;
      chatBody.appendChild(messageElement);
      chatBody.scrollTop = chatBody.scrollHeight;
    }
  });
  