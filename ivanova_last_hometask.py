import os, sys

def read_text():
    f = open('anna.txt', 'r', encoding = 'utf-8') #читаем какой-нибудь большой файл, например Анну Каренину
    text = f.read()
    
    text_arr = [] #создаем массив словоформ, очищенных от знаков препинания
    text = text.split()
    for word in text:
        word = word.strip('.,?!\"\(\);:')
        text_arr.append(word)
    f.close()

    #создадим директории 1 (для хранения списка словоформ) и 2 (для хранения словоформ и лемм после обработки mystem-ом)
    newpath1 = r'/Users/violaivanova/Desktop/1' 
    if not os.path.exists(newpath1):
        os.makedirs(newpath1)
    
    newpath2 = r'/Users/violaivanova/Desktop/2'
    if not os.path.exists(newpath2):
        os.makedirs(newpath2)
        
    #теперь запишем этот массив в файл в директорию 1
    f = open('/Users/violaivanova/Desktop/1/wordforms.txt','w', encoding='utf-8')
    for word in text_arr:
        f.write(word + '\n')
    f.close()

    #далее файл wordforms.txt отдаем mystem-у, результаты записываются в директорию 2
    inp = '/Users/violaivanova/Desktop/1'
    lst = os.listdir(inp)
    for fl in lst:
        os.system(r"/Users/violaivanova/Desktop/mystem" + " -n " + inp + os.sep + fl + " 2" + os.sep + fl)

    lemm_dict = {}
    #откроем файл, в котором хранятся словоформы и леммы (то, что получилось после обработки mystem-ом)
    #и создадим словарь, в котором ключами будут словоформы
    f = open('/Users/violaivanova/Desktop/2/wordforms.txt', 'r', encoding='utf-8')
    for line in f:
        k = line.split('{')
        k[1] = k[1].strip('}\r\n')
        lemm_dict[k[0]] = k[1]
    f.close()

    
    #откроем файл на запись, куда будем вписывать INSERT-ы
    f = open('table.txt', 'w', encoding='utf-8')
    string =''
    
    for keys in lemm_dict:
        string += "INSERT INTO table_of_wordforms (wordform, lemma) VALUES (" + keys + ", " + lemm_dict[keys] + ");\r\n"
    f.write(string)
        
    f.close()
    
    return lemm_dict

       
def main():
    
    read_text()
    
if __name__ == '__main__':  
    main()
