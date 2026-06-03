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
