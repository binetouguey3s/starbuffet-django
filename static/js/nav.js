// sert à gérer l'ouverture et la fermeture du menu de navigation sur les petits écrans
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

// explication du code en haut
// 1. On attend que le DOM soit complètement chargé avant d'exécuter le code
// 2. On sélectionne les éléments du DOM nécessaires : le bouton de menu, la navigation et les boutons
// 3. Si le bouton de menu ou la navigation n'existent pas, on arrête l'exécution du code
// 4. On ajoute un écouteur d'événement au bouton de menu pour détecter les clics
// 5. Lorsqu'on clique sur le bouton de menu, on bascule la classe "active" sur la navigation, les boutons et le bouton de menu lui-même pour afficher ou masquer le menu de navigation sur les petits écrans   