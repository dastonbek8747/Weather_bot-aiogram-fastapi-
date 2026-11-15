# Weather Bot (aiogram + FastAPI)

Telegram bot orqali ob-havo ma'lumotlarini beruvchi mikroservislar to'plami.

## Arxitektura

- `bot/` — Telegram bot (aiogram). Foydalanuvchi so'rovlarini qabul qiladi.
- `fastapi/` — OpenWeatherMap API bilan ishlovchi REST servis.
- `docker-compose.yml` — ikkala servisni birga ishga tushiradi.

## O'rnatish va sozlash

1. `.env.example` dan nusxa oling:

   ```bash
   cp .env.example .env
   ```

2. `.env` faylida `BOT_TOKEN` va `WEATHER_API` kalitlarini to'ldiring.

3. Docker bilan ishga tushirish:

   ```bash
   docker compose up --build
   ```

## Muhim

`.env` faylini hech qachon GitHub'ga yuklamang — u `.gitignore`da. Kalitlar oshkor bo'lsa, darhol almashtiring.

## Litsenziya

MIT
