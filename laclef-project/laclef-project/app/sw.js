/* La Clef service worker — makes the app work offline once installed.
 *
 * Strategy: cache the app shell (the HTML + icons) on install, then serve
 * from cache first and fall back to the network. The live tutor's API calls
 * always go to the network (they're never cached). Bump CACHE_VERSION whenever
 * you change la-clef.html so users pick up the update.
 */
const CACHE_VERSION = "laclef-v1";
const SHELL = [
  "./la-clef.html",
  "./manifest.webmanifest",
  "./icon-192.png",
  "./icon-512.png",
  "./icon-maskable-512.png",
  "./apple-touch-icon.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(CACHE_VERSION).then((cache) => cache.addAll(SHELL)).then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_VERSION).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  // Never cache API calls (the live tutor) — always hit the network.
  if (req.url.includes("/v1/messages") || req.method !== "GET") {
    return; // let the browser handle it normally
  }
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req)
        .then((res) => {
          // cache same-origin successful responses for next time
          if (res && res.status === 200 && req.url.startsWith(self.location.origin)) {
            const copy = res.clone();
            caches.open(CACHE_VERSION).then((c) => c.put(req, copy));
          }
          return res;
        })
        .catch(() => cached); // offline and not cached -> nothing we can do
    })
  );
});
