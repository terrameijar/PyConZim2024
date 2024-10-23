document.addEventListener('DOMContentLoaded', ()=> {
    const apiUrl = '/api/transformers';
    let currentPage = 1;

    // Display and fetch transformers
    function loadTransformers(page = 1, name='', affiliation=''){
        const url = `${apiUrl}?page=${page}&name=${encodeURIComponent(name)}&affiliation=${affiliation}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const tbody = document.querySelector('#transformers-table tbody');
                tbody.innerHTML = '';

                data.transformers.forEach(transformer => {
                    const row = `
                        <tr>
                            <td>${transformer.name}</td>
                            <td>${transformer.affiliation}</td>
                            <td>${transformer.transformation_mode || 'N/A'}</td>

                            <td>
                                <a href="/transformers/${encodeURIComponent(transformer.name)}">View</a>
                        
                                
                            </td>
                        </tr>
                    `;
                    tbody.innerHTML += row;
                });

                document.getElementById('page-info').textContent = `Page ${data.page} of ${data.total_pages}`;
                currentPage = data.page;
            });
    }

    // Search form event lister
    document.getElementById('search-form').addEventListener('submit', event => {
        event.preventDefault();
        const name = document.getElementById('name').value;
        const affiliation = document.getElementById('affiliation').value;
        loadTransformers(1, name, affiliation);
    });

    // Clear button event listener
    document.getElementById('clear-button').addEventListener('click', ()=>{
        document.getElementById('name').value = '';
        document.getElementById('affiliation').value = '';
    });

    // Pagination control
    document.getElementById('prev-page').addEventListener('click', () => {
        if (currentPage > 1) {
            loadTransformers(currentPage - 1);
        }
    });

    document.getElementById('next-page').addEventListener('click', () => {
        loadTransformers(currentPage + 1);
        
    });

    // Load first page on load
    loadTransformers();
});