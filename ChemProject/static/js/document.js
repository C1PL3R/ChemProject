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
                var callback = response.data.doc_id;
            })
            .catch(function (error) {
                const callback = error.response?.data?.error || "Сталася помилка!";
            });
    });
}

var documentInput = document.getElementById('documentTextArea');

var documentId = document.getElementById('DocumentId');

if (documentId) {
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/document/' + documentId.innerText + '/'
    );

    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        documentInput.value = data.text;
    };

    documentInput.addEventListener('input', () => {
        var text = documentInput.value;
        chatSocket.send(JSON.stringify({
            'text': text,
        }));
    });
}


