function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var createNewDocBtn = document.getElementById("createNewDocBtn")

if (createNewDocBtn) {
    document.getElementById("createNewDocBtn").addEventListener("click", function () {
        axios.post(window.location.origin + "/document/create-new-doc/", {
        }, {
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                "Content-Type": "application/json"
            }
        })
            .then(function (response) {
                Swal.fire({
                    title: 'Документ створено',
                    text: "Зайдіть на сторінку, де є список ваших документів, і ви там його побачите! Або почекайте ще трішки часу сторінка сама перезавантажиться!",
                    icon: 'success',
                    confirmButtonText: 'ОК'
                }).then(() => {
                    var doc = response.data.doc;

                    var document_ui = document.createElement("div");
                    document_ui.classList.add("doc");

                    var title = document.createElement("a");
                    title.innerText = doc.title;
                    title.href = window.location.origin + "/document/" + doc.id;
                    document_ui.appendChild(title);

                    var docs = document.getElementsByClassName("docs");
                    docs[docs.length - 1].appendChild(document_ui);
                    
                    setTimeout(() => {
                        window.location.href = window.location.origin + "/document/" + doc.id;
                    }, 2000);
                });

            })
            .catch(function (error) {
                const callback = error.response?.data?.error || "Сталася помилка!";
            });
    });
}

document.addEventListener('DOMContentLoaded', function () {
    var documentInput = document.getElementById('docEditor');
    var documentNameInput = document.getElementById('documentNameInput');
    var documentId = document.getElementById('DocumentId');

    if (documentId && documentId.innerText) { // Check if documentId exists and has a value
        const protocol = window.location.protocol === 'https:' ? 'wss://' : 'ws://';
        const chatSocket = new WebSocket(
            protocol + window.location.host + '/ws/document/' + documentId.innerText + '/'
        );

        chatSocket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            documentInput.value = data.text;
            if (data.document_name) {
                documentNameInput.value = data.document_name;
            }
        };

        chatSocket.onerror = function (error) {
            console.error('WebSocket Error: ', error);
        };

        let timeoutId;
        const delay = 5 * 1000;

        documentInput.addEventListener('input', () => {
            clearTimeout(timeoutId);

            timeoutId = setTimeout(() => {
                var text = documentInput.innerHTML;
                console.log(text)
                chatSocket.send(JSON.stringify({
                    'text': text,
                }));
            }, delay);
        });

        documentNameInput.addEventListener('input', () => {
            clearTimeout(timeoutId);

            timeoutId = setTimeout(() => {
                var title = documentNameInput.value;
                chatSocket.send(JSON.stringify({
                    'title': title,
                }));
            }, delay);
        });


        window.addEventListener('beforeunload', () => {
            chatSocket.close();
        });
    } else {
        console.warn("Document ID not found or empty. Skipping WebSocket connection.");
    }
});