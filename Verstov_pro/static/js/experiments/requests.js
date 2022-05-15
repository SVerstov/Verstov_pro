       function copyText() {

            /* Copy text into clipboard */
            navigator.clipboard.writeText
            ("{{ SITE_URL }}");
            document.getElementById("copy-btn")
                .innerHTML = 'Скопировано!';
        }

        function sendRequest(csrf) {


            // var xhr = new XMLHttpRequest;
            // xhr.open('GET', 'request/');
            // xhr.send();

            fetch('request/', {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrf,
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
            });

        }