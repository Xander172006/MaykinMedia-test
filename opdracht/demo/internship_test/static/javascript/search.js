document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('city');
    const suggestionsBox = document.getElementById('suggestions');

    if (!cityInput || !suggestionsBox) {
        console.error('City input or suggestions box element not found');
        return;
    }

    cityInput.addEventListener('input', function() {
        const query = cityInput.value;
        if (query.length > 0) {
            fetch(`/autocomplete/?term=${query}`)
                .then(response => response.json())
                .then(data => {
                    suggestionsBox.innerHTML = '';
                    if (data.length > 0) {
                        data.forEach(city => {
                            const div = document.createElement('div');
                            div.style.padding = '8px';
                            div.style.cursor = 'pointer';
                            div.innerHTML = city.name;

                            div.addEventListener('mouseover', function() {
                                div.style.transform = 'translateX(10px)';
                            });

                            div.addEventListener('mouseout', function() {
                                div.style.transform = 'translateX(0)';
                            });

                            
                            div.addEventListener('click', function() {
                                cityInput.value = city.name;
                                suggestionsBox.innerHTML = '';
                                suggestionsBox.classList.add('hidden');
                            });
                            suggestionsBox.appendChild(div);
                        });
                        suggestionsBox.classList.remove('hidden');
                    } else {
                        suggestionsBox.classList.add('hidden');
                    }
                }).catch(error => console.error('Error:', error));
        } else {
            suggestionsBox.innerHTML = '';
            suggestionsBox.classList.add('hidden');
        }
    });
});

