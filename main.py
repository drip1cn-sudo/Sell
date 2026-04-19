import telebot

# আপনার বটের সঠিক টোকেন
TOKEN = '8716769137:AAGpJcCbpF0FBa1VtU4kXk_EQKkb98sg3oA'
# আপনার গ্রুপের সঠিক ইউজারনেম (অবশ্যই @ সহ)
GROUP_ID = '@rahim_ff_Panel'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    try:
        # গ্রুপ মেম্বার চেক
        member = bot.get_chat_member(GROUP_ID, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            bot.send_message(message.chat.id, "✅ অভিনন্দন! আপনি আমাদের গ্রুপে আছেন।")
        else:
            bot.send_message(message.chat.id, f"⚠️ বোনাস পেতে আগে আমাদের গ্রুপে জয়েন করুন: {GROUP_ID}")
    except Exception as e:
        # বট এডমিন না থাকলে এই এরর মেসেজ আসবে
        bot.send_message(message.chat.id, "❌ আমি মেম্বার চেক করতে পারছি না! আমাকে আপনার গ্রুপে Admin বানিয়ে সব পারমিশন দিন।")

bot.polling()
