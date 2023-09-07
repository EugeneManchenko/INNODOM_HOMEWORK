import telebot
import requests
import random

# Ваш токен от BotFather
TOKEN = '6665973671:AAGby4fNXTcYysOT6CFehm3-7jYvKFqhu7s'
bot = telebot.TeleBot(TOKEN)

# Ваш API ключ от OpenWeatherMap
API_KEY = '6715bb311d66cf432ca9d649c4872381'
API_URL_CURRENT = 'http://api.openweathermap.org/data/2.5/weather'
API_URL_FORECAST = 'http://api.openweathermap.org/data/2.5/forecast'
UNSPLASH_API_KEY = 'vbo-W3qYcWTM95i3PYqbZjuJQ_u0TOQkdbVQeuI6flM'


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет! Я бот, который может прислать тебе погоду в любом городе. Просто введи название города!")


@bot.message_handler(func=lambda message: True)
def send_weather(message):
    city = message.text

    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        yes_button = telebot.types.KeyboardButton(text='Да')
        no_button = telebot.types.KeyboardButton(text='Нет')
        keyboard.add(yes_button, no_button)
        question_message = "Хотите текущий прогноз погоды и прогноз на несколько дней?"
        msg = bot.send_message(message.chat.id, question_message, reply_markup=keyboard)
        bot.register_next_step_handler(msg, lambda message: get_weather(message, city))
    except requests.exceptions.RequestException:
        response_message = "Извините, не удалось подключиться к погодному сервису. Пожалуйста, попробуйте снова позже."
        bot.reply_to(message, response_message)


def get_weather(message, city):
    try:
        current_weather = get_current_weather(city)
        forecast_weather = get_forecast_weather(city)

        if current_weather is not None and forecast_weather is not None:
            current_temp = current_weather['main']['temp']
            current_description = current_weather['weather'][0]['description']

            if message.text.lower() == 'да':
                forecast_message = generate_forecast_message(forecast_weather)
                response_message = f"Текущая погода в городе {city.title()}: {current_temp}°C, {current_description}.\n\n{forecast_message}"
            else:
                response_message = f"Текущая погода в городе {city.title()}: {current_temp}°C, {current_description}."

            # Добавление картинки из Unsplash
            image_url = get_random_image()
            bot.send_photo(message.chat.id, image_url,
                           caption="Эта картинка появилась не случайно. Подумай с какими мыслями она ассоциируется..."
                                   "Хорошего дня!")
        else:
            response_message = "Извините, что-то пошло не так. Пожалуйста, попробуйте снова позже."
    except requests.exceptions.RequestException:
        response_message = "Извините, не удалось подключиться к погодному сервису. Пожалуйста, попробуйте снова позже."

    bot.reply_to(message, response_message)


def get_current_weather(city):
    response = requests.get(API_URL_CURRENT, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    if response.status_code == 200:
        return response.json()
    return None


def get_forecast_weather(city):
    response = requests.get(API_URL_FORECAST, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    if response.status_code == 200:
        return response.json()
    return None


def generate_forecast_message(weather):
    forecast_message = "Прогноз погоды на несколько дней вперед:\n\n"
    for forecast in weather['list']:
        date = forecast['dt_txt'].split()[0]
        time = forecast['dt_txt'].split()[1]
        temp = forecast['main']['temp']
        description = forecast['weather'][0]['description']

        forecast_message += f"{date} {time}: {temp}°C, {description}\n"
    return forecast_message


def get_random_image():
    url = f"https://api.unsplash.com/photos/random?client_id={UNSPLASH_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        json_response = response.json()
        image_url = json_response['urls']['regular']
        return image_url
    return None


bot.polling()