#coding=utf-8

class ParserError(Exception):
    pass
    
    
class Sentence(object):
    
    def __init__(self, subject, verb, object):
    #这里用的是元组的第二个元素，元组组成为('noun', 'princess')
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

#识别下一个单词，并返回该单词
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

#将一个单词与语法相匹配，匹配则返回该单词        
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)
        #元组的格式，('noun', 'princess')
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

#skip无用的单词        
def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)
        
#match verb
def parse_verb(word_list):
    skip(word_list, 'stop')
    
    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError('Expected a verb next.')
        
#match object
def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)
    
    if next == 'noun':
        return match(word_list, 'noun')
    elif next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError('Expected a noun or direction next.')
        
#输入subject 返回组成sentence
def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    
    return Sentence(subj, verb, obj)
    
#直接进行sentence组成判断，该句子要以subj、obj或verb开头
def parse_sentence(word_list):
    skip(word_list, 'stop')
    start = peek(word_list)
    #开头有主语则进行匹配，没有则加上player
    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not:%s" %start)
    
        