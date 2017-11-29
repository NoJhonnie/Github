from nose.tools import *
from ex48 import parse

def test_Sentence():
    parser = parse.Sentence(('noun', 'bear'), ('verb', 'go'), ('direction', 'north'))
    
    assert_equal(parser.subject, 'bear')
    assert_equal(parser.verb, 'go')
    assert_equal(parser.object, 'north')
    
def test_peek():
    assert_equal(parse.peek([('direction', 'north'), ('verb', 'go')]), 'direction')
    assert_equal(parse.peek([('verb', 'go')]), 'verb')
    assert_equal(parse.peek([('noun', 'bear')]), 'noun')
    assert_equal(parse.peek([]), None)
    
def test_match():
    assert_equal(parse.match([('direction', 'north')], 'direction'), ('direction', 'north'))
    assert_equal(parse.match([('verb', 'go')], 'noun'), None)
    assert_equal(parse.match([('noun', 'bear')], 'noun'), ('noun', 'bear'))
    assert_equal(parse.match([('stop', 'princess'), ('number', 123)], 'stop'), ('stop', 'princess'))
    assert_equal(parse.match([('stop', 'princess'), ('number', 123)], 'number'), None)
    assert_equal(parse.match([('stop', 'princess'), ('number', 123)], 'noun'), None)
    assert_equal(parse.match([], 'noun'), None)
    
def test_parse_verb():
    assert_equal(parse.parse_verb([('stop', 'the'), ('verb', 'go'), ('direction', 'north')]), ('verb', 'go'))
    assert_equal(parse.parse_verb([('verb', 'go'), ('direction', 'north')]), ('verb', 'go'))
    assert_raises(parse.ParserError, parse.parse_verb, [('noun', 'bear'), ('number', 1234)])
    
def test_parse_object():
    assert_equal(parse.parse_object([('stop', 'of'), ('noun', 'bear'), ('direction', 'north')]), ('noun', 'bear'))
    assert_equal(parse.parse_object([('direction', 'north'), ('stop', 'of'), ('verb', 'go')]), ('direction', 'north'))
    assert_raises(parse.ParserError, parse.parse_object, [('stop', 'of'), ('verb', 'go'), ('direction', 'north')])
    
def test_parse_subject():
    sub = parse.parse_subject([('verb', 'go'), ('direction', 'north'), ('stop', 'of')], ('noun', 'bear'))
    assert_equal(sub.subject, 'bear')
    assert_equal(sub.verb, 'go')
    assert_equal(sub.object, 'north')
    
def test_parse_sentence():
    sen1 = parse.parse_sentence([('noun', 'bear'), ('verb', 'go'), ('direction', 'north')])
    assert_equal(sen1.subject, 'bear')
    assert_equal(sen1.verb, 'go')
    assert_equal(sen1.object, 'north')
    
    sen2 = parse.parse_sentence([('verb', 'kill'), ('direction', 'bear')])
    assert_equal(sen2.subject, 'player')
    assert_equal(sen2.verb, 'kill')
    assert_equal(sen2.object, 'bear')
    
    assert_raises(parse.ParserError, parse.parse_sentence, [('stop', 'in'), ('direction', 'north')])