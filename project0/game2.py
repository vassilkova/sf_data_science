import numpy as np

def random_predict(number=1):
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1  # число попыток
    begin_interval = 0 # начало отрезка угадывания
    end_interval = 100 # конец отрезка угадывания
    predict = 50 # попытка угадать число np.random.randint(1,101)
    
    while predict != number:
        count += 1
        if number > predict:
            begin_interval = predict+1 # сдвиг начала отрезка 
        else:
            end_interval = predict-1 # сдвиг конца отрезка
        predict=(begin_interval+end_interval)//2    
    return(count)


print(f'Количество попыток: {random_predict()}')



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
   score_game(random_predict)
    
