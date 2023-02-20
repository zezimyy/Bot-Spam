import telebot

chave = "6231013608:AAHRiT-uy5qfC24ln5DVIHo9eRg4B119_18"
bot = telebot.TeleBot(chave)
chat_mestre = 1829626918
lista = []

@bot.message_handler(commands=["hack"])
def hack(mensagem):
  lista = bot.send_message(chat_mestre, "qual o id do alvo? :  ")
  bot.register_next_step_handler(lista, Alvo)

def Alvo(mensagem):
  n = 10
  open("lista.txt", "w").write(mensagem.text)
  bot.send_message(chat_mestre, "anotado")
  lista.append(mensagem.text)
  while n > 0:
    bot.send_message(lista[0], "oi")
    n-=1
    
def verificar(mensagem):
  return True

@bot.message_handler(func=verificar)
def responder(mensagem):
  bot.reply_to(mensagem, "/hack")

bot.polling()