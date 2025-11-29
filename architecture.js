/**
 * Travel Itinerary Agent Architecture
 * 
 * User → Itinerary Generation Agent (NaviTrip)
 *      → Output: Draft itinerary + daftar destinasi
 * 
 * Backend → Map Data Agent
 *         → Places API (tool)
 *         → Distance Matrix API (tool)
 *         → Directions API (opsional)
 * 
 * → Output: Data jarak & durasi yang sudah terstruktur
 * 
 * Refinement Agent (Finalizer)
 * → Menggabungkan semuanya jadi itinerary final
 * → Memhasilkan link maps
 * → Memberi tips + estimasi biaya
 * 
 * Frontend → Tampilkan ke user
 *         → Interaksi user (edit, simpan, bagikan)
 */

module.exports = {
  // Architecture defined above
};

