from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from deep_translator import GoogleTranslator
import httpx

router = Router()

# Emoji mapping for weather icons
ICON_EMOJI = {
    "01d": "☀️", "01n": "🌕",
    "02d": "🌤️", "02n": "☁️",
    "03d": "☁️", "03n": "☁️",
    "04d": "☁️", "04n": "☁️",
    "09d": "🌧️", "09n": "🌧️",
    "10d": "🌦️", "10n": "🌧️",
    "11d": "🌩️", "11n": "🌩️",
    "13d": "❄️", "13n": "❄️",
    "50d": "🌫️", "50n": "🌫️"
}


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "🌤 Bu bot orqali *bugungi* va *7 kunlik ob-havo* ma'lumotlarini olishingiz mumkin.\n"
        "📍 Shunchaki shahar nomini yuboring!",
        parse_mode="Markdown"
    )


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "🆘 *Yordam*\n\n"
        "1️⃣ /day - Bugungi ob-havo\n"
        "2️⃣ /week - 7 kunlik ob-havo\n"
        "📍 Yoki shunchaki shahar nomini kiriting.",
        parse_mode="Markdown"
    )


@router.message(Command("about"))
async def about_handler(message: Message):
    await message.answer("👨‍💻 Bot yaratuvchisi: @doston_sultonov")


@router.message()
async def handle_city(message: Message):
    city_name = message.text.strip()

    async with httpx.AsyncClient() as client:
        # Bugungi ob-havo
        resp_day = await client.post("http://fastapi:8000/day/", json={"name": city_name})
        data_day = resp_day.json()

        # 7 kunlik ob-havo
        resp_week = await client.post("http://fastapi:8000/week/", json={"name": city_name})
        data_week = resp_week.json()

    # Bugungi ob-havo tarjimasi
    desc_en = data_day.get("description", "").lower()
    desc_uz = GoogleTranslator(source='en', target='uz').translate(desc_en)
    icon_today = ICON_EMOJI.get(data_day.get("icon", ""), "🌡️")

    today_text = (
        f"📍 *{city_name.title()}* shahri uchun *bugungi ob-havo*:\n\n"
        f"{icon_today} *{data_day['description'].capitalize()}* ({desc_uz})\n"
        f"🌡 Harorat: {data_day['temperature']}°C\n"
        f"💧 Namlik: {data_day['humidity']}%\n"
        f"💨 Shamol tezligi: {data_day['wind_speed']} m/s\n"
    )

    # 7 kunlik ob-havo matni
    week_text = "\n📅 *7 kunlik ob-havo:*"
    for day in data_week["forecast"]:
        icon = ICON_EMOJI.get(day.get("icon", ""), "🌤️")
        desc_en = day.get("description", "").lower()
        desc_uz = GoogleTranslator(source='en', target='uz').translate(desc_en)
        week_text += (
            f"\n\n📆 {day['date']}\n"
            f"{icon} *{day['description'].capitalize()}* ({desc_uz})\n"
            f"🌡 Harorat: {day['min_temp']}°C dan {day['max_temp']}°C gacha\n"
        )

    await message.answer(today_text + week_text, parse_mode="Markdown")
