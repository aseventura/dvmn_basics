import os
import ptbot
from pytimeparse import parse

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░') -> str():
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def notify_progress(secs_left:int, message_id: int, total_seconds:int) -> None:
  current_seconds = total_seconds - secs_left
  message = 'Осталось {} секунд(ы).\n\n'.format(secs_left)
  progressbar = render_progressbar(total_seconds, current_seconds)
  updated_message = message + progressbar
  bot.update_message(chat_id, message_id, updated_message)


def notify(message:str) -> None:
  bot.send_message(chat_id, message)


def reply(wait_time:str) -> None:
  wait_seconds = parse(wait_time)
  if wait_seconds != None:
    message_id = bot.send_message(chat_id, 'Таймер запущен на {} секунд.'.format(wait_seconds))
    bot.create_timer(wait_seconds, notify, 'Время вышло')
    bot.create_countdown(wait_seconds, notify_progress, message_id = message_id, total_seconds = wait_seconds)
  else:
    bot.send_message(chat_id, 'Некорректные данные. Формат: 10s, 2m, 3h')


chat_id = os.getenv('TELEGRAM_CHAT_ID')
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
bot = ptbot.Bot(bot_token)
bot.send_message(chat_id, 'Привет. На сколько запустить таймер?')
bot.wait_for_msg(reply)
