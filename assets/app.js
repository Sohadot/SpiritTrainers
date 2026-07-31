/* SpiritTrainers — motion is slow, meaning-bearing, and optional.
   No external dependencies. Everything degrades to legible static text. */
(function () {
  "use strict";

  var reduce = window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* -------- reveal-on-scroll (used site-wide) -------- */
  function initReveals() {
    var els = document.querySelectorAll(".reveal");
    if (!els.length) return;
    if (reduce || !("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.35, rootMargin: "0px 0px -8% 0px" });
    els.forEach(function (el) { io.observe(el); });
  }

  /* -------- hero: SPIRIT disperses, settles, becomes a question -------- */
  function splitLetters(el) {
    var text = el.getAttribute("data-word") || el.textContent;
    el.textContent = "";
    var frag = document.createDocumentFragment();
    for (var i = 0; i < text.length; i++) {
      var s = document.createElement("span");
      s.className = "ltr";
      s.textContent = text[i];
      frag.appendChild(s);
    }
    el.appendChild(frag);
    return el.querySelectorAll(".ltr");
  }

  function scatter(letters) {
    letters.forEach(function (l) {
      var dx = (Math.random() * 2 - 1) * 42;
      var dy = (Math.random() * 2 - 1) * 30;
      var rot = (Math.random() * 2 - 1) * 22;
      l.style.transform =
        "translate(" + dx + "vw," + dy + "vh) rotate(" + rot + "deg)";
      l.style.opacity = "0.06";
    });
  }
  function settle(letters) {
    letters.forEach(function (l) {
      l.style.transform = "none";
      l.style.opacity = "1";
    });
  }

  function initHero() {
    var hero = document.querySelector("[data-hero]");
    if (!hero) return;

    var spirit = hero.querySelector('[data-word="SPIRIT"]');
    var trained = hero.querySelector('[data-word="TRAINED"]');
    var q = hero.querySelector(".hero-q");
    var enter = hero.querySelector(".enter");
    var cue = hero.querySelector(".scroll-cue");

    // Reduced motion: keep only the question + entry, drop the choreography.
    if (reduce) {
      if (spirit) { spirit.classList.add("persist", "show"); }
      if (q) q.classList.add("show");
      if (enter) enter.classList.add("show");
      if (cue) cue.classList.add("show");
      return;
    }

    var sLetters = spirit ? splitLetters(spirit) : [];
    var tLetters = trained ? splitLetters(trained) : [];
    if (spirit) scatter(sLetters);
    if (trained) scatter(tLetters);

    var t = [];
    function at(ms, fn) { t.push(setTimeout(fn, ms)); }

    // 1. SPIRIT fades in scattered, then converges.
    at(300, function () { spirit && spirit.classList.add("show"); });
    at(700, function () { settle(sLetters); });
    // 2. It disperses again.
    at(3200, function () { scatter(sLetters); });
    at(3700, function () { spirit && spirit.classList.remove("show"); });
    // 3. TRAINED converges.
    at(4200, function () {
      if (trained) { trained.classList.add("show"); settle(tLetters); }
    });
    at(6600, function () { trained && trained.classList.remove("show"); });
    // 4. The question remains.
    at(7200, function () { q && q.classList.add("show"); });
    at(8000, function () {
      enter && enter.classList.add("show");
      cue && cue.classList.add("show");
    });

    // Safety: if the tab is backgrounded, don't leave it blank.
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) {
        t.forEach(clearTimeout);
        settle(sLetters); settle(tLetters);
        spirit && spirit.classList.remove("show");
        trained && trained.classList.remove("show");
        q && q.classList.add("show");
        enter && enter.classList.add("show");
        cue && cue.classList.add("show");
      }
    }, { once: true });
  }

  /* -------- render data-driven sections (progressive enhancement) -------- */
  function renderData() {
    var mounts = document.querySelectorAll("[data-render]");
    if (!mounts.length) return;
    mounts.forEach(function (mount) {
      var src = mount.getAttribute("data-src");
      var kind = mount.getAttribute("data-render");
      fetch(src).then(function (r) { return r.json(); }).then(function (data) {
        if (kind === "buyers") renderBuyers(mount, data);
      }).catch(function () { /* static fallback content stays */ });
    });
  }

  function renderBuyers(mount, data) {
    if (!data || !data.archetypes) return;
    var html = "";
    data.archetypes.forEach(function (a) {
      html +=
        '<div class="cell reveal">' +
        '<h3>' + esc(a.label) + "</h3>" +
        "<p>" + esc(cap(a.buys_because)) + ".</p>" +
        '<span class="tag">Fears losing: ' + esc(a.fears_losing) + "</span>" +
        "</div>";
    });
    mount.innerHTML = html;
    initReveals();
  }

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }
  function cap(s) { s = String(s); return s.charAt(0).toUpperCase() + s.slice(1); }

  /* -------- boot -------- */
  function boot() {
    initHero();
    initReveals();
    renderData();
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
