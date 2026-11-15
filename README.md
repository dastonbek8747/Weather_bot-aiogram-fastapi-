# 🌤 Weather Bot (aiogram + FastAPI)

Ob-havo ma'lumotlarini beruvchi Telegram bot va shu ma'lumotlarni API orqali taqdim etuvchi **FastAPI** servisi.

---

## ✨ Imkoniyatlar

- 🌤 **Bugungi ob-havo** va **7 kunlik prognoz**
- 🌍 **Har qanday shahar** nomi bo'yicha qidiruv
- 🌐 **Ko'p tilli:** `deep_translator` orqali tarjima
- 🎨 **Emoji ikonkalar:** ob-havo holatiga mos
- 🔌 **REST API:** `/day/` va `/week/` endpointlari

---

## 🛠 Texnologiyalar

| Texnologiya | Maqsad |
|---|---|
| **Python 3.10+** | Asosiy til |
| **aiogram 3.x** | Telegram bot |
| **FastAPI** | REST API |
| **httpx / requests** | OpenWeatherMap API |
| **deep_translator** | Tarjima |

---

## ⚙️ O'rnatish

```bash
git clone https://github.com/dastonbek8747/Weather_bot-aiogram-fastapi-.git
cd Weather_bot-aiogram-fastapi-
python -m venv venv
source venv/bin/activate

# Bot
pip install -r bot/requirements.txt
# API
pip install -r fastapi/requirements.txt
```

`.env` fayl yarating:

```env
BOT_TOKEN=123456:ABC...
WEATHER_API=<openweathermap_api_key>
BASE_URL=https://api.openweathermap.org/data/2.5
```

> 🔒 `.env` git'ga qo'shilmaydi.

---

## ▶️ Ishga tushirish

**Telegram bot:**

```bash
cd bot && python main.py
```

**FastAPI servisi:**

```bash
cd fastapi && python main.py
# yoki: uvicorn main:app --host 0.0.0.0 --port 8000
```

API hujjati: `http://localhost:8000/docs`

---

## 📁 Loyiha tuzilishi

```
Weather_bot-aiogram-fastapi-/
├── bot/
│   ├── main.py          # Bot ishga tushirish
│   ├── handlers.py      # Handler'lar
│   └── requirements.txt
└── fastapi/
    ├── main.py          # FastAPI app
    ├── get_weather.py   # Ob-havo logikasi
    └── requirements.txt
```

---

## 📄 Litsenziya

Litsenziya ko'rsatilmagan.
