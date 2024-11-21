from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Присоединиться', callback_data='join')],
        [InlineKeyboardButton(text='🔎 Подробнее о канале', callback_data='about_channel')],
        [InlineKeyboardButton(text='💬 Задать вопрос', url='https://t.me/fixer_support')]
    ]
)

about_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Присоединиться', callback_data='join')],
        [InlineKeyboardButton(text='💬 Задать вопрос', url='https://t.me/fixer_support')],
        [InlineKeyboardButton(text='❮ Назад', callback_data='back')]
    ]
)

join = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅ Получить доступ', url='https://t.me/tribute/app?startapp=sjwC')],
        [InlineKeyboardButton(text='💬 Задать вопрос', url='https://t.me/fixer_support')],
        [InlineKeyboardButton(text='🔎 Подробнее о канале', callback_data='about_channel')],
        [InlineKeyboardButton(text='❮ Назад', callback_data='back')]
    ]
)
