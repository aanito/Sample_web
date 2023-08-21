document.querySelector('#search-form').addEventListener('submit', function(e) {
    e.preventDefault();
    var query = document.querySelector('input[name="query"]').value;
    fetch('/search?query=' + query)
        .then(response => response.json())
        .then(data => {
            var resultsContainer = document.querySelector('#search-results');
            resultsContainer.innerHTML = '';
            data.results.forEach(function(result) {
                var resultElement = document.createElement('div');
                resultElement.innerHTML = '<a href="/hospital/' + result.id + '">' + result.name + '</a>';
                resultsContainer.appendChild(resultElement);
            });
        });
});

