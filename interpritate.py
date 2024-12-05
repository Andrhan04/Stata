import csv
#from sklearn.metrics import confusion_matrix

def inerpritate():
    data = [[],[],[],[],[],[],[],[],[],[],[],[]]
    with open('data.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        cnt = 0
        for row in reader:
            if cnt == 0:
                # Вывод строки, содержащей заголовки для столбцов
                # print(f'Файл содержит столбцы: {", ".join(row)}')
                pass
            else:
                data[0].append(float(row[1].split()[0]))
                if(row[2] == 'Новичок'):
                    data[1].append(1.0)
                if(row[2] == 'Средний'):
                    data[1].append(2.0)
                if(row[2] == 'Продвинутый'):
                    data[1].append(3.0)
                if(row[2] == 'Эксперт'):
                    data[1].append(4.0)
                data[2].append(float(row[6].split()[0]))
                data[3].append(float(row[9].split()[0]))
                data[4].append(float(row[12].split()[0]))
                data[5].append(float(row[15].split()[0]))
                data[6].append(float(row[18].split()[0]))
                data[7].append(float(row[21].split()[0]))
                data[8].append(float(row[24].split()[0]))
                data[9].append(float(row[27].split()[0]))
                data[10].append(float(row[30].split()[0]))
                data[11].append(float(row[33].split()[0]))
            cnt+=1
    return data
