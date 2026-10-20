# 1. Taban İmaj: Hafif bir Python ortamı
FROM python:3.11-slim

# 2. Konteyner içinde çalışacağımız dizin
WORKDIR /app

# 3. Bağımlılıklar listesini kopyala
COPY requirements.txt .

# 4. Kütüphaneleri kur (Cache optimizasyonu için kodlardan önce kurulur)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Kalan tüm uygulama kodlarını kopyala
COPY . .

# 6. Dışarıya açılacak port bilgisi (Dokümantasyon amaçlı)
EXPOSE 8000

# 7. Konteyner çalıştığında çalışacak başlatma komutu
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
