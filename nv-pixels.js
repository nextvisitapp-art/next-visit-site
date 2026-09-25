// Meta Pixel + TikTok Pixel for hello.next-visit.app.
//
// Both pixels are OFF until an id is set below. With an empty id nothing
// loads: no script, no network request, no cookie, no console error. So this
// file can ship ahead of the ids and switches on the moment they are pasted.
//
//   Meta:   Events Manager -> Data sources -> your Pixel -> the numeric id
//   TikTok: Ads Manager -> Assets -> Events -> Web Events -> the pixel code id
//
// What fires here (the request, 25 Sep 2026):
//   - PageView on every page of this site (both pixels)
//   - ViewContent on the landing page only (both pixels)
// CompleteRegistration fires on next-visit.app when someone actually finishes
// creating or joining a space on the web - the planner is account-free, so
// that is where sign-up really completes. See src/lib/marketingPixels.js in
// the couples repo, and the fbclid/ttclid hand-off in go's index.html that
// lets that event attribute back to the ad click.
//
// Disclosed in privacy.html clause 6. Anything added here needs that clause
// kept honest.
(function () {
  var IDS = {
    meta: '',    // e.g. '1234567890123456'
    tiktok: '',  // e.g. 'D1ABCDEFGHIJKLMNOP'
  };
  // Local smoke test only: lets the Playwright check inject ids on localhost
  // without touching the real values above. Never honoured in production.
  try {
    if (/^(localhost|127\.0\.0\.1)$/.test(location.hostname) && window.NV_PIXELS_OVERRIDE) IDS = window.NV_PIXELS_OVERRIDE;
  } catch (e) { /* ignore */ }

  var isLanding = location.pathname === '/' || location.pathname === '/index.html';

  if (IDS.meta) {
    /* eslint-disable */
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    /* eslint-enable */
    window.fbq('init', IDS.meta);
    window.fbq('track', 'PageView');
    if (isLanding) window.fbq('track', 'ViewContent', { content_name: 'Landing page', content_category: 'marketing' });
  }

  if (IDS.tiktok) {
    /* eslint-disable */
    !function (w, d, t) { w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie","holdConsent","revokeConsent","grantConsent"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var r="https://analytics.tiktok.com/i18n/pixel/events.js",o=n&&n.partner;ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=r,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};n=document.createElement("script");n.type="text/javascript",n.async=!0,n.src=r+"?sdkid="+e+"&lib="+t;e=document.getElementsByTagName("script")[0];e.parentNode.insertBefore(n,e)}; }(window, document, 'ttq');
    /* eslint-enable */
    window.ttq.load(IDS.tiktok);
    window.ttq.page();
    if (isLanding) window.ttq.track('ViewContent', { content_name: 'Landing page', content_category: 'marketing' });
  }
})();
