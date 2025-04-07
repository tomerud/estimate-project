// Handle the "Submit" button click
document.getElementById('submitFormButton').addEventListener('click', function () {
    const form = document.getElementById('tripForm'); // Get the form element

    // Collect form data using form.elements
    const formData = {
        destination: form.elements['destination'].value,
        duration: form.elements['duration'].value,
        travelerType: form.elements['travelerType'].value // Corrected key
    };

    console.log('Form data:', formData); // Log the form data

    // Send data to the server
    fetch('/form-submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData) // Convert formData to JSON
    })
        .then(response => response.json()) // Parse the response as JSON
        .then(data => {
            console.log('Parsed response data:', data); // Log the parsed JSON data

            // Check if the estimated cost is -1
            let message;
            if (data.estimatedCost === -1) {
                message = `Sorry, the destination '${data.destination}' isn't available at this time.`;
            } else {
                message = `Your trip to ${data.destination} will be ${data.duration} days long on a ${data.travelerType} budget and will cost $${data.estimatedCost}.`;
            }

            // Display the constructed message
            document.getElementById('responseQuestions').innerText = message;
        })
        .catch(error => console.error('Error:', error)); // Handle errors
});