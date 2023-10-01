let input_string = ''; // Initialize input_string

function checkPlagiarism() {
    // Get the text from the input box
    input_string = document.getElementById('inputText').value;
    
    // Send an HTTP request to the Flask backend to calculate plagiarism
    fetch('/calculate_plagiarism', {
        method: 'POST', // Use POST method to send the input text to the server
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_text: input_string }), // Send the input text as JSON data
    })
        .then(response => response.json())
        .then(data => {
            // Display the result in the HTML
            document.getElementById('result').textContent = `Plagiarism Score: ${data.average_score.toFixed(2)}%`;
        });
}
