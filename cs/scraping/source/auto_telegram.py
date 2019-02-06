import telepot
import datetime

bot = telepot.Bot('631535855:AAEhO70torhSSAsT-DTSmfpI9bQJeEeXQsI')

# now = today.strftime('%Y%m%d')
# st_dt = today - datetime.timedelta(days=30)
# print(now)
# print(st_dt)

# output_file = open('../output/officetel_rent(201901_2019-01-13).xlsx', 'rb')
# bot.sendDocument(769375336, (output_file))

# print(bot.getMe()) # {'id': 631535855, 'is_bot': True, 'first_name': 'DataBot', 'username': 'DataCrwalBot'}
# bot.sendMessage('769375336', '안녕?')
# bot.sendChatAction('769375336', 'upload_photo')
# bot.sendPhoto('769375336', open('./img/seokhyeon/12179841208_20180804223343866.jpg', 'rb'), caption='귀여운 어린 시절')

class Telegram():
    def send_telegram(self, name, id='769375336', attachment=None):
        caption = "안녕?"
        output_file = open(attachment, 'rb')
        bot.sendDocument(id, (output_file), caption=caption)