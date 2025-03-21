document.addEventListener('DOMContentLoaded', function() {
    const userImportForm = document.getElementById('user-import-form');
    const loginForm = document.getElementById('login-form');

    if (userImportForm) {
        userImportForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Perform form validation and submission logic here
            const formData = new FormData(userImportForm);
            // Example: Send data to the server using fetch
            fetch('/import-users', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Handle response data
                alert(data.message);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            // Perform login validation and submission logic here
            const formData = new FormData(loginForm);
            fetch('/login', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/dashboard';
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
});