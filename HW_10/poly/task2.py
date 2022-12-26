""""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.
Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.
Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE ):

    await update.message.reply_text(
        f'Здравствуйте, {update.effective_user.first_name}! '
        f'Введите /poly и нажмите enter для вычисления суммы многочленов: '
        f'9*x^5 + 7*x^4 + 7*x^3 + 9*x^2 + 6x + 17 = 0 ')


async def poly(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text(f'Сумма многочленов: {res_sum}')

def poly_genium():
    global res_sum
    with open('res1.txt', 'r') as data:
        res1 = data.read()
    with open('res2.txt', 'r') as data:
        res2 = data.read()
    file_1 = open('res1.txt', 'r')
    file_2 = open('res2.txt', 'r')
    sum_poly = open('res_sum.txt', 'w')
    file1 = file_1.readline()
    file2 = file_2.readline()
    for i in range(len(file1)):
        if file1[i - 1] != '^':
            if file1[i].isnumeric():
                sum_poly.write(str(int(file1[i]) + int(file2[i])))
            else:
                sum_poly.write(str(file1[i]))
        else:
            sum_poly.write(str(file1[i]))
    sum_poly = open('res_sum.txt', 'r')
    with open('res_sum.txt', 'r') as data:
        res_sum = data.read()


poly_genium()
bot_token = ""
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("poly", poly))
app.run_polling()