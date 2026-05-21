document$.subscribe(() => {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    const prevBtn = document.querySelector('.nav.prev');
    const nextBtn = document.querySelector('.nav.next');
    const slideshow = document.querySelector('.slideshow');

    if (!slideshow || slides.length === 0) return; // Safeguard

    slideshow.addEventListener('mouseenter', () => {
        document.addEventListener('keydown', handleKey);
    });
    slideshow.addEventListener('mouseleave', () => {
        document.removeEventListener('keydown', handleKey);
    });

    function handleKey(event) {
        if (event.key === 'ArrowRight') nextSlide();
        if (event.key === 'ArrowLeft') prevSlide();
    }

    // Find index of active slide
    let currentIndex = Array.from(slides).findIndex(slide => slide.classList.contains('active'));
    if (currentIndex === -1) currentIndex = 0;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('active', i === index);
        });

        dots.forEach((dot, i) => {
            dot.classList.toggle('active', i === index);
        });

        currentIndex = index;
    }

    function nextSlide() {
        const newIndex = (currentIndex + 1) % slides.length;
        showSlide(newIndex);
    }

    function prevSlide() {
        const newIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(newIndex);
    }

    // Event listeners
    nextBtn?.addEventListener('click', nextSlide);
    prevBtn?.addEventListener('click', prevSlide);

    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => showSlide(index));
    });
});