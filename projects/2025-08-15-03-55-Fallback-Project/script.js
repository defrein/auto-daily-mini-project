// Fallback Project JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('click-btn');
    const messageDiv = document.getElementById('message');
    
    const messages = [
        "Hello! 👋",
        "This is a fallback project! 🚀",
        "Generated automatically! 🤖",
        "Have a great day! ☀️",
        "Keep coding! 💻"
    ];
    
    let clickCount = 0;
    
    button.addEventListener('click', function() {
        clickCount++;
        const messageIndex = (clickCount - 1) % messages.length;
        messageDiv.textContent = messages[messageIndex];
        
        // Add some animation
        messageDiv.style.transform = 'scale(0.9)';
        setTimeout(() => {
            messageDiv.style.transform = 'scale(1)';
        }, 150);
    });
    
    // Initial message
    messageDiv.textContent = "Click the button to see messages!";
});