'''
Created on 2013-7-9

@author: yongli.dang
'''
#import os
import re
from xml.dom.minidom  import Document
doc=Document()
wordbook=doc.createElement('wordbook')
match=re.compile(u'(\d+)\.(.*?)([\u4e00-\u9fa5].*)')
with open('d:\\a.txt','r') as myfile:
    content=myfile.readlines()
    for  line in content:
        # print line
        item=doc.createElement('item')
        word=doc.createElement('word')
        trans=doc.createElement('trans')
        phonetic=doc.createElement('phonetic')
        tags=doc.createElement('tags')
        progress=doc.createElement('progress')
        
        matches=match.findall(line.decode())
        word.appendChild(doc.createCDATASection(matches[0][1]))
        trans.appendChild(doc.createCDATASection(matches[0][2]))
        progress.appendChild(doc.createTextNode('0'))
        phonetic.appendChild(doc.createTextNode(''))
        tags.appendChild(doc.createTextNode(''))
        item.appendChild(word)
        item.appendChild(trans)
        item.appendChild(phonetic)
        item.appendChild(tags)
        item.appendChild(progress)
        wordbook.appendChild(item)
    doc.appendChild(wordbook)
objxml=open('d:\\word.xml','w')
objxml.write(doc.toprettyxml(indent="  "))
objxml.close()
    

       
        

