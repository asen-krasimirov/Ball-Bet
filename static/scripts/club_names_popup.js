const mainElements = Array.from(document.getElementsByClassName('slider'));
const imageElements = Array.from(document.querySelectorAll('.future-match img'));

mainElements.forEach(
    slider => slider.addEventListener('mouseover', (event) => {
        const target = event.target;
        if (target.tagName !== 'IMG') return;

        const clubNameElement = target.nextElementSibling;

        let x = event.pageX;
        let y = event.pageY;

        clubNameElement.style.left = x + 'px';
        clubNameElement.style.top = y + 'px';

        clubNameElement.classList.toggle('show');

        target.addEventListener('mouseout', onMouseout);

        function onMouseout() {
            clubNameElement.classList.toggle('show');
            target.removeEventListener('mouseout', onMouseout);
        }
    })
);
