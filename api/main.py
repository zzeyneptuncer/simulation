import os
from fastapi import FastAPI
import psycopg2
import redis

app = FastAPI(title="Stajyer API Servisi")

# Docker ağındaki diğer servislerin isimleri ve portları
PG_HOST = os.getenv("POSTGRES_HOST", "postgres-db")
PG_USER = os.getenv("POSTGRES_USER", "stajyer")
PG_PASSWORD = os.getenv("POSTGRES_PASSWORD", "guclusifre123")
PG_DB = os.getenv("POSTGRES_DB", "staj_db")
REDIS_HOST = os.getenv("REDIS_HOST", "redis-cache")

@app.get("/")
def home():
    # PostgreSQL Bağlantı Testi
    pg_status = "Bilinmiyor"
    try:
        conn = psycopg2.connect(
            host=PG_HOST,
            user=PG_USER,
            password=PG_PASSWORD,
            dbname=PG_DB,
            connect_timeout=3
        )
        conn.close()
        pg_status = "Bağlantı Başarılı! ✅"
    except Exception as e:
        pg_status = f"Bağlantı Hatası: {str(e)} ❌"

    # Redis Bağlantı Testi
    redis_status = "Bilinmiyor"
    try:
        r = redis.Redis(host=REDIS_HOST, port=6379, socket_timeout=3)
        r.ping()
        redis_status = "Bağlantı Başarılı! ✅"
    except Exception as e:
        redis_status = f"Bağlantı Hatası: {str(e)} ❌"

    return {
        "mesaj": "Python API Servisi Çalışıyor!",
        "postgresql_durumu": pg_status,
        "redis_durumu": redis_status
    }

@app.get("/cache-test")
def cache_test():
    r = redis.Redis(host=REDIS_HOST, port=6379)
    # Ziyaretçi sayacını 1 artır
    sayac = r.incr("ziyaretci_sayisi")
    return {"mesaj": "Redis Cache Çalışıyor", "ziyaretci_sayisi": sayac}
