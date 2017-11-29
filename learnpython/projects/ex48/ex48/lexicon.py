#coding=utf-8
def convert_number(stuff):
    try:
        return int(stuff)
    except ValueError:
        return None
#设置一个字典，每个词对应一个元组       
lexicon = {
        'north': ('direction', 'north'),
        'south': ('direction', 'south'),
        'east': ('direction', 'east'),
        'west': ('direction', 'west'),
        
        'go': ('verb', 'go'),
        'kill': ('verb', 'kill'),
        'eat': ('verb', 'eat'),
        
        'the': ('stop', 'the'),
        'in': ('stop', 'in'),
        'of': ('stop', 'of'),
        
        'bear': ('noun', 'bear'),
        'princess': ('noun', 'princess')
        }
#定义一个scan扫描器        
def scan(sentence):
    words = sentence.split()
    result = []
    
    for word in words:
        if convert_number(word):
            result.append(('number', int(word)))
        elif word in lexicon.keys():    #判断每个单词与字典的key是否对应
            result.append(lexicon[word])    #返回key对应的元组
        else:
            result.append(('error', word))
            
    return result