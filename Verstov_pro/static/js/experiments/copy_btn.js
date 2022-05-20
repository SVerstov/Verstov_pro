       function copyText() {

            /* Copy text into clipboard */
            navigator.clipboard.writeText
            (document.getElementById('textbox').value);
            document.getElementById("copy-btn")
                .innerHTML = 'Скопировано!';
        }
