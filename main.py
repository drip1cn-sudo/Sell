import telebot
from telebot import types

# এখানে আপনার বটের টোকেন বসান
TOKEN = 'আপনার_বট_টোকেন'
# আপনার গ্রুপ ইউজারনেম (বটকে অবশ্যই এডমিন করতে হবে)
GROUP_ID = '@wf_rahim_69_ff'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    try:
        # গ্রুপ মেম্বার কি না চেক করা
        status = bot.get_chat_member(GROUP_ID, user_id).status
        if status in ['member', 'administrator', 'creator']:
            bot.send_message(message.chat.id, "✅ আপনি গ্রুপে আছেন! কাজ শুরু করতে পারেন।")
        else:
            bot.send_message(message.chat.id, f"⚠️ বোনাস পেতে আগে আমাদের গ্রুপে জয়েন করুন: {GROUP_ID}\nজয়েন করার পর আবার /start দিন।")
    except Exception as e:
        bot.send_message(message.chat.id, "বটকে গ্রুপে এডমিন হিসেবে যুক্ত করুন!")

bot.polling()
