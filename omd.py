# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Guido van Rossum <guido@python.org>

def step2_umbrella():
    print(
        'Заходит утка с зонтиком в бар, а бармен ей и говорит:\n'
        'Чувак, ты думал что-то здесь будет? Оооооо, нет, от тебя воняет уткой, даже отсюда чувствую!\n'
        'Закрывай, закрывай дверь и иди отсюда.\n'
    )


def step2_no_umbrella():
    print(
        'Заходит утка без зонтика в бар, а там на входе надпись:\n'
        '«@Балабоба»\n'
        'Утка заходит, садится за столик. Вдруг, откуда ни возьмись - кабан.\n'
        'Подкрался к утке, и говорит: - Это я, ваш муж, верните мне мою утку! \n'
        '- Ты кто? - спрашивает утка.\n'
        '- Мой муж!\n'
        '- Я пришел забрать у вас вашу утку.\n'
        '- Но я никогда не давала мужу моей утки!\n'
        'Кабан, почесав бок: - А он и не спрашивал.\n'
    )


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
