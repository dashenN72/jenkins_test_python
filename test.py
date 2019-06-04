# coding:utf-8
import datetime
content = datetime.datetime.now() 
with open('read.txt', 'a', encoding='utf-8') as f:
    print(content)
    f.write(str(content) + '\n')