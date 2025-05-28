function sendNotification(title, text) {
    if (Notification.permission === "granted") {
        new Notification(title, {
            body: text,
            icon: "https://cdn-icons-png.flaticon.com/512/545/545705.png"
        });
    } else if (Notification.permission !== "denied") {
        Notification.requestPermission().then(permission => {
            if (permission === "granted") {
                new Notification(title, {
                    body: text,
                    icon: "https://cdn-icons-png.flaticon.com/512/545/545705.png"
                });
            } else {
                alert("Сповіщення заборонені 😞");
            }
        });
    } else {
        alert("Сповіщення заборонені 😞");
    }
}


document.addEventListener('DOMContentLoaded', function () {
    var burgerMenu = document.getElementById('burger-menu');
    var overlay = document.getElementById('menu');
    var body = document.body;

    burgerMenu.addEventListener('click', function () {
        this.classList.toggle('close');
        overlay.classList.toggle('overlay');

        // Додаємо або прибираємо клас no-scroll для блокування скролінгу
        if (overlay.classList.contains('overlay')) {
            body.classList.add('no-scroll');
        } else {
            body.classList.remove('no-scroll');
        }
    });
});

window.addEventListener('blur', () => {
    this.document.title = 'Ви покинули сайт ChemVisualizer!';
});

window.addEventListener('focus', () => {
    var title = document.getElementById('title');
    this.document.title = title.innerText;
});

function SendDataPost(url, data, successCallback) {
    axios.post(window.location.origin + url, {
        data
    }, {
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        }
    })
        .then(function (response) {
            hasUnsavedChanges = false;
            Swal.fire({
                title: successCallback,
                icon: 'success',
                confirmButtonText: 'ОК'
            }).then(() => {
                CloseSettings();
                window.location.reload();
            });

        })
        .catch(function (error) {
            const errorMessage = error.response?.data?.error || "Сталася помилка!";
            Swal.fire({
                title: 'Помилка',
                text: errorMessage,
                icon: 'error',
                confirmButtonText: 'OK'
            });
        });
}
