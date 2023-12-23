from aiogram import executor, types, Bot, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import webbrowser
import pyautogui
import os

kb = [
    [types.KeyboardButton(text="Закрити попередню вкладку")],
    [types.KeyboardButton(text="Програмування")],
    [types.KeyboardButton(text="Музика")],
    [types.KeyboardButton(text="Пауза")],
    [types.KeyboardButton(text=">>")],
    [types.KeyboardButton(text="<<")],
    [types.KeyboardButton(text="Закрити файл")],
    [types.KeyboardButton(text="+")],
    [types.KeyboardButton(text="-")],
    [types.KeyboardButton(text="Пошук в гуглі")],
    [types.KeyboardButton(text="↑")],
    [types.KeyboardButton(text="↓")],
    [types.KeyboardButton(text="Enter")]
]

keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

TOKEN = "6706937927:AAHmtThOd8UEr9ITKQTKZViCt4Yy6TZAOsE"
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["st"
                              "art"])
async def greet_and_show(msg: types.Message):
    await msg.answer("Запускаюсь...",reply_markup=keyboard)
    await msg.delete()


@dp.message_handler()
async def open_google(msg: types.Message):
    if msg.text == "Закрити попередню вкладку":
        pyautogui.hotkey('ctrl', 'w')
        await msg.delete()
    elif msg.text == "Програмування":
        os.startfile(r"C:\Program Files\JetBrains\PyCharm 2023.2.5\bin\pycharm64.exe")
        await msg.delete()
    elif msg.text == "Музика":
        os.startfile(r"C:\Users\user\Desktop\Music")
        await msg.delete()
    elif msg.text == "Пауза":
        pyautogui.hotkey("ctrl", "p")
        await msg.delete()
    elif msg.text == ">>":
        pyautogui.hotkey("ctrl", "right")
        await msg.delete()
    elif msg.text == "<<":
        pyautogui.hotkey("ctrl", "left")
        await msg.delete()
    elif msg.text == "Закрити файл":
        pyautogui.hotkey("alt", "f4")
        await msg.delete()
    elif msg.text == "+":
        pyautogui.hotkey("volumeup")
        await msg.delete()
    elif msg.text == "-":
        pyautogui.hotkey("volumedown")
        await msg.delete()
    elif msg.text == "↑":
        pyautogui.hotkey("up")
        await msg.delete()
    elif msg.text == "↓":
        pyautogui.hotkey("down")
        await msg.delete()
    elif msg.text == "Enter":
        pyautogui.press("enter")
        await msg.delete()

    elif msg.text == "Пошук в гуглі":
        webbrowser.open("https://www.google.com.ua")
        await msg.delete()

    elif msg.text:
        pyautogui.write(msg.text)

if __name__ == "__main__":
    executor.start_polling(dp)
