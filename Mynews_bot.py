import telepot
import requests
import time

# Telegram bot token (replace with your bot's token)
TOKEN = '6541233743:AAGo-6EQmFu_ueXd3ifdq0_ntxVip3loD_Y'

# News API key (get your API key from newsapi.org)
NEWS_API_KEY = '21f1e59b741a4536b53ae65cc9f94838'

# Initialize the Telegram bot
bot = telepot.Bot(TOKEN)

# Function to handle incoming messages
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/start':
        bot.sendMessage(chat_id, "Welcome to the News Bot! Send /news to get news headlines.")
    elif command == '/news':
        try:
            # Fetch news data from the News API (you can customize the sources, categories, and other parameters)
            news_url = f'https://newsapi.org/v2/top-headlines?apiKey={NEWS_API_KEY}&country=US'
            response = requests.get(news_url)
            news_data = response.json()

            # Extract and send headlines to the user
            if news_data.get('articles'):
                for article in news_data['articles'][:5]:  # Send the top 5 headlines
                    headline = article['title']
                    link = article['url']
                    bot.sendMessage(chat_id, f"{headline}\nRead more: {link}")
            else:
                bot.sendMessage(chat_id, "No news found.")

        except Exception as e:
            print(str(e))
            bot.sendMessage(chat_id, "Sorry, there was an error fetching the news.")

# Start listening for messages
bot.message_loop(handle)

# Keep the bot running
while True:
    time.sleep(10)
