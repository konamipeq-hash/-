import telebot
import google.generativeai as genai

# ضع هنا توكن التيليجرام الخاص بك
TELEGRAM_TOKEN = '8557793418:AAGZr4crQ4DoazN1RcuB2ovQPuQEkQ1TAoc'
# ضع هنا مفتاح Gemini الخاص بك
GEMINI_API_KEY = 'AIzaSyDXFyC-yeEgK8bdzyIRFVEia7ezMFMeyxg'

# إعداد الذكاء الاصطناعي
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def answer_all(message):
    try:
        # إرسال سؤال المستخدم للذكاء الاصطناعي
        response = model.generate_content(message.text)
        # إرسال الإجابة للمستخدم في تيليجرام
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "عذراً، حدث خطأ ما أو السؤال مخالف للسياسات.")

print("البوت يعمل الآن...")
bot.polling()
