#Иванова Виолетта
#пробный экзамен 7.11.2016
#задание 1 и 2


def capital_letter(): #эта функция создает список слов с заглавной буквы
    f = open('anna.txt', 'r', encoding = 'utf-8')
    string = f.read()
    f.close()
    arr = string.split()
    arr_capital = []
    for element in arr:
        if element[0].isupper():
            arr_capital.append(element)
    arr_capital.sort()

    f = open('capitalized.txt', 'w', encoding = 'utf-8')
    for element in arr_capital:
        element = element.strip('.,!?:;\"')
        f.write(element + '\n')
    f.close()
    return arr_capital

def capital_dictionary(arr_capital): #эта функция выводит все слова по одному разу и выводит кол-во упоминаний каждого слова
    capital_dict = {}
    for element in arr_capital:
        element = element.strip('.,!?:;\"»…')
        if element not in capital_dict:
            capital_dict[element] = 1
        if element in capital_dict:
            capital_dict[element] += 1
    
    f = open('cap_dict.txt', 'w', encoding = 'utf-8')
    for element in capital_dict:
        f.write(element + ' ' + str(capital_dict[element]) + '\n')
        
    f.close()
      

def main():

    arr_capital = capital_letter()
    capital_dictionary(arr_capital)

if __name__ == '__main__':
    main()
    
    
