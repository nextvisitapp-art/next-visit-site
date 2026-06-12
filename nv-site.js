// Next Visit · site pages — light/dark toggle. Navy is the default look (set
// pre-paint by the inline bootstrap in each page's <head>); this only wires the
// header toggle button and keeps the theme-color meta in step. The choice
// persists under the shared `nv_appearance` key.
(function () {
  function apply() {
    var dark = document.documentElement.getAttribute("data-theme") !== "light";
    var btn = document.getElementById("themeToggle");
    if (btn) {
      btn.innerHTML = dark
        ? '<i class="ph ph-sun" aria-hidden="true"></i>'
        : '<i class="ph ph-moon" aria-hidden="true"></i>';
      btn.setAttribute("aria-label", dark ? "Switch to light mode" : "Switch to dark mode");
    }
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", dark ? "#0e2240" : "#fdf0f0");
  }
  window.nvToggleTheme = function () {
    var next = document.documentElement.getAttribute("data-theme") === "light" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", next);
    try { localStorage.setItem("nv_appearance", next); } catch (e) {}
    apply();
  };
  if (document.readyState !== "loading") apply();
  else document.addEventListener("DOMContentLoaded", apply, { once: true });
})();

// ── Store badges ───────────────────────────────────────────────────────
// Single source of truth for the App Store / Play links. To go live:
//   1. set `live: true` on a platform
//   2. for iOS, paste the real App Store URL (apps.apple.com/app/id<APPLE_ID>)
// Until live, the badge renders dimmed with a "Coming soon" note and the
// hero's "open it in your browser" link carries the load.
(function () {
  var STORE = {
    ios: {
      live: false,
      url: "https://apps.apple.com/app/idREPLACE_WITH_APPLE_ID"
    },
    android: {
      live: false, // flip true once the Play listing is published
      url: "https://play.google.com/store/apps/details?id=app.nextvisit.couples"
    }
  };

  // Inline SVG marks (fill is set by CSS to #fff).
  var APPLE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.05 12.54c-.02-2.06 1.68-3.05 1.76-3.1-0.96-1.4-2.46-1.6-2.99-1.62-1.27-.13-2.48.75-3.13.75-.64 0-1.64-.73-2.7-.71-1.39.02-2.67.81-3.38 2.05-1.44 2.5-.37 6.2 1.04 8.23.69.99 1.51 2.1 2.58 2.06 1.04-.04 1.43-.67 2.69-.67 1.25 0 1.61.67 2.7.65 1.12-.02 1.83-1.01 2.51-2.01.79-1.15 1.12-2.27 1.13-2.33-.02-.01-2.17-.83-2.19-3.29zM15.0 6.91c.57-.69.95-1.65.85-2.61-.82.03-1.81.55-2.4 1.24-.53.6-.99 1.58-.86 2.51.91.07 1.84-.46 2.41-1.14z"/></svg>';
  var PLAY  = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3.6 2.3c-.25.24-.4.6-.4 1.07v17.26c0 .47.15.83.4 1.07l.06.06 9.67-9.67v-.23L3.66 2.24l-.06.06zm12.97 12.97l-3.22-3.22 3.22-3.22 3.8 2.16c1.09.62 1.09 1.64 0 2.26l-3.8 2.16zm-.34.34l-3.22-3.22-9.67 9.67c.36.38.95.43 1.62.05l11.27-6.5zm-11.27-15.2c-.67-.38-1.26-.33-1.62.05l9.67 9.67 3.22-3.22L5.0.41z"/></svg>';

  function badge(kind, conf) {
    var soon = !conf.live;
    var a = document.createElement("a");
    a.className = "nv-store-badge" + (soon ? " is-soon" : "");
    a.href = soon ? "#get" : conf.url;
    if (!soon) { a.target = "_blank"; a.rel = "noopener"; }
    if (soon) { a.setAttribute("aria-disabled", "true"); }
    var isiOS = kind === "ios";
    a.setAttribute("aria-label", (isiOS ? "Download on the App Store" : "Get it on Google Play") + (soon ? " — coming soon" : ""));
    a.innerHTML = (isiOS ? APPLE : PLAY) +
      '<span class="nv-store-badge__txt">' +
        '<span class="nv-store-badge__sm">' + (isiOS ? "Download on the" : "Get it on") + '</span>' +
        '<span class="nv-store-badge__lg">' + (isiOS ? "App Store" : "Google Play") + '</span>' +
      '</span>';
    return a;
  }

  function render() {
    var hosts = document.querySelectorAll(".nv-stores");
    if (!hosts.length) return;
    var anySoon = !STORE.ios.live || !STORE.android.live;
    hosts.forEach(function (host) {
      host.innerHTML = "";
      host.appendChild(badge("ios", STORE.ios));
      host.appendChild(badge("android", STORE.android));
      if (anySoon) host.setAttribute("data-state", "soon");
      else host.removeAttribute("data-state");
    });
  }

  if (document.readyState !== "loading") render();
  else document.addEventListener("DOMContentLoaded", render, { once: true });
})();

// ── Landing choreography ───────────────────────────────────────────────
// Scroll reveals, the split-flap destination board, and a whisper of
// parallax on the hero phones. All of it bails under reduced-motion and
// no-ops on pages without the landing markup (legal/support).
(function () {
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function onReady(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn, { once: true });
  }

  onReady(function () {
    // Scroll reveals
    var revealEls = document.querySelectorAll(".reveal");
    if (revealEls.length) {
      if (reduced || !("IntersectionObserver" in window)) {
        revealEls.forEach(function (el) { el.classList.add("is-in"); });
      } else {
        var io = new IntersectionObserver(function (entries) {
          entries.forEach(function (e) {
            if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
          });
        }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
        revealEls.forEach(function (el) { io.observe(el); });
      }
    }

    // Split-flap destination board — cycles real next-stop ideas. Pads to a
    // fixed slot count so the board doesn't reflow between words.
    var board = document.getElementById("flapBoard");
    if (board) {
      var WORDS = ["LISBON", "TOKYO", "NEW YORK", "SANTORINI", "KYOTO", "BANFF", "PARIS", "QUEENSTOWN"];
      var SLOTS = 10;
      var tiles = [];
      for (var i = 0; i < SLOTS; i++) {
        var t = document.createElement("span");
        t.className = "board__tile";
        t.textContent = " ";
        board.appendChild(t);
        tiles.push(t);
      }
      var w = 0;
      function setWord(word) {
        var padTotal = SLOTS - word.length;
        var padL = Math.floor(padTotal / 2);
        var chars = [];
        for (var i = 0; i < SLOTS; i++) {
          var c = word[i - padL];
          chars.push(c === undefined ? " " : (c === " " ? " " : c));
        }
        tiles.forEach(function (tile, i) {
          var next = chars[i];
          if (tile.textContent === next) return;
          if (reduced) { tile.textContent = next; return; }
          setTimeout(function () {
            tile.classList.add("is-flipping");
            setTimeout(function () { tile.textContent = next; }, 170); // swap at mid-flip
            setTimeout(function () { tile.classList.remove("is-flipping"); }, 380);
          }, i * 45); // stagger left → right, like a real departure board
        });
      }
      setWord(WORDS[0]);
      if (!reduced) setInterval(function () { w = (w + 1) % WORDS.length; setWord(WORDS[w]); }, 3400);
    }

    // Hero phone parallax — tiny translate driven by scroll.
    var px = document.querySelectorAll("[data-parallax]");
    if (px.length && !reduced) {
      var ticking = false;
      function frame() {
        ticking = false;
        var y = window.scrollY || 0;
        px.forEach(function (el) {
          var f = parseFloat(el.getAttribute("data-parallax")) || 0;
          el.style.translate = "0 " + (y * f / 100) + "px";
        });
      }
      window.addEventListener("scroll", function () {
        if (!ticking) { ticking = true; requestAnimationFrame(frame); }
      }, { passive: true });
    }
  });
})();
