# 1. Taban İmaj: Hafif Node.js ortamı
FROM node:20-alpine

# 2. Konteyner içi çalışma dizini
WORKDIR /app

# 3. Bağımlılık dosyasını kopyala
COPY package*.json ./

# 4. Bağımlılıkları kur
RUN npm install

# 5. Kalan frontend kodlarını kopyala
COPY . .

# 6. Dışa açılan port
EXPOSE 3000

# 7. Başlatma komutu
CMD ["npm", "start"]
