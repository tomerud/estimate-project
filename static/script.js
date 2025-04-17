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

        let flag = 0;
        let message;
        if (data.estimatedCost === -1) {
            message = `Sorry, the destination '${data.destination}' isn't available at this time.`;
        } else if (data.estimatedCost === -2) {
            message = `Sorry, the origin '${data.origin}' isn't available at this time.`;
        } else if (data.estimatedCost === -3) {
            message = 'Number of days is not valid';
        } else {
            flag = 1;
            message = `Your trip from ${data.origin} to ${data.destination} in ${data.month} will be ${data.duration} days long on a ${data.travelerType} budget and will cost $${Math.round(data.estimatedCost)}. \n description: \n budget: ${data.dailyBudget} per day. \n ${data.flightPrice} for flight.\n `;
        }
        
        // Display the constructed message
        document.getElementById('responseQuestions').innerText = message;

        // When flag === 1, show the "Are you satisfied?" question along with Yes and No buttons.
        if (flag === 1) {
            console.log('Displaying satisfaction question because flag is 1');
            document.getElementById('areYouSatisfied').innerHTML = `
                <p>Are you satisfied with this price?</p>
                <button id="yesButton">Yes, thats great</button>
                <button id="noButton">No,Show me some alternatives</button>
            `;
            
            document.getElementById('yesButton').addEventListener('click', function() {
                console.log('User is satisfied');

            });
            
            document.getElementById('noButton').addEventListener('click', () => {
                // pack all returned fields into the query string
                const params = new URLSearchParams({
                  origin:       data.origin,
                  destination:  data.destination,
                  duration:     data.duration,
                  month:        data.month,
                  travelerType: data.travelerType,
                  dailyBudget:  data.dailyBudget,
                  flightPrice:  data.flightPrice,
                  estimatedCost:data.estimatedCost
                });
                window.location.href = `/alternatives?${params.toString()}`;
              });
            } else {
              document.getElementById('areYouSatisfied').innerText = '';
            }
          })
          .catch(err => console.error('Error:', err));
        });