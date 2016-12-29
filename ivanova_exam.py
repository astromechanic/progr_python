import urllib.request
import os, sys, re

def getting_words():
    
    url = 'http://web-corpora.net/Test2_2016/short_story.html'
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')

    regex = '\s[с|С].*?\s'
    regex_clean = '<.*?>'
    
    words = re.findall(regex, html) #находим все слова на "с"
    words_final = []

    print('Слова на \"с\" из текста\n')
    for element in words:
        element = re.sub(regex_clean, '', element)
        element = re.sub('\s', '', element)
        element = element.strip(',.:;!?')
        element = re.sub('<li', '', element)
        element = re.sub('<div', '', element)
        words_final.append(element)
        print(element) #распечатываем на экране все слова на "с"

    newpath1 = r'/Users/violaivanova/Desktop/all_words' 
    if not os.path.exists(newpath1):
        os.makedirs(newpath1)
        
    f = open('/Users/violaivanova/Desktop/all_words/wordforms.txt','w', encoding='utf-8')
    for element in words_final:
        f.write(element + '\n')
    f.close()

    newpath2 = r'/Users/violaivanova/Desktop/verbs'
    if not os.path.exists(newpath2):
        os.makedirs(newpath2)

    inp = '/Users/violaivanova/Desktop/all_words' #отдадим mystem список слов на "с"
    lst = os.listdir(inp)
    for fl in lst:
        os.system(r"/Users/violaivanova/Desktop/mystem" + " -nwi " + inp + os.sep + fl + " verbs" + os.sep + fl)

    regex_verbs = '{.*?}'
    verbs = []
    f = open('/Users/violaivanova/Desktop/verbs/wordforms.txt', 'r', encoding = 'utf-8')
    for line in f:
        if "=V" in line:
            line = re.sub(regex_verbs, '', line)
            verbs.append(line)
    print('Только глаголы\n') #распечатываем только глагола из списка слов на "с"          
    for element in verbs:
        print(element)
    f.close()

    return verbs

def db():
    f = open('/Users/violaivanova/Desktop/verbs/wordforms.txt', 'r', encoding = 'utf-8')
    text_for_lemmas = f.read()
    text_for_wordforms = text_for_lemmas
    text_for_POS = text_for_lemmas

    f.close()

    
    arr_wordforms_final = []
    arr_lemmas_final = []
    POS = []

    regex_for_lemmas = '{.*?[=\?]'
    regex_for_wordforms = '.*?{'
    regex_for_POS = '(=.*?=|\?)'

    arr_lemmas = re.findall(regex_for_lemmas, text_for_lemmas)
    for element in arr_lemmas:
        element = re.sub('=', '', element)
        element = re.sub('{', '', element)
        arr_lemmas_final.append(element)

    arr_wordforms = re.findall(regex_for_wordforms, text_for_wordforms)
    for element in arr_wordforms:
        element = element.strip('{')
        arr_wordforms_final.append(element)

 
    f = open('/Users/violaivanova/Desktop/verbs/wordforms.txt', 'r', encoding = 'utf-8')
    for line in f:   
        result_POS = re.search(regex_for_POS, line)
        if result_POS:
            POS.append(result_POS.group())
    f.close()

    POS_final = []
    regex_POS_clean = ',.*'
    
    for element in POS:
        element = re.sub(regex_POS_clean, '', element)
        element = element.strip('=')
        POS_final.append(element)

        
    f = open('db.txt', 'w', encoding='utf-8')
    string = ''
    for k in range(0, len(arr_lemmas)):
        string += "INSERT INTO table_of_wordforms (id, lemma, wordform, part of speech) VALUES (" + str(k) + ', ' + arr_lemmas_final[k] + ', ' + arr_wordforms_final[k] + ', ' + POS_final[k] + ");\r\n"
        k += 1
    f.write(string)

    f.close()

        

def main():

    getting_words()
    db()


if __name__ == '__main__':
    main()


    

        
    
    
    
