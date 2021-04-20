import datetime as dt
import random

from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Updater, Filters  # Подключаем библиотеки


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater('1648583254:AAHWoIMzKh07D1zd32kbXfPA_DhyBjdAnVw', use_context=True)  # Имя бота - @Alabuga_tat_bot

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('help', helper))  # Добавляем несколько обработчиков команд
    dp.add_handler(CommandHandler("set_timer", set_timer,
                                  pass_args=True,  # Парсинг аргументов при вводе комманды
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset_timer,
                                  pass_chat_data=True)
                   )
    dp.add_handler(CommandHandler("rasp", rasp,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))  # Все еще обрабатываем потенциальные команды
    text_handler = MessageHandler(Filters.text, calkulater)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler('calculate', calkulater,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("goroskop", goroskop,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    updater.start_polling()  # запускаем бота

    updater.idle()


def helper(update, context):  # функция для помощи в использовании бота
    update.message.reply_text(  # вывод текста помощи
        'Окей, я бот, в котором реализованы некоторые функции, такие как: '
        '\n'  # символ переноса строки
        '/calculate - это калькулятор, ввод, например - "/calculate 56+568+9-94/8598*8"'
        '\n'
        '/set_timer - это установка таймера, например - /set_timer 150'
        '\n'
        '/unset - удалить все процессы таймера'
        '\n'
        '/rasp - Расписание уроков, например - /rasp 8'
        '\n'
        '/goroskop - Гороскоп, нпроимер - /goroskop овен'
    )


def start(update, context):  # функция для начала бота
    update.message.reply_text(  # вывод текста приветствия
        "Я бот. Помочь? "
        "Введите /help для получения помощи"
    )


def calkulater(update, context):  # функция для калькулятора
    if context.args == []:  # проверка, что есть что вычислять
        update.message.reply_text(
            'Пожалуйста, введите в формате "/calkulate (здесь ваше выражение)"'  # вывод предупреждения
        )
    else:
        due = context.args  # назначение переменной со строкой
        due = ''.join(due)  # делаем слитную строку
        due = due.replace(' ', '')  # убираем пробелы
        due = due.replace('=', '')  # убираем знак равенства

        due = due.replace('^', '**')  # замена знака степени на понятный для питона

        try:  # обработчик ошибок
            update.message.reply_text(
                f'Ответ - {round(eval(due), 2)}'  # если все хорошо, то вывод ответа
            )
        except ZeroDivisionError:  # если есть деление на ноль
            update.message.reply_text(
                'На ноль делить нельзя!'  # вывод ошибки
            )
        except ValueError:  # если неверный формат
            update.message.reply_text(
                'Неверный формат!'
            )
        except FloatingPointError:
            update.message.reply_text(
                'Ошибка!'
            )
        except OverflowError:
            update.message.reply_text(
                'Ошибка!'
            )
        except IndexError:
            update.message.reply_text(
                'Ошибка!'
            )
        except SyntaxError:  # и другие ошибки
            update.message.reply_text(
                'Ошибка при вводе'
            )


def rasp(update, context):  # функция для создания расписания
    n = context.args[0]  # создание переменной

    try:  # отлов ошибок
        a, b, c, d, e = 'Математика', 'Русский Язык', 'Физическая культура', 'Иностранный язык', 'Биология'  # назначение переменных

        k6 = {0: [a, b, c, d, e],  # создание расписаний для разных классов
              1: [b, c, a, e, d],  # на разные дни недели
              2: [c, d, a, e, b],
              3: [d, a, c, b, e],
              4: [a, d, e, b, c],
              5: [a, d, e, b, c],
              6: 'Сегодня тебе повезло, у тебя нет уроков'}
        k7 = {0: [a, b, c, d, e],
              1: [b, c, a, e, d],
              2: [c, d, a, e, b],
              3: [d, a, c, b, e],
              4: [a, d, e, b, c],
              5: [a, d, e, b, c],
              6: 'Сегодня тебе повезло, у тебя нет уроков'}
        k8 = {0: [a, b, c, d, e],
              1: [b, c, a, e, d],
              2: [c, d, a, e, b],
              3: [d, a, c, b, e],
              4: [a, d, e, b, c],
              5: [a, d, e, b, c],
              6: 'Сегодня тебе повезло, у тебя нет уроков'}
        k9 = {0: [a, b, c, d, e],
              1: [b, c, a, e, d],
              2: [c, d, a, e, b],
              3: [d, a, c, b, e],
              4: [a, d, e, b, c],
              5: [a, d, e, b, c],
              6: 'Сегодня тебе повезло, у тебя нет уроков'}
        k10 = {0: [a, b, c, d, e],
               1: [b, c, a, e, d],
               2: [c, d, a, e, b],
               3: [d, a, c, b, e],
               4: [a, d, e, b, c],
               5: [a, d, e, b, c]}

        k11 = {0: [a, b, c, d, e],
               1: [b, c, a, e, d],
               2: [c, d, a, e, b],
               3: [d, a, c, b, e],
               4: [a, d, e, b, c],
               5: [a, d, e, b, c]}

        my_datetime = dt.datetime.now()

        k = ['01-01', '01-02', '01-03', '01-04', '01-05', '01-06', '01-07', '02-23', '03-08', '05-01', '05-09', '06-12',
             '09-01', '11-04']  # праздничные дни
        ggg = 0
        if str(my_datetime.strftime("%m")) == '06' or str(my_datetime.strftime("%m")) == '07' \
                or str(my_datetime.strftime("%m")) == '08':
            update.message.reply_texе('Можешь отдохнуть, сейчас каникулы.')  # каникулы

        if str(my_datetime.strftime("%m-%d")) in k:
            update.message.reply_text('Счастливого праздника!')  # праздники

        if my_datetime.weekday() == 6:  # в воскресенье выходной
            update.message.reply_text(
                'Выходной.'
            )
            ggg += 1

        x = int(my_datetime.strftime("%H").lstrip('0'))  # создание переменных для часов и минут
        y = int(my_datetime.strftime("%M").lstrip('0'))
        if ggg == 0:
            if x == 8 and y < 45:  # расчет времени уроков
                z = 0
            elif x == 9 and y < 45:
                z = 1
            elif x == 10 and y < 45:
                z = 2
            elif x == 11 and 5 <= y < 50:
                z = 3
            elif x == 10 and 5 <= y < 50:
                z = 4
            elif x >= 12 and y >= 50 or x >= 13:
                update.message.reply_text('Уроки закончились, можешь отдохнуть.')  # окончание уроков
            else:
                update.message.reply_text('На данный момент нет урока.')

            if n == 6:
                update.message.reply_text(k6[my_datetime.weekday()][z])  # вывод данного урока
            if n == 7:
                update.message.reply_text(k7[my_datetime.weekday()][z])
            if n == 8:
                update.message.reply_text(k8[my_datetime.weekday()][z])
            if n == 9:
                update.message.reply_text(k9[my_datetime.weekday()][z])
            if n == 10:
                update.message.reply_text(k10[my_datetime.weekday()][z])
            if n == 11:
                update.message.reply_text(k11[my_datetime.weekday()][z])

    except ValueError:  # отлов ошибок при вводе
        update.message.reply_text(
            'Ошибка'
        )
    except SyntaxError:
        update.message.reply_text(
            'Ошибка'
        )


def goroskop(update, context):  # функция для гороскопа

    x = context.args[0]  # назначение переменных
    r = {}
    try:  # отлов ошибок
        if x.lower() == 'овен':  # спрос знака зодиака
            x = 1
        elif x.lower() == 'телец':
            x = 2
        elif x.lower() == 'близнецы':
            x = 3
        elif x.lower() == 'рак':
            x = 4
        elif x.lower() == 'лев':
            x = 5
        elif x.lower() == 'дева':
            x = 6
        elif x.lower() == 'весы':
            x = 7
        elif x.lower() == 'скорпион':
            x = 8
        elif x.lower() == 'стрелец':
            x = 9
        elif x.lower() == 'козерог':
            x = 10
        elif x.lower() == 'водолей':
            x = 11
        elif x.lower() == 'рыбы':
            x = 12
        opi = ['Вас ждёт незабываемый день, все ваши цели оправдаются!', 'Приготовтесь к неудачам, их будет много',
               'Вас переполнит жизненная энергия.', 'Красивый день, но не для вас, вам нужно готовиться для успеха',
               'Вас ждет очень прибыльный день.', 'Много лжи, много обмана. но это сыграет вам на руку',
               'Сегодня будет самый успешный день за неделю!', 'Готовтесь к убыткам, зато потом придет прибыль',
               'Ваш день будет полон сюрпризов', 'Вы сможете повысить свой рейтинг',
               'Удачный день для начала романа.', 'Неплохое время. чтобы пройти обследование.']  # предсказания
        if dt.date.today() not in r:
            ove, tel, bli, rac, lev, dev, ves, sco, stre, coz, vod, ryb = random.sample(opi, 12)
            r[dt.date.today()] = [ove, tel, bli, rac, lev, dev, ves, sco, stre, coz, vod, ryb]  # вывод предсказания
        update.message.reply_text(r[dt.date.today()][x - 1])
    except SyntaxError:  # отлов ошибок
        update.message.reply_text(
            'Введите свой знак зодиака'
        )
    except ValueError:
        update.message.reply_text(
            'Введите свой знак зодиака'
        )


def set_timer(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.message.chat_id
    try:
        # args[0] должен содержать значение аргумента (секунды таймера)
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text(
                'Извините, не умеем возвращаться в прошлое')
            return

        # Добавляем задачу в очередь
        # и останавливаем предыдущую (если она была)
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(task, due, context=chat_id)
        # Запоминаем созданную задачу в данных чата.
        context.chat_data['job'] = new_job
        # Присылаем сообщение о том, что всё получилось.
        update.message.reply_text(f'Вернусь через {due} секунд')

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


def task(context):  # завершение работы таймера
    job = context.job
    context.bot.send_message(job.context, text='Вернулся!')


def unset_timer(update, context):
    # Проверяем, что задача ставилась
    if 'job' not in context.chat_data:
        update.message.reply_text('Нет активного таймера')
        return
    job = context.chat_data['job']
    # планируем удаление задачи (выполнится, когда будет возможность)
    job.schedule_removal()
    # и очищаем пользовательские данные
    del context.chat_data['job']
    update.message.reply_text('Хорошо, вернулся сейчас!')


if __name__ == '__main__':  # запуск программы
    main()
