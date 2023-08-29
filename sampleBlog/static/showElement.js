
        const showElement = document.getElementById('show-element-button');
        const hideElement = document.getElementById('hide-element-button');
        const element= document.getElementById("form-element");
        showElement.addEventListener('click', () => {
        element.style.display = 'block';
           });

       hideElement.addEventListener('click', () => {
           element.display = 'none';
                  });