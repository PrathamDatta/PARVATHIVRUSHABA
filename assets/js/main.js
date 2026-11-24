/* Parvathi Vrushabha HR Solution LLP — site interactions (vanilla JS, no dependencies) */
(function () {
  'use strict';
  var d = document, w = window;
  var reduce = w.matchMedia && w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || d).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); };

  /* ---- header, progress bar, back-to-top ---- */
  var header = $('.site-header'), bar = $('.progress'), top = $('.to-top');
  var ticking = false;
  function onScroll() {
    var y = w.scrollY || d.documentElement.scrollTop;
    var h = d.documentElement.scrollHeight - w.innerHeight;
    if (bar) bar.style.setProperty('--sp', h > 0 ? (y / h).toFixed(4) : 0);
    if (header) header.classList.toggle('scrolled', y > 12);
    if (top) top.classList.toggle('show', y > 700);
    $$('.steps').forEach(updateSteps);
    $$('[data-parallax]').forEach(function (el) {
      if (reduce) return;
      var r = el.getBoundingClientRect();
      var k = parseFloat(el.getAttribute('data-parallax')) || .1;
      el.style.translate = '0 ' + ((r.top + r.height / 2 - w.innerHeight / 2) * -k).toFixed(1) + 'px';
    });
    ticking = false;
  }
  w.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  if (top) top.addEventListener('click', function () { w.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' }); });

  /* ---- mobile nav ---- */
  var burger = $('.burger'), nav = $('#site-nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var o = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', o);
      burger.setAttribute('aria-label', o ? 'Close menu' : 'Open menu');
    });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { burger.click(); burger.focus(); } });
    $$('a', nav).forEach(function (a) { a.addEventListener('click', function () { if (nav.classList.contains('open')) burger.click(); }); });
  }

  /* ---- reveal on scroll ---- */
  var io = 'IntersectionObserver' in w ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('in');
      if (e.target.hasAttribute('data-count')) countUp(e.target);
      io.unobserve(e.target);
    });
  }, { threshold: .15, rootMargin: '0px 0px -6% 0px' }) : null;
  $$('[data-reveal], .tier, .ring-card, .reg, .clock, [data-count]').forEach(function (el) {
    if (io) io.observe(el); else { el.classList.add('in'); if (el.hasAttribute('data-count')) countUp(el); }
  });

  /* ---- counters ---- */
  function countUp(el) {
    var end = parseInt(el.getAttribute('data-count'), 10), suf = el.getAttribute('data-suffix') || '';
    if (reduce || isNaN(end)) { el.textContent = end + suf; return; }
    var t0 = null, dur = 1600;
    function f(t) {
      if (!t0) t0 = t;
      var p = Math.min((t - t0) / dur, 1), e = 1 - Math.pow(1 - p, 4);
      el.textContent = Math.round(end * e) + suf;
      if (p < 1) requestAnimationFrame(f);
    }
    requestAnimationFrame(f);
  }

  /* ---- rotating headline words ---- */
  $$('[data-rotate]').forEach(function (el) {
    var words = el.getAttribute('data-rotate').split('|'), i = 0, c = 0, del = false;
    if (reduce) { el.textContent = words[0]; return; }
    (function tick() {
      var word = words[i];
      c += del ? -1 : 1;
      el.textContent = word.slice(0, c);
      var wait = del ? 45 : 95;
      if (!del && c === word.length) { wait = 1700; del = true; }
      else if (del && c === 0) { del = false; i = (i + 1) % words.length; wait = 350; }
      setTimeout(tick, wait);
    })();
  });

  /* ---- card spotlight + tilt ---- */
  $$('.card, .info, .tile').forEach(function (c) {
    c.addEventListener('pointermove', function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });
  if (!reduce && w.matchMedia('(hover: hover)').matches) {
    $$('[data-tilt]').forEach(function (c) {
      c.addEventListener('pointermove', function (e) {
        var r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        c.style.transform = 'perspective(900px) rotateX(' + (-y * 7).toFixed(2) + 'deg) rotateY(' + (x * 9).toFixed(2) + 'deg) translateY(-6px)';
      });
      c.addEventListener('pointerleave', function () { c.style.transform = ''; });
    });
    $$('[data-magnetic]').forEach(function (b) {
      b.addEventListener('pointermove', function (e) {
        var r = b.getBoundingClientRect();
        b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * .18).toFixed(1) + 'px,' + ((e.clientY - r.top - r.height / 2) * .28).toFixed(1) + 'px)';
      });
      b.addEventListener('pointerleave', function () { b.style.transform = ''; });
    });
  }

  /* ---- process steps: line fills as the section scrolls into view ---- */
  function updateSteps(s) {
    var r = s.getBoundingClientRect(), vh = w.innerHeight;
    var p = Math.min(1, Math.max(0, (vh * .78 - r.top) / (r.height + vh * .2)));
    if (reduce) p = 1;
    s.style.setProperty('--p', p.toFixed(3));
    var kids = $$('.step', s);
    kids.forEach(function (k, i) { k.classList.toggle('on', p >= (i + .4) / kids.length * .98 || p >= 1); });
  }

  /* ---- lifecycle wheel ---- */
  $$('.wheel-wrap').forEach(function (wrap) {
    var nodes = $$('.wnode', wrap), panes = $$('.pane', wrap), hub = $('.hub strong', wrap), auto = null, n = nodes.length;
    function show(i, user) {
      nodes.forEach(function (x, j) { x.classList.toggle('on', i === j); x.setAttribute('aria-pressed', i === j); });
      panes.forEach(function (p, j) { p.classList.toggle('on', i === j); });
      if (hub) hub.textContent = nodes[i].getAttribute('data-hub');
      wrap.dataset.i = i;
      if (user && auto) { clearInterval(auto); auto = null; }
    }
    nodes.forEach(function (nd, i) {
      var ang = (i / n) * 2 * Math.PI - Math.PI / 2;
      nd.style.left = (50 + 40 * Math.cos(ang)).toFixed(2) + '%';
      nd.style.top = (50 + 40 * Math.sin(ang)).toFixed(2) + '%';
      nd.addEventListener('click', function () { show(i, true); });
      nd.addEventListener('mouseenter', function () { show(i, true); });
      nd.addEventListener('focus', function () { show(i, true); });
    });
    show(0);
    if (!reduce) auto = setInterval(function () { show(((+wrap.dataset.i || 0) + 1) % n); }, 3800);
  });

  /* ---- tabs ---- */
  $$('[data-tabs]').forEach(function (g) {
    var tabs = $$('[role="tab"]', g), panels = $$('[role="tabpanel"]', g);
    function sel(i) {
      tabs.forEach(function (t, j) { t.setAttribute('aria-selected', i === j); t.tabIndex = i === j ? 0 : -1; });
      panels.forEach(function (p, j) { p.classList.toggle('on', i === j); });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { sel(i); });
      t.addEventListener('keydown', function (e) {
        var k = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (k) { var j = (i + k + tabs.length) % tabs.length; sel(j); tabs[j].focus(); }
      });
    });
    sel(0);
  });

  /* ---- value cards: tap to flip on touch ---- */
  $$('.vcard').forEach(function (v) { v.addEventListener('click', function () { v.classList.toggle('flip'); }); });

  /* ---- subnav highlight ---- */
  var sub = $$('.subnav a');
  if (sub.length && io) {
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) sub.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id); });
      });
    }, { rootMargin: '-35% 0px -55% 0px' });
    sub.forEach(function (a) { var t = $(a.getAttribute('href')); if (t) so.observe(t); });
  }

  /* ---- contact form: opens WhatsApp or email with the message prefilled (no server needed) ---- */
  $$('form[data-contact]').forEach(function (f) {
    function compose() {
      var v = function (n) { var e = f.elements[n]; return e ? (e.value || '').trim() : ''; };
      return 'Hello Parvathi Vrushabha HR Solution,\n\n' +
        'Name: ' + v('name') + '\nCompany: ' + v('company') + '\nPhone: ' + v('phone') + '\nEmail: ' + v('email') +
        '\nInterested in: ' + v('service') + '\n\n' + v('message');
    }
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!f.reportValidity()) return;
      var kind = (e.submitter && e.submitter.value) || 'wa';
      if (kind === 'mail') {
        w.location.href = 'mailto:info@parvathivrushabha.com?cc=hrd@parvathivrushabha.com&subject=' + encodeURIComponent('Enquiry: ' + (f.elements.service.value || 'HR services')) + '&body=' + encodeURIComponent(compose());
      } else {
        w.open('https://wa.me/917026199239?text=' + encodeURIComponent(compose()), '_blank', 'noopener');
      }
    });
  });

  /* ---- prefill contact form from ?service= ---- */
  var qs = new URLSearchParams(w.location.search).get('service'), sel = $('#f-service');
  if (qs && sel) { $$('option', sel).some(function (o) { if (o.textContent.toLowerCase().indexOf(qs.toLowerCase().split(' ')[0]) === 0) { sel.value = o.textContent; return true; } }); }

  onScroll();
})();
