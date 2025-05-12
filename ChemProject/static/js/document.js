var documentInput  = document.getElementById('documentTextArea');

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
