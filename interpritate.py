import csv
#from sklearn.metrics import confusion_matrix

def inerpritate():
    data = [[]*12]
    with open('data.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        cnt = 0
        for row in reader:
            if cnt == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                if(cnt != 1):
                    data.append([]*12)
                else:
                    print(row)
                if(row[1] == 'Новичок'):
                    data[cnt-1].append(1)
                if(row[1] == 'Средний'):
                    data[cnt-1].append(2)
                if(row[1] == 'Продвинутый'):
                    data[cnt-1].append(3)
                if(row[1] == 'Эксперт'):
                    data[cnt-1].append(4)
                
                data[cnt-1].append(row[2].count(';') + 1)
                data[cnt-1].append(row[3].count(',') + 1)
                if(row[3][len(row[3])-1] == ','):
                    data[cnt-1][2] -= 1
                data[cnt-1].append(row[4].count(';') + 1)
                data[cnt-1].append(row[5])

                if(row[6] == 'Не знаком'):
                    data[cnt-1].append(0)
                else:
                    data[cnt-1].append(row[6].count(';') + 1)
                
                data[cnt-1].append(row[7].count(',') + 1)
                data[cnt-1].append(row[9])

                if(row[10] == 'Никогда'):
                    data[cnt-1].append(0)
                if(row[10] == 'Иногда'):
                    data[cnt-1].append(1)
                if(row[10] == 'Регулярно'):
                    data[cnt-1].append(2)
                if(row[10] == 'Всегда участвую'):
                    data[cnt-1].append(3)

                if(row[11] == 'Совсем не знаком'):
                    data[cnt-1].append(0)
                if(row[11] == 'Знаком с базовыми понятиями'):
                    data[cnt-1].append(1)
                if(row[11] == 'Понимаю и применяю на практике'):
                    data[cnt-1].append(2)
                if(row[11] == 'Эксперт'):
                    data[cnt-1].append(3)

                if(row[12] == 'Оптимизация алгоритмов'):
                    data[cnt-1].append(0)
                if(row[12] == 'Работа с графами'):
                    data[cnt-1].append(1)
                if(row[12] == 'Алгоритмы динамического программирования'):
                    data[cnt-1].append(2)
                if(row[12] == 'Алгоритмы динамического программирования'):
                    data[cnt-1].append(3)
                if(row[12] == 'Другие'):
                    data[cnt-1].append(4)
            cnt+=1
    return data
