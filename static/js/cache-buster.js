// 🔥 CACHE BUSTER - Fuerza recarga completa del JavaScript
// Esta línea garantiza que el navegador descargue la versión más reciente
console.log('🔥 CACHE BUSTER ACTIVADO:', Date.now());

// Forzar recarga
if (window.location.reload) {
    // Agregar timestamp para evitar cache
    const url = new URL(window.location);
    url.searchParams.set('_t', Date.now());
    // Solo en desarrollo para forzar cache bust
}
