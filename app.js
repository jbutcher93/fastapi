function makeApiRequest() {
    const apiUrl = document.getElementById('apiUrl').value;

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            document.getElementById('apiResult').textContent = data;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error.message);
            document.getElementById('apiResult').textContent = 'Error fetching data.';
        });
}
