document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.querySelector('.nav');
    const buttons = document.querySelector('.button');

    if (!toggle || !nav) {
        return;
    }

    toggle.addEventListener('click', () => {
        nav.classList.toggle('active');
        if (buttons) {
            buttons.classList.toggle('active');
        }
        toggle.classList.toggle('active');
    });
});
