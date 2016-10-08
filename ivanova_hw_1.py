import urllib.request  

url = 'http://www.znamyatrud.ru/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  
req = urllib.request.Request('http://www.znamyatrud.ru/', headers={'User-Agent':user_agent})  

with urllib.request.urlopen(req) as response:
    html = response.read().decode('windows-1251')

import re
regPostTitle = re.compile('<div class="mndata">.*?</a>', flags=re.U | re.DOTALL)
titles = regPostTitle.findall(html)

new_titles = []
regex = '(<.*?>|[0-9])|\.'

for element in titles:
    element = re.sub(regex, '', element)
    new_titles.append(element)

f = open('titles.txt', 'w')
for t in new_titles:
    f.write(t + '\n')

f.close()

