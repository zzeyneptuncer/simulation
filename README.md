# 🚀 4-Tier Containerized Microservices Architecture

Bu proje; **PostgreSQL**, **Redis**, **Python (FastAPI)** ve **Node.js** servislerini içeren, Docker ve Docker Compose ile izole bir ağ üzerinde orkestre edilen mikroservis tabanlı bir mimaridir.

---

## 🏛️ Mimari Şema

```
[ İstemci / Tarayıcı ]
         │ (Port 3000)
         ▼
[ 1. Frontend: Node.js (Express) ]
         │ (HTTP Dahili Ağ)
         ▼
[ 2. API: Python (FastAPI) ] (Port 8000)
    ├── (Port 5432) ──> [ 3. Veritabanı: PostgreSQL 16 (Alpine) ] (Kalıcı Volume)
    └── (Port 6379) ──> [ 4. Önbellek: Redis (Alpine) ] (Kalıcı Volume)
```

---

## 📦 Bileşenler ve Özellikler

1. **PostgreSQL (`postgres:16-alpine`):**
   - İlişkisel kalıcı veri saklama.
   - `postgres_data` adlı Docker Volume ile veri kalıcılığı (persistence).
2. **Redis (`redis:alpine`):**
   - RAM tabanlı ultra-hızlı önbellek ve sayaç yönetimi (`appendonly yes`).
   - `redis_data` adlı Docker Volume ile veri kalıcılığı.
3. **Python API (FastAPI):**
   - Özel `Dockerfile` ile optimize katman önbelleği (layer caching).
   - PostgreSQL ve Redis ile asenkron / hızlı bağlantı testi ve sayaç endpoints.
4. **Node.js Frontend (Express & Vanilla JS):**
   - Kullanıcı dostu canlı sistem izleme paneli.
   - Servislerin durumunu (sağlık kontrolü) yeşil/kırmızı göstergelerle raporlar.

---

## 🚀 Kurulum ve Çalıştırma

Projeyi bilgisayarınızda tek bir komutla ayağa kaldırmak için:

```bash
docker compose up -d --build
```

### Servislere Erişim:
- **Frontend Paneli:** [http://localhost:3000](http://localhost:3000)
- **Python API:** [http://localhost:8000](http://localhost:8000)
- **FastAPI Otomatik Swagger Dokümantasyonu:** [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🛠️ Yönetim ve Hata Ayıklama Komutları

```bash
# Servislerin çalışma durumunu kontrol et
docker compose ps

# Canlı logları izle
docker compose logs -f

# Sistemi durdur
docker compose stop

# Sistemi kapat ve temizle (veriler volume'da kalır)
docker compose down
```
