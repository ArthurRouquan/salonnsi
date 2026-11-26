document$.subscribe(function() {
    document.querySelectorAll('.sl-steps[start]').forEach(function(el) {
        var start = parseInt(el.getAttribute('start'), 10);
        if (!isNaN(start)) {
            el.style.setProperty('--sl-steps-start', start - 1);
        }
    });

});

/* Schéma interactif « avancer vers la cible » (projets/agario.md).
   Usage : bloc `/// html | div.schema-vecteur`. On fait glisser la cellule
   ou la cible ; une glissière règle la vitesse v.
   Les textes sont en LaTeX (classe arithmatex), composés par MathJax. */
function creerSchemaVecteur(conteneur) {
    var NS = 'http://www.w3.org/2000/svg';
    var LARGEUR = 480, HAUTEUR = 260;
    var ECHELLE = 40;                         // pixels SVG pour une unité
    var R = 10;                               // rayon de la cellule (px SVG)
    var cellule = { x: 3, y: 1.25 };          // en unités
    var cible = { x: 6, y: 5.25 };
    var vitesse = 2;                          // en unités par image

    // Pointes de flèche : triangle plat et allongé (longueur, largeur)
    var POINTES = {
        gris: [12, 6],
        vitesse: [12, 6],
        unite: [14, 7]
    };

    function el(nom, attributs, parent) {
        var e = document.createElementNS(NS, nom);
        for (var cle in attributs) e.setAttribute(cle, attributs[cle]);
        (parent || svg).appendChild(e);
        return e;
    }
    function poser(e, attributs) {
        for (var cle in attributs) e.setAttribute(cle, attributs[cle]);
    }
    function afficher(e, visible) {
        e.style.display = visible ? '' : 'none';
    }
    // Nombre en LaTeX, avec une virgule décimale
    function nombre(x, n) {
        var t = x.toFixed(n);
        if (parseFloat(t) === 0) t = (0).toFixed(n);
        return t.replace('.', '{,}');
    }
    function maths(tex) {
        return '<span class="arithmatex">\\(' + tex + '\\)</span>';
    }

    var figure = document.createElement('div');
    figure.className = 'sv-figure';
    conteneur.appendChild(figure);

    var svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', '0 0 ' + LARGEUR + ' ' + HAUTEUR);
    figure.appendChild(svg);

    // Étiquette LaTeX posée par-dessus le SVG ; ancre : 'centre', 'gauche' ou 'droite'
    function etiquette(tex, classe) {
        var e = document.createElement('div');
        e.className = 'sv-etiquette ' + (classe || '');
        e.innerHTML = maths(tex);
        figure.appendChild(e);
        return e;
    }
    // Légende en texte normal, dans la police du site
    function legende(texte, classe) {
        var e = document.createElement('div');
        e.className = 'sv-etiquette sv-legende ' + (classe || '');
        e.textContent = texte;
        figure.appendChild(e);
        return e;
    }
    // Place une étiquette à une distance « marge » du point (x, y), dans la
    // direction (ox, oy), en l'ancrant par son bord le plus proche
    function placerAutour(e, x, y, ox, oy, marge) {
        var ancre = ox > 0.35 ? 'gauche' : ox < -0.35 ? 'droite' : 'centre';
        var my = ancre === 'centre' ? marge + 4 : marge;
        placer(e, x + ox * marge, y + oy * my, ancre);
    }
    function placer(e, x, y, ancre) {
        e.style.left = (100 * x / LARGEUR) + '%';
        e.style.top = (100 * y / HAUTEUR) + '%';
        e.style.transform = ancre === 'gauche' ? 'translate(0, -50%)'
            : ancre === 'droite' ? 'translate(-100%, -50%)' : 'translate(-50%, -50%)';
    }

    // La base de chaque pointe est posée au bout du trait : un vecteur
    // de (x1, y1) à (x2, y2) s'arrête donc une longueur de pointe avant.
    var defs = el('defs', {});
    Object.keys(POINTES).forEach(function (nom) {
        var longueur = POINTES[nom][0], largeur = POINTES[nom][1];
        var marqueur = el('marker', {
            id: 'sv-fleche-' + nom, viewBox: '0 0 ' + longueur + ' ' + largeur,
            refX: 0.5, refY: largeur / 2, markerUnits: 'userSpaceOnUse',
            markerWidth: longueur, markerHeight: largeur, orient: 'auto'
        }, defs);
        el('path', { d: 'M0,0 L' + longueur + ',' + (largeur / 2) + ' L0,' + largeur + ' Z',
            'class': 'sv-tete-' + nom }, marqueur);
    });
    function fleche(ligne, nom, x1, y1, x2, y2) {
        var ex = x2 - x1, ey = y2 - y1;
        var l = Math.sqrt(ex * ex + ey * ey);
        var k = l > 0 ? (l - POINTES[nom][0]) / l : 0;
        poser(ligne, { x1: x1, y1: y1, x2: x1 + ex * k, y2: y1 + ey * k });
        afficher(ligne, l > POINTES[nom][0] + 2);
    }

    // Grille de points, tout au fond (un point toutes les demi-unités)
    var PAS_GRILLE = ECHELLE / 2;
    var motif = el('pattern', { id: 'sv-grille', width: PAS_GRILLE, height: PAS_GRILLE,
        patternUnits: 'userSpaceOnUse', x: 0, y: 0 }, defs);
    el('circle', { cx: PAS_GRILLE / 2, cy: PAS_GRILLE / 2, r: 1, 'class': 'sv-point-grille' }, motif);
    el('rect', { x: 0, y: 0, width: LARGEUR, height: HAUTEUR, fill: 'url(#sv-grille)' });

    // Ordre de dessin : de l'arrière vers l'avant
    var fantome = el('circle', { r: R, 'class': 'sv-fantome' });
    var traitDx = el('line', { 'class': 'sv-pointille' });
    var traitDy = el('line', { 'class': 'sv-pointille' });
    var angle = el('path', { 'class': 'sv-angle' });
    var vecteur = el('line', { 'class': 'sv-vecteur', 'marker-end': 'url(#sv-fleche-gris)' });
    var disque = el('circle', { r: R, 'class': 'sv-cellule' });
    var deplacement = el('line', { 'class': 'sv-deplacement', 'marker-end': 'url(#sv-fleche-vitesse)' });
    var unite = el('line', { 'class': 'sv-unite', 'marker-end': 'url(#sv-fleche-unite)' });
    var curseur = el('path', { 'class': 'sv-cible' });
    var texteDx = etiquette('dx');
    var texteDy = etiquette('dy');
    var texteD = etiquette('d');
    var texteUn = etiquette('1', 'sv-bleu');
    var texteV = etiquette('v', 'sv-orange');
    var legendeCellule = legende('Cellule', 'sv-legende-cellule');
    var legendeCible = legende('Cible', 'sv-legende-cible');
    var legendeNouvelle = legende('Nouvelle position', 'sv-legende-nouvelle');

    var controle = document.createElement('div');
    controle.className = 'sv-controle';
    controle.innerHTML = '<label>Vitesse ' + maths('v') + '</label>' +
        '<input type="range" min="0.5" max="3" step="0.1" value="' + vitesse + '">';
    conteneur.appendChild(controle);
    var glissiere = controle.querySelector('input');
    glissiere.addEventListener('input', function () {
        vitesse = parseFloat(glissiere.value);
        dessiner();
    });

    var lecture = document.createElement('div');
    lecture.className = 'sv-lecture';
    conteneur.appendChild(lecture);

    // Composition MathJax de la ligne de calcul : une seule à la fois,
    // toujours avec le dernier contenu demandé.
    var contenu = '', occupe = false, enAttente = false;
    function composer() {
        if (!(window.MathJax && MathJax.startup && MathJax.startup.promise && MathJax.typesetPromise)) {
            lecture.innerHTML = contenu;
            return;
        }
        if (occupe) { enAttente = true; return; }
        occupe = true;
        MathJax.startup.promise.then(function () {
            MathJax.typesetClear([lecture]);
            lecture.innerHTML = contenu;
            return MathJax.typesetPromise([lecture]);
        }).catch(function () {}).then(function () {
            occupe = false;
            if (enAttente) { enAttente = false; composer(); }
        });
    }

    function dessiner() {
        var cx = cellule.x * ECHELLE, cy = cellule.y * ECHELLE;
        var tx = cible.x * ECHELLE, ty = cible.y * ECHELLE;
        var dx = cible.x - cellule.x, dy = cible.y - cellule.y;
        var d = Math.sqrt(dx * dx + dy * dy);
        var sx = dx >= 0 ? 1 : -1, sy = dy >= 0 ? 1 : -1;

        poser(disque, { cx: cx, cy: cy });
        // Cible : curseur de souris, pointe exactement sur le point visé
        poser(curseur, { d: 'M' + tx + ',' + ty + 'l0,17 l4.5,-4.5 l3,6.5 l2.5,-1 l-3,-6.5 l6,0 Z' });

        // Composantes dx et dy, et angle droit
        poser(traitDx, { x1: cx, y1: cy, x2: tx, y2: cy });
        poser(traitDy, { x1: tx, y1: cy, x2: tx, y2: ty });
        poser(angle, { d: 'M' + (tx - sx * 8) + ',' + cy + 'v' + (sy * 8) + 'h' + (sx * 8) });
        afficher(angle, Math.abs(dx) * ECHELLE > 16 && Math.abs(dy) * ECHELLE > 16);
        placer(texteDx, (cx + tx) / 2, cy - sy * 14, 'centre');
        afficher(texteDx, Math.abs(dx) * ECHELLE > 30);
        placer(texteDy, tx + sx * 9, (cy + ty) / 2, sx > 0 ? 'gauche' : 'droite');
        afficher(texteDy, Math.abs(dy) * ECHELLE > 24);

        // Légendes « cellule » et « cible » : dans le prolongement du vecteur,
        // chacune du côté opposé à l'autre point (au-dessus / en dessous si d = 0)
        var lx = d > 0 ? dx / d : 0, ly = d > 0 ? dy / d : 1;
        placerAutour(legendeCellule, cx, cy, -lx, -ly, R + 5);
        // (plus loin quand la légende tomberait sur le corps du curseur, en bas à droite)
        placerAutour(legendeCible, tx, ty, lx, ly, lx > -0.3 && ly > -0.3 ? 24 : 10);

        var visible = d >= vitesse;
        [vecteur, unite, deplacement, texteUn, texteV, legendeNouvelle].forEach(function (e) { afficher(e, visible); });
        afficher(texteD, visible && d * ECHELLE > 60);
        if (!visible) {
            poser(fantome, { cx: tx, cy: ty });
            contenu = '<div>' + maths('v = ' + nombre(vitesse, 1)) + '</div><div class="sv-avertissement">' +
                maths('d < v') + '&nbsp;: la cellule se place directement sur la cible.</div>';
            composer();
            return;
        }
        var ux = dx / d, uy = dy / d;
        // Normale qui pointe à l'opposé de l'angle droit, pour l'étiquette d
        var nx = -uy, ny = ux;
        if (nx * (tx - (cx + tx) / 2) + ny * (cy - (cy + ty) / 2) > 0) { nx = -nx; ny = -ny; }

        // Vecteur vers la cible, arrêté juste avant la pointe du curseur
        var fin = d * ECHELLE - 4;
        fleche(vecteur, 'gris', cx + ux * R, cy + uy * R, cx + ux * fin, cy + uy * fin);
        placer(texteD, (cx + tx) / 2 + nx * 14, (cy + ty) / 2 + ny * 14, 'centre');

        // Vecteur v × unité (derrière), vecteur unité (devant) et nouvelle position
        var pas = vitesse * ECHELLE;
        fleche(deplacement, 'vitesse', cx, cy, cx + ux * pas, cy + uy * pas);
        fleche(unite, 'unite', cx, cy, cx + ux * ECHELLE, cy + uy * ECHELLE);
        poser(fantome, { cx: cx + ux * pas, cy: cy + uy * pas });

        // « 1 » sous le vecteur unité
        var mx = cx + ux * ECHELLE / 2, my = cy + uy * ECHELLE / 2;
        var bx = -uy, by = ux;
        if (by < 0 || (by === 0 && bx < 0)) { bx = -bx; by = -by; }
        placer(texteUn, mx + bx * 16, my + by * 16, 'centre');

        // « v » sous la partie visible du vecteur vitesse (au-delà du vecteur unité)
        var vx = cx + ux * (ECHELLE + pas) / 2, vy = cy + uy * (ECHELLE + pas) / 2;
        placer(texteV, vx + bx * 16, vy + by * 16, 'centre');
        afficher(texteV, pas - ECHELLE > 24);

        // « nouvelle position » : à côté du disque pâle, du côté opposé au « 1 »
        var gx = cx + ux * pas, gy = cy + uy * pas;
        placerAutour(legendeNouvelle, gx, gy, -bx, -by, R + 5);

        var u = '\\left(\\frac{dx}{d}\\,;\\,\\frac{dy}{d}\\right)';
        contenu =
            '<div>' + maths('dx = ' + nombre(dx, 1) + ' \\quad dy = ' + nombre(dy, 1) + ' \\quad d = ' + nombre(d, 1) +
                  ' \\quad v = ' + nombre(vitesse, 1)) + '</div>' +
            '<div class="sv-ligne">' +
            '<span class="sv-bleu"><span class="sv-puce"></span>' +
            maths(u + ' = (' + nombre(ux, 2) + '\\,;\\,' + nombre(uy, 2) + ')') + '</span>' +
            '<span class="sv-orange"><span class="sv-puce"></span>' +
            maths('v \\times ' + u + ' = (' + nombre(vitesse * ux, 2) + '\\,;\\,' + nombre(vitesse * uy, 2) + ')') + '</span>' +
            '</div>';
        composer();
    }

    // Glisser-déposer de la cellule ou de la cible
    var SAISIE = 18;                          // rayon de saisie (px SVG)
    var saisi = null;

    function position(evenement) {
        var point = svg.createSVGPoint();
        point.x = evenement.clientX;
        point.y = evenement.clientY;
        var p = point.matrixTransform(svg.getScreenCTM().inverse());
        return { x: p.x / ECHELLE, y: p.y / ECHELLE };
    }
    function sous(p) {
        function proche(q) {
            var ex = (q.x - p.x) * ECHELLE, ey = (q.y - p.y) * ECHELLE;
            return ex * ex + ey * ey <= SAISIE * SAISIE;
        }
        // On attrape le curseur par son corps (en bas à droite de la pointe) ;
        // la cible passe devant la cellule
        if (proche({ x: cible.x + 5 / ECHELLE, y: cible.y + 8 / ECHELLE })) return cible;
        if (proche(cellule)) return cellule;
        return null;
    }

    svg.addEventListener('pointerdown', function (evenement) {
        saisi = sous(position(evenement));
        if (!saisi) return;
        evenement.preventDefault();
        try { svg.setPointerCapture(evenement.pointerId); } catch (e) {}
        svg.style.cursor = 'grabbing';
    });
    svg.addEventListener('pointermove', function (evenement) {
        var p = position(evenement);
        if (!saisi) {
            svg.style.cursor = sous(p) ? 'grab' : '';
            return;
        }
        saisi.x = Math.max(0.3, Math.min(LARGEUR / ECHELLE - 0.3, p.x));
        saisi.y = Math.max(0.3, Math.min(HAUTEUR / ECHELLE - 0.3, p.y));
        dessiner();
    });
    function lacher(evenement) {
        if (!saisi) return;
        saisi = null;
        svg.style.cursor = sous(position(evenement)) ? 'grab' : '';
    }
    svg.addEventListener('pointerup', lacher);
    svg.addEventListener('pointercancel', lacher);
    dessiner();
}

document$.subscribe(function () {
    document.querySelectorAll('.schema-vecteur').forEach(function (conteneur) {
        if (conteneur.dataset.pret) return;
        conteneur.dataset.pret = 'oui';
        creerSchemaVecteur(conteneur);
    });
});
