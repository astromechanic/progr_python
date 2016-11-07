#Иванова Виолетта
#пробный экзамен 7.11.2016
#задание 1


def capital_letter():
    f = open('anna.txt', 'r', encoding = 'utf-8')
    string = f.read()
    f.close()
    arr = string.split()
    arr_capital = []
    for element in arr:
        if element[0].isupper():
            arr_capital.append(element)

    f = open('capitalized.txt', 'w', encoding = 'utf-8')
    for element in arr_capital:
        f.write(element + '\n')
    f.close()
    return arr_capital

def main():

    capital_letter()

if __name__ == '__main__':
    main()
    
    
