import telegram
import datetime
# updater
from telegram import bot
from telegram.ext import MessageHandler, Filters, Updater


token= "5558978594:AAF83L7r2PGj0EMjPQMR6EgeO4FeCbrLQSs"
id = "5524834637"
bot=telegram.Bot(token=token)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()


# 사용자가 보낸 메세지를 읽어들이고, 답장을 보내줍니다.
# 아래 함수만 입맛에 맞게 수정해주면 됩니다. 다른 것은 건들 필요없어요.
def handler(update, context):
    user_text = update.message.text  # 사용자가 보낸 메세지를 user_text 변수에 저장합니다.
    if user_text == "안녕":  # 사용자가 보낸 메세지가 "안녕"이면?
        bot.send_message(chat_id=id, text="어 그래 안녕")  # 답장 보내기
    elif user_text == "뭐해":  # 사용자가 보낸 메세지가 "뭐해"면?
        bot.send_message(chat_id=id, text="그냥 있어")  # 답장 보내기
    elif user_text == "뭐 먹었어?":  # 사용자가 보낸 메세지가 "뭐 먹었어?"면?
        bot.send_message(chat_id=id, text="난 계란찜에 주먹밥 먹었어")  # 답장 보내기


echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)


def send_msg(text):
    token= "5558978594:AAF83L7r2PGj0EMjPQMR6EgeO4FeCbrLQSs"
    id = "5524834637"
    bot=telegram.Bot(token=token)
    # update = bot.getUpdates()
    # for u in update:
    #     print(u.message)


    bot.sendMessage(chat_id=id, text=text)

def main():
    # send_msg("안녕")
    # send_msg("따까리")
    # send_msg(str(datetime.datetime.now()))
    pass

if __name__ == "__main__":
    main()