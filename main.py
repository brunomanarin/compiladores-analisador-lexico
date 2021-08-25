#!/usr/bin/env python
# -*- coding: utf-8 -*-

from buffer import Buffer
from lexicalAnalyzer import LexicalAnalyzer

if __name__ == '__main__':
    Buffer = Buffer()
    Analyzer = LexicalAnalyzer()

    token = []
    lexeme = []

    for i in Buffer.load_buffer():
        t, lex = Analyzer.tokenize(i)
        token += t
        lexeme += lex

    counterLexeme = 0
    foundLexemes = []
    countedLexemes = []
    lexemeLines = []

    for x in lexeme:
        for y in lexeme:
            if x[0] == y[0]:
                counterLexeme += 1
                if y[1] not in lexemeLines:
                    lexemeLines.append(y[1])
        if x[0] not in foundLexemes:
            foundLexemes.append(x[0])
            countedLexemes.append([x[0], counterLexeme, lexemeLines])
        lexemeLines = []
        counterLexeme = 0
    
    for lexeme in countedLexemes:
        print('IDENT = {0}, Count = \'{1}\' in Lines = {2}'.format(lexeme[0], lexeme[1], lexeme[2]))

    print('\nLista de tokens: ', token)