const CACHE_NAME = "4safety-cache-v4";
const urlsToCache = [
  "/favicon.ico",
  "/favicon.svg",
];

self.addEventListener("install", (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(async (cache) => {
      await Promise.allSettled(
        urlsToCache.map((url) => cache.add(url).catch((err) => console.warn(`[SW] Failed to cache ${url}:`, err)))
      );
    })
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((cacheName) => cacheName !== CACHE_NAME)
          .map((cacheName) => caches.delete(cacheName))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  // Ignora requisições não-GET (e.g. POST de formulários) e esquemas não-HTTP(S)
  if (event.request.method !== "GET" || !event.request.url.startsWith("http")) {
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }
      return fetch(event.request).catch((error) => {
        console.warn("[SW] Fetch failed; returning offline fallback if available", error);
        return cachedResponse || new Response("Offline", { status: 503, statusText: "Service Unavailable" });
      });
    })
  );
});

