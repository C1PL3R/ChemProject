document.getElementById("registerForm").addEventListener("submit", function (e) {
    e.preventDefault();

    var username = document.getElementById("username").value;
    var phone = document.getElementById("phone").value;
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    var first_name = document.getElementById("first_name").value;
    var last_name = document.getElementById("last_name").value;
    const messageDiv = document.getElementById("contact-message");

    messageDiv.textContent = "";
    messageDiv.style.display = "flex";

    axios.post(window.location.origin + "/auth-post/", {
        "username": username,
        "phone": phone,
        "password": password,
        "email": email,
        "first_name": first_name,
        "last_name": last_name
    }, {
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Content-Type": "application/json"
        }
    })
        .then(function (response) {
            if (response.data.redirect_url) {
                window.location.href = response.data.redirect_url;
            }
        })
        .catch(function (error) {
            const msg = error.response?.data?.error || "Сталася помилка!";
            messageDiv.textContent = msg;
            messageDiv.style.display = "flex";
            messageDiv.style.color = "red";
        });
});

document.getElementById("phone").addEventListener("input", function () {
    const phoneInput = document.getElementById("phone");
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