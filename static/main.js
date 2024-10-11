
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Active nav item highlighting
    const currentLocation = location.pathname;
    const navItems = document.querySelectorAll('.nav-link');
    navItems.forEach(item => {
        if (item.getAttribute('href') === currentLocation) {
            item.classList.add('active');
        }
    });

    // Form submission handling (for contact form)
    const contactForm = document.querySelector('#contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Here you would typically send the form data to a server
            // For now, we'll just show an alert
            alert('Thank you for your message! We will get back to you soon.');
            contactForm.reset();
        });
    }

    // Responsive image loading
    function loadResponsiveImages() {
        const images = document.querySelectorAll('img[data-src]');
        images.forEach(img => {
            img.setAttribute('src', img.getAttribute('data-src'));
            img.onload = function() {
                img.removeAttribute('data-src');
            };
        });
    }

    // Call the function on page load and resize
    loadResponsiveImages();
    window.addEventListener('resize', loadResponsiveImages);
});