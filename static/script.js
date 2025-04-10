// Handle the "Submit" button click
document.getElementById('submitFormButton').addEventListener('click', function () {
    const form = document.getElementById('tripForm'); // Get the form element

    // Collect form data using form.elements
    const formData = {
        destination: form.elements['destination'].value,
        origin: form.elements['origin'].value, 
        duration: form.elements['duration'].value,
        month: form.elements['month'].value,
        travelerType: form.elements['travelerType'].value 
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

        let message;
        if (data.estimatedCost === -1) {
            message = `Sorry, the destination '${data.destination}' isn't available at this time.`;
        } else if (data.estimatedCost === -2) {
            message = `Sorry, the origin '${data.origin}' isn't available at this time.`;
        } else if (data.estimatedCost === -3) {
            message = 'Number of days is not valid';
        } else {
            message = `Your trip from ${data.origin} to ${data.destination} in ${data.month} will be ${data.duration} days long on a ${data.travelerType} budget and will cost $${Math.round(data.estimatedCost)}.`;
        }

        // Display the constructed message
        document.getElementById('responseQuestions').innerText = message;
    })
    .catch(error => console.error('Error:', error)); // Handle errors
});
