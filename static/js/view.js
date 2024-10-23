document.addEventListener('DOMContentLoaded', () => {
    const apiUrl = '/api/transformers';

    // Get the transformer name from the URL path
    const transformerName = window.location.pathname.split('/').pop();

    // Fetch Transformer details by name
    fetch(`${apiUrl}?name=${encodeURIComponent(transformerName)}`)
        .then(response => response.json())
        .then(data => {
            if (data.transformers && data.transformers.length > 0) {
                const transformer = data.transformers[0]; // We expect only one result based on name
                document.getElementById('name').textContent = transformer.name;
                document.getElementById('quote').textContent = transformer.quote;
                document.getElementById('affiliation').textContent = transformer.affiliation;
                document.getElementById('transformation_mode').textContent = transformer.transformation_mode || 'N/A';
                document.getElementById('description').textContent = transformer.description || 'No description available';
                
                if (transformer.image_url) {
                    const imgElement = document.getElementById('transformer-image');
                    imgElement.src = transformer.image_url;
                    imgElement.style.display = 'block'; //Show the image
                }
            } else {
                alert('Transformer not found!');
                window.location.href = '/';  // Redirect to the list page if not found
            }
        })
        .catch(error => {
            console.error('Error fetching transformer details:', error);

        });
});
