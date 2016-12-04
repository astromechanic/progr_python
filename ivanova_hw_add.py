import urllib.request
import re

def getting_texts(): #функция, которая достает тексты с сайтов

    url_arr = [
        'http://ura.ru/news/1052269896',
        'https://russian.rt.com/world/news/338712-tramp-vecherinka-obraz-sebya',
        'http://mir24.tv/news/world/15396255',
        'http://izvestia.ru/news/649382',
        ]

    regex1 = '</div></div><p>.*?</p>.*?<div class="custom-html">'
    regex2 = 'article__summary.*?Конуэй\.&nbsp;'
    regex3 = '<p>Главный спонсор.*?каждым Рождеством.'
    regex4 = '<p>Дональд Трамп.*?галстуком маскарадному наряду.'

    reg_sub = re.compile('<.*?>', flags = 0)
    
    i = 0

    while i < len(url_arr):
        response = urllib.request.urlopen(url_arr[i])
        html = response.read().decode('utf-8')
        if i == 0:
            text1 = re.findall(regex1, html)
            for el in text1:
                el = reg_sub.sub('', el)
                el = re.sub('&nbsp;', ' ', el)
                el = re.sub('&laquo;', ' ', el)
                el = re.sub('&raquo;', '', el)
                el = re.sub('&mdash;', ' ', el)
                
                f = open('text1.txt', 'w')
                f.write(el)
                f.close()
        
        if i == 1:
            text2 = re.findall(regex2, html)
            for el in text2:
                el = reg_sub.sub(' ', el)
                f = open('text2.txt', 'w')
                f.write(el)
                f.close()
        
        if i == 2:
            text3 = re.findall(regex3, html)
            for el in text3:
                el = reg_sub.sub(' ', el)
                f = open('text3.txt', 'w')
                f.write(el)
                f.close()
        
        if i == 3:
            text4 = re.findall(regex4, html)
            for el in text4:
                el = reg_sub.sub(' ', el)
                el = re.sub('&nbsp;', ' ', el)
                f = open('text4.txt', 'w')
                f.write(el)
                f.close()
        i += 1
    return 0

def getting_sets(): #функция, которая делает из полученных текстов множества
    regex = '[.,?!"\(\)«:»]'
    f = open('text1.txt', 'r')
    text1 = f.read()
    f.close()
    text1 = text1.lower()
    text1 = re.sub(regex, '', text1)
    text1 = text1.split()
    A1 = set(text1)
    

    #f = open('text2.txt', 'r')
    #text2 = f.read()
    #f.close()
    #text2 = text2.split()
    #A2 = set(text2)

    f = open('text3.txt', 'r')
    text3 = f.read()
    f.close()
    text3 = text3.lower()
    text3 = re.sub(regex, '', text3)
    text3 = text3.split()
    A3 = set(text3)

    f = open('text4.txt', 'r')
    text4 = f.read()
    f.close()
    text4 = text4.lower()
    text4 = re.sub(regex, '', text4)
    text4 = text4.split()
    A4 = set(text4)
    
    #поиск общих для всех заметок слов
    B13 = A1.intersection(A3) # слова, общие в 1 и 3 заметке
    B134 = B13.intersection(A4) #слова, общие в 1, 3 и 4 заметке
    f = open('common_words.txt', 'w')
    for word in sorted(B134):
        f.write(word + '\n')

    C1 = A1.symmetric_difference(A3)
    f = open('symm_1_3.txt', 'w') #симм.разность 1 и 3 заметки
    for word in sorted(C1):
        f.write(word + '\n')

    C2 = A1.symmetric_difference(A4)
    f = open('symm_1_4.txt', 'w') #симм.разность 1 и 4 заметки
    for word in sorted(C2):
        f.write(word + '\n')

    C3 = A3.symmetric_difference(A4)
    f = open('symm_3_4.txt', 'w') #симм.разность 3 и 4 заметки
    for word in sorted(C3):
        f.write(word + '\n')

        

def main():
    
    getting_texts()
    getting_sets()
    
if __name__ == '__main__':
    main()

