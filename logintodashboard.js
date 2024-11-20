document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('login-form');
    
    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent default form submission
        
        // You can add validation or authentication logic here
        
        // If successful, redirect to the dashboard
        window.location.href = 'dashboard.html';
    });
});
