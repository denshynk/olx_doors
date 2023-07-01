import webbrowser
import pyautogui
import time
import datetime
import telebot
import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime
from LISTS import LIST_OF_UP1, LIST_TO_TOP, LIST_TO_PUSHUP7
from telebot import types
import clipboard
import keyboard
import tkinter as tk

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

if screen_width == 1920 and screen_height == 1080:
    address_bar_position = (400, 47)
    first_button = (1500, 970)
    second_button = (1500, 870)
    variable2 = "Другое значение для разрешения 1920x1080"
elif screen_width == 1366 and screen_height == 768:
    address_bar_position = (700, 53)
    first_button = (1150, 670)
    second_button = (1150, 670)


TOKEN = '6323579647:AAEwnkuMPpd8c4aIbZDLeFBC5loaGn6Tc_4'
CHAT_ID = -1001911928428
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['up1'])
def start_up1(message):
    LIST_OF_PARS = []
    link_to_parse = 'https://barbados.olx.ua'
    r = requests.get(link_to_parse)
    soup = BeautifulSoup(r.content, 'html.parser')
    elements = soup.find_all('div', {'class': 'css-1sw7q4x'})
    if elements:
        for element in elements:
            element_id = element.get('id')
            if element_id is not None:
                p_elements = element.find_all('p', class_='css-ki4ei7 er34gjf0')
                for p_element in p_elements:
                    extracted_text = p_element.get_text()
                    LIST_OF_PARS.append((extracted_text, int(element_id)))
    else:
        bot.reply_to(message, "Элементы не найдены.")

    sleep = 240
    message_of_start = f'\U0001F6AA Начинаю поднимать за 15 гривен с интервалом {sleep // 60} минут'
    bot.send_message(CHAT_ID, message_of_start)

    sum_of_road = 0
    sum_of_success = 0
    total = 0

    for i in range(len(LIST_OF_UP1)):
        link = LIST_OF_UP1[i]
        parsed_url = urllib.parse.urlparse(link)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        extracted_id = query_params.get('ad-id', [''])[0]
        for item in LIST_OF_PARS:
            if item[1] == int(extracted_id):
                doors_model = item[0]
        webbrowser.open_new(link)
        pyautogui.sleep(20)
        pyautogui.hotkey('f5')
        pyautogui.sleep(5)
        pyautogui.scroll(-2000)
        pyautogui.sleep(5)
        pyautogui.moveTo(second_button)
        pyautogui.sleep(5)
        pyautogui.click()
        pyautogui.sleep(5)
        pyautogui.moveTo(second_button)
        pyautogui.click()
        pyautogui.sleep(0.5)
        keyboard.press('ctrl')
        keyboard.press('w')
        pyautogui.sleep(0.5)
        keyboard.release('ctrl')
        keyboard.release('w')

        pyautogui.sleep(0.5)
        
        date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        total += 1
        message = f'\u2705 {total}.{doors_model} піднялися у топ!\n {date_time}'
        bot.send_message(CHAT_ID, message)
        sum_of_success += 1
        time.sleep(sleep)
        sum_of_road += 1

    message = f'\U0001F916 {sum_of_road} обработано'
    bot.send_message(CHAT_ID, message)
    message = f'\U0001F916 {sum_of_success} успешно оплаченно'
    bot.send_message(CHAT_ID, message)

@bot.message_handler(commands=['top all'])
def start_top_all(message):
    LIST_OF_PARS = []
    link_to_parse = 'https://barbados.olx.ua'
    r = requests.get(link_to_parse)
    soup = BeautifulSoup(r.content, 'html.parser')
    elements = soup.find_all('div', {'class': 'css-1sw7q4x'})
    if elements:
        for element in elements:
            element_id = element.get('id')
            if element_id is not None:
                p_elements = element.find_all('p', class_='css-ki4ei7 er34gjf0')
                for p_element in p_elements:
                    extracted_text = p_element.get_text()
                    LIST_OF_PARS.append((extracted_text, int(element_id)))
    else:
        print("Элементы не найдены.")
    
    sleep = 800
    message_of_start = f'\U0001F6AA Начинаю оплачивать рекламу за 55 гривен с интервалом {sleep // 60} минут'
    bot.send_message(CHAT_ID, message_of_start)
    
    sum_of_road = 0
    sum_of_succes = 0
    sum_of_bad = 0
    for i in range(len(LIST_TO_TOP)):
        link = LIST_TO_TOP[i]
        parsed_url = urllib.parse.urlparse(link)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        extracted_id = query_params.get('ad-id', [''])[0]
        
        for item in LIST_OF_PARS:
            if item[1] == int(extracted_id):
                doors_model = item[0]
                
        webbrowser.open_new(link)
        pyautogui.sleep(20)
        pyautogui.scroll(-2000)
        pyautogui.sleep(5)
        pyautogui.moveTo(first_button)
        pyautogui.sleep(5)
        pyautogui.click()
        pyautogui.sleep(5)
        pyautogui.moveTo(address_bar_position)
        pyautogui.sleep(5)
        pyautogui.click()
        pyautogui.sleep(1)
        keyboard.press('ctrl')
        keyboard.press('a')
        keyboard.release('ctrl')
        keyboard.release('a')
        pyautogui.sleep(0.5)
        keyboard.press('ctrl')
        keyboard.press('c')
        keyboard.release('ctrl')
        keyboard.release('c')
        clipboard_content = clipboard.paste()
        pyautogui.moveTo(first_button)
        
        if clipboard_content != link: 
            pyautogui.moveTo(second_button)
            pyautogui.scroll(-2000)
            pyautogui.sleep(5)
            pyautogui.click()
            pyautogui.sleep(5)
            pyautogui.click(second_button)
            pyautogui.sleep(5)
            pyautogui.click()
            pyautogui.sleep(0.5)
            keyboard.press('ctrl')
            keyboard.press('w')
            pyautogui.sleep(0.5)
            keyboard.release('ctrl')
            keyboard.release('w')
            pyautogui.sleep(0.5)
        
            date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            message = f'\u2705 {doors_model} піднялися у топ!\n {date_time}'
            bot.send_message(-1001911928428, message)
            sum_of_succes += 1
            time.sleep(sleep)
        else:
            pyautogui.sleep(2)
            date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            message = f'\u274C Ще в топі {doors_model}\n {date_time}'
            bot.send_message(-1001911928428, message)
            pyautogui.click()
            pyautogui.sleep(0.5)
            keyboard.press('ctrl')
            keyboard.press('w')
            pyautogui.sleep(0.5)
            keyboard.release('ctrl')
            keyboard.release('w')
            time.sleep(20) 
            sum_of_bad += 1 
        sum_of_road += 1
        
    message = f'\U0001F916 {sum_of_road} обработано'
    bot.send_message(-1001911928428, message)
    message = f'\U0001F916 {sum_of_succes} успешно обработано'
    bot.send_message(-1001911928428, message)
    message = f'\U0001F916 {sum_of_succes} не нужно оплата'
    bot.send_message(-1001911928428, message)   

@bot.message_handler(commands=['up7'])
def start_up7(message):
    
    LIST_OF_PARS = []
    link_to_parse = 'https://barbados.olx.ua'
    r = requests.get(link_to_parse)
    soup = BeautifulSoup(r.content, 'html.parser')
    elements = soup.find_all('div', {'class': 'css-1sw7q4x'})
    
    if elements:
        for element in elements:
            element_id = element.get('id')
            if element_id is not None:
                p_elements = element.find_all('p', class_='css-ki4ei7 er34gjf0')
                for p_element in p_elements:
                    extracted_text = p_element.get_text()
                    LIST_OF_PARS.append((extracted_text, int(element_id)))
    else:
        print("Элементы не найдены.")

    sleep = 800
    message_of_start = f'\U0001F6AA Начинаю оплачивать поднятия на 7 дней за 65 гривен с интервалом {sleep // 60} минут'
    bot.send_message(CHAT_ID, message_of_start)

    sum_of_road = 0
    sum_of_succes = 0
    
    for i in range(len(LIST_TO_PUSHUP7)):
        link = LIST_TO_PUSHUP7[i]
        parsed_url = urllib.parse.urlparse(link)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        extracted_id = query_params.get('ad-id', [''])[0]
        
        for item in LIST_OF_PARS:
            if item[1] == int(extracted_id):
                doors_model = item[0]
                
        webbrowser.open_new(link)
        pyautogui.sleep(20)
        pyautogui.scroll(-2000)
        pyautogui.sleep(5)
        pyautogui.moveTo(first_button)
        pyautogui.sleep(5)
        pyautogui.click()
        pyautogui.sleep(8)
        pyautogui.scroll(-2000)
        pyautogui.moveTo(second_button)
        pyautogui.sleep(5)
        pyautogui.click()
        pyautogui.sleep(5)
        pyautogui.click(second_button)
        pyautogui.sleep(0.5)
        keyboard.press('ctrl')
        keyboard.press('w')
        keyboard.release('ctrl')
        keyboard.release('w')
        pyautogui.sleep(5)
        
        date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        message = f'\u2705 7 поднятий оплаченн для\n{doors_model}\n {date_time}'
        bot.send_message(-1001911928428, message)
        sum_of_succes += 1
        sum_of_road += 1
        time.sleep(800)
        
    message = f'\U0001F916 {sum_of_road} постов обработано'
    bot.send_message(-1001911928428, message)
    message = f'\U0001F916 {sum_of_succes} - оплатилось'
    bot.send_message(-1001911928428, message)

@bot.message_handler(commands=['start'])
def start_command(message):
    
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_help = types.KeyboardButton("Помощь")
    markup.add(button_help)
    bot.send_message(message.chat.id, "Привет! Напиши /help, чтобы получить список команд.", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_command(message):
    
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_up1 = types.KeyboardButton("Поднять в топ 1 раз")
    button_top_all = types.KeyboardButton("Поднять все в топ")
    button_up7 = types.KeyboardButton("Поднять 7 раз")
    markup.add(button_up1, button_top_all, button_up7)
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    
    if message.text == 'Поднять в топ 1 раз':
        start_up1(message)
    elif message.text == 'Поднять все в топ':
        start_top_all(message)
    elif message.text == 'Поднять 7 раз':
        start_up7(message)
    elif message.text == 'Помощь':
        help_command(message)

def main():
    bot.polling()

if __name__ == '__main__':
    main()