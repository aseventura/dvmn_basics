import smtplib
import os

template_message = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. После окончания курса у тебя будет 2 месяца, чтобы догнать программу. 
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

personal_message = template_message.replace('%friend_name%', 'Ярослав')\
    .replace('%my_name%', 'Евгений').replace('%website%', 'dvmn.org')

from_addr = os.getenv('FROM_ADDRESS')
to_addr = os.getenv('TO_ADRESS')

mail = """From: {from_addr} 
To: {to_addr}
Subject: Ревью!
Content-Type: text/plain; charset="UTF-8";

{msg}""".format(from_addr=from_addr, to_addr=to_addr, msg=personal_message)\
    .encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
server.login(login, password)
server.sendmail(from_addr, to_addr, mail)
server.quit()
