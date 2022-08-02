# from isOdd import isOdd # проверка на четность

# print(isOdd(0)) 
# print(isOdd(1))



# from progress.bar import Bar # прогресс загрузки
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     # Do some work
#     bar.next()
# bar.finish()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
from spy import *


app = ApplicationBuilder().token("5459063823:AAE2YLKrSp37ZrfBVem5IAJWb81FzAQBljc").build()

print('server start')
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

app.run_polling()
