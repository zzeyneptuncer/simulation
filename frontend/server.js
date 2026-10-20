const express = require("express");
const axios = require("axios");
const path = require("path");

const app = express();
const PORT = 3000;
const API_URL = process.env.API_URL || "http://api:8000";

app.use(express.static(path.join(__dirname, "public")));

// Python API'den durum çeken uç nokta
app.get("/api/system-status", async (req, res) => {
  try {
    const response = await axios.get(`${API_URL}/`);
    res.json(response.data);
  } catch (error) {
    res.status(500).json({
      mesaj: "Python API'ye ulaşılamadı",
      hata: error.message
    });
  }
});

// Redis sayacını tetikleyen uç nokta
app.get("/api/hit-cache", async (req, res) => {
  try {
    const response = await axios.get(`${API_URL}/cache-test`);
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ hata: error.message });
  }
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Frontend sunucusu ${PORT} portunda çalışıyor`);
});
