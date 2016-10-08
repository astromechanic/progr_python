#краулер, который собирает все ссылки, откуда надо вытащить текст
#в main() нужно поменять range(), чтобы было больше ссылок

import urllib.request
import re

def download(commonUrl):

    req = urllib.request.Request(commonUrl)     
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('windows-1251')

    regPostTitle = re.compile('mnname.*?html', flags=re.U | re.DOTALL)
    all_links = regPostTitle.findall(html)

    new_links = []
    regex = 'mnname"><a href="/'
    basicUrl = 'http://znamyatrud.ru/'
    for link in all_links:
        link = re.sub(regex, '', link)
        link_1 = basicUrl + link
        new_links.append(link_1)      

    f = open('links.txt', 'a')
    for t in new_links:
        f.write(t + '\n')

    f.close()
    return 0




def main():

    commonUrl = 'http://znamyatrud.ru/news.html?page='
    for i in range(1, 5):
        s = commonUrl + str(i)
        download(s)

if __name__ == '__main__':
    main()




