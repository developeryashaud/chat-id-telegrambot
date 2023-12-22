import telebot
import csv

# Initialize your bot with the Telegram Bot API token
TOKEN = '6902024990:AAGr_Dpzxw0aCB_Jc31caJGvqGfrqDCSntY'
bot = telebot.TeleBot(TOKEN)

# Function to get the chat IDs
def get_chat_ids():
    chat_ids = []

    # Fetch updates from the bot
    updates = bot.get_updates()
    
    # Extract chat IDs from the updates
    for update in updates:
        chat_id = update.message.chat.id
        if chat_id not in chat_ids:
            chat_ids.append(chat_id)
    
    return chat_ids

# Get chat IDs
chat_ids_list = get_chat_ids()

# File path to save chat IDs in a CSV file
file_path = 'chat_ids.csv'

# Writing chat IDs to the CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the chat IDs to the CSV file
    writer.writerow(['Chat IDs'])
    for chat_id in chat_ids_list:
        writer.writerow([chat_id])

print(f"Chat IDs have been saved to {file_path}")

@bot.message_handler(commands=['start'])
def get_chat_id(message):
    chatid=message.chat.id
    bot.reply_to(message,chatid)

bot.polling()