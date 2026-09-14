document$.subscribe(function() {
    document.querySelectorAll('.sl-steps[start]').forEach(function(el) {
        var start = parseInt(el.getAttribute('start'), 10);
        if (!isNaN(start)) {
            el.style.setProperty('--sl-steps-start', start - 1);
        }
    });

});
