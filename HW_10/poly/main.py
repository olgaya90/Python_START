from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from polynom_sum import *
import bot_token


async def sum_poly(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num, pol1, pol2 = update.message.text.split()
    print(f'Пользователь {update.effective_user.first_name} ввел(а) {pol1} и {pol2}')
    pol1 = convert_pol(pol1)
    pol2 = convert_pol(pol2)
    temp = fold_pols(pol1, pol2)
    print(f'Сумма полиномов: {get_sum_pol(temp)}')
    await update.message.reply_text(f'ответ: {get_sum_pol(temp)} ')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}!')
    await update.message.reply_text(f'Введите полинромы через пробел после команды /sum 9*x^5+7*x^4+7*x^3+9*x^2+6*x+17=0 3*x^2+2*x+1=0')




bot_token = "ваш token"
app = ApplicationBuilder().token(bot_token).build()
app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("sum", sum_poly))

app.run_polling()