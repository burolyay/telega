import logging

from aiogram import Bot, Dispatcher, executor, types
from tugurmalar import mars_shop_inline,mars_menu,mars_profile_inline

API_TOKEN = '6287800146:AAHrDuh9OmfYwRrlan5V7P093yYsEt6P1vo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup=mars_menu)

@dp.message_handler(text="Мои монеты")
async def echo(message: types.Message):
    await message.answer("У вас 10000 монет")


@dp.message_handler(text="Space shop")
async def echo(message: types.Message):
    await message.answer("Выберите приз",reply_markup=mars_shop_inline)


@dp.message_handler(text="Профиль")
async def echo(message: types.Message):
    await message.answer("Имя: Saidburxon Фамилия: Akbarov Язык: ru Телефон: 909880452 Город: Uzbekiston Учебный центр: YUNUSABAD",reply_markup=mars_profile_inline)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Any text")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)