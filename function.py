from aiogram import Bot, types
from aiogram.types import Message
import instaloader

async def start_answer(message: Message, bot: Bot):
    await message.answer("Assalomu Aleykum botimga xush kelibsiz\n\nBu bot sizga instagramdagi userlar haqida malumotlar beradi\n\nMisol: avazbek.dev")


async def help_answer(message: Message, bot: Bot):
    await message.answer("Sizga qanday yordam bera olaman")


async def insta(message: Message, bot: Bot):
    L = instaloader.Instaloader()
    p = message.text

    profile = instaloader.Profile.from_username(L.context, p)

    await message.answer(f"""
    Obunachilar: {profile.followers}
    Obunalar: {profile.followees}
    Postlar: {profile.mediacount}
    Views: {profile.followed_by_viewer}
    """)
