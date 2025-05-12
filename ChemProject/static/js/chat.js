var chatId = document.getElementById('chat_id');
var myId = document.getElementById('myId');

if (chatId) {
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + chatId.innerText + '/'
    );
    chatSocket.onmessage = function (e) {
        const data = JSON.parse(e.data);
        console.log(myId.innerText);
        const messagesList = document.getElementById('chat-messages-list');

        const newMessage = document.createElement('div');

        if (parseInt(myId.innerText) === parseInt(data.sender_id) && parseInt(myId.innerText) !== parseInt(data.receiver_id)) {
            newMessage.className = 'message-item-receiver';
        } else {
            newMessage.className = 'message-item-sender';
        }
        const newMessageText = document.createElement('p');
        newMessageText.innerText = data.message;

        newMessage.appendChild(newMessageText);
        messagesList.appendChild(newMessage);
    };

    function SendMessage(receiver, sender) {
        document.getElementById('chat-message-submit').onclick = function (e) {
            const input = document.getElementById('messageText');
            var message = input.value.trim();

            if (message !== '') {
                chatSocket.send(JSON.stringify({
                    'message': message,
                    'receiver_id': receiver,
                    'sender_id': sender
                }));
            }

            input.value = '';

            const chatList = document.getElementById("chat-messages-list");
            if (chatList) {
                setTimeout(() => {
                    chatList.scrollTo({
                        top: chatList.scrollHeight,
                        behavior: "smooth"
                    });
                }, 100);
            }
        };
    }
}



document.addEventListener("DOMContentLoaded", function () {
    const addBtn = document.getElementById("add_contact");
    const closeBtn = document.getElementById("close");
    const container = document.getElementById("add-contact-container");

    if (addBtn && container) {
        addBtn.addEventListener("click", function () {
            container.style.display = "flex";
        });
    }

    if (closeBtn && container) {
        closeBtn.addEventListener("click", function () {
            container.style.display = "none";
        });
    }
});

document.getElementById("close").addEventListener("click", function () {
    const addContactContainer = document.getElementById("add-contact-container");

    if (addContactContainer.style.display === "none" || addContactContainer.style.display === "") {
        addContactContainer.style.display = "flex";  // Відображаємо контейнер
    } else {
        addContactContainer.style.display = "none";  // Ховаємо контейнер
    }
});


const messageText = document.getElementById('messageText');


if (messageText) {
    messageText.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            document.getElementById("chat-message-submit").click();
        }
    });

    messageText.addEventListener('input', () => {
        messageText.style.height = 'auto';

        const lineHeight = parseFloat(getComputedStyle(messageText).lineHeight);
        const maxHeight = lineHeight * 5;

        if (messageText.scrollHeight <= maxHeight) {
            messageText.style.height = `${messageText.scrollHeight}px`;
            messageText.style.overflowY = 'hidden';
        } else {
            messageText.style.height = `${maxHeight}px`;
            messageText.style.overflowY = 'scroll';
        }
    });
}


document.getElementById("addContactForm").addEventListener("submit", function (e) {
    e.preventDefault();

    var username = document.getElementById("username").value;
    var phone_number = document.getElementById("phone_number").value;
    const messageDiv = document.getElementById("contact-message");

    messageDiv.textContent = "";
    messageDiv.style.display = "flex";

    axios.post(window.location.origin + "/chat/add_contact/", {
        "username": username,
        "phone_number": phone_number,
    }, {
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        }
    })
        .then(function (response) {
            messageDiv.textContent = response.data.success;
            messageDiv.style.display = "flex";
            messageDiv.style.color = "green";
            window.location.reload();
        })
        .catch(function (error) {
            const msg = error.response?.data?.error || "Сталася помилка!";
            messageDiv.textContent = msg;
            messageDiv.style.display = "flex";
            messageDiv.style.color = "red";
        });
});

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


document.getElementById("settingsChatBtn").addEventListener("click", function () {
    const settingsWrapper = document.getElementById("settings-wrapper");
    const settingsContainer = document.getElementById("settings-chat-container");

    if (settingsWrapper.style.display === "none" || settingsWrapper.style.display === "") {
        settingsWrapper.style.display = "flex";  // Відображаємо контейнер
        settingsContainer.style.display = "flex";  // Відображаємо контейнер
    } else {
        settingsWrapper.style.display = "none";  // Ховаємо контейнер
        settingsContainer.style.display = "none";  // Ховаємо контейнер
    }
});

document.getElementById("phone_number").addEventListener("input", function () {
    const phoneInput = document.getElementById("phone_number");
    const formattedNumber = formatUAPhone(phoneInput.value);
    phoneInput.value = formattedNumber;
});

function formatUAPhone(phoneNumber) {
    const cleaned = phoneNumber.replace(/\D/g, '');

    if (cleaned.length !== 10 || !/^0\d{9}$/.test(cleaned)) {
        return phoneNumber;
    }

    return `+38 (${cleaned.slice(0, 3)}) ${cleaned.slice(3, 6)}-${cleaned.slice(6, 8)}-${cleaned.slice(8)}`;
}



function CleanHistory(chat_id) {
    const messageList = document.getElementById("chat-messages-list");
    messageList.textContent = "";
    axios.post("/clean-history/", {
        "chat_id": chat_id,
    }, {
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        }
    })
        .then(function (response) {
            console.log(response.data.success);
        })
        .catch(function (error) {
            console.error("Error deleting chat history:", error);
        });
}

function DeleteChat(chat_id) {
    axios.post("/delete-chat/", {
        "chat_id": chat_id,
    }, {
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        }
    })
        .then(function (response) {
            console.log(response.data.success);
        })
        .catch(function (error) {
            console.error("Error deleting chat history:", error);
        });
}