from aiogram import Router

from app import keyboards as kb
from app import texts as tx
from aiogram import F
from aiogram.types import (
    Message,
    CallbackQuery,
    FSInputFile
)
from aiogram.filters import CommandStart

router = Router()

first_message_ids = {}


@router.message(CommandStart())
async def cmd_start(message: Message):
    # URL фотографии
    photo_url = "https://disk.yandex.ru/i/bU2z404HlRMlew"
    vnote_path = "../fixer_vnote.mp4"

    video_note = FSInputFile(vnote_path)

    await message.answer_video_note(video_note=video_note)

    # Отправляем фотографию с текстом и клавиатурой
    sent_message = await message.answer_photo(
        photo=photo_url,  # Указываем URL фотографии
        caption=tx.start,  # Добавляем текст к фотографии
        reply_markup=kb.start,  # Добавляем клавиатуру
        parse_mode="HTML"  # Указываем форматирование текста
    )
    first_message_ids[message.chat.id] = sent_message.message_id


@router.callback_query(F.data == "join")
async def join(callback: CallbackQuery):
    if callback.message.message_id != first_message_ids.get(callback.message.chat.id):
        await callback.message.delete()
    await callback.answer()
    await callback.message.answer(tx.join, reply_markup=kb.join, parse_mode="HTML")


@router.callback_query(F.data == "about_channel")
async def aboutchannel(callback: CallbackQuery):
    if callback.message.message_id != first_message_ids.get(callback.message.chat.id):
        await callback.message.delete()
    await callback.answer()
    await callback.message.answer(tx.about_channel, reply_markup=kb.about_channel, parse_mode="HTML")


@router.callback_query(F.data == "back")
async def aboutchannel(callback: CallbackQuery):
    if callback.message.message_id != first_message_ids.get(callback.message.chat.id):
        await callback.message.delete()
    await callback.answer()
    await callback.message.answer(tx.start, reply_markup=kb.start, parse_mode="HTML")
