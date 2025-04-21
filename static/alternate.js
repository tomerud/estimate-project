document.getElementById('preferencesFormButton').addEventListener('click', function () {
  const form = document.getElementById('preferencesForm'); // Get the form element

  // Get URL parameters
  const params = new URLSearchParams(window.location.search);

  // Collect form data using form.elements
  const requestData = {
    development: form.elements['development'].value,
    farAway: form.elements['farAway'].value,
    weather: form.elements['weather'].value,
    culture: form.elements['culture'].value, // Now correctly references the updated name

    // Add URL parameters
    origin: params.get('origin'),
    destination: params.get('destination'),
    duration: params.get('duration'),
    month: params.get('month'),
    travelerType: params.get('travelerType'),
    estimatedCost: params.get('estimatedCost')
  };

  console.log('Request data:', requestData);

  fetch('/get_other_destinations', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(requestData) // Convert requestData to JSON
  })
  .then(response => response.json())
  .then(data => {
    console.log('Response:', data);
  })
  .catch(err => console.error('Error:', err));
});