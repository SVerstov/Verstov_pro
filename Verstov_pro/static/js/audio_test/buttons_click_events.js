const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


        function sendRequest(csrftoken) {


            // var xhr = new XMLHttpRequest;
            // xhr.open('GET', 'request/');
            // xhr.send();

            fetch('request/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
            });

        }