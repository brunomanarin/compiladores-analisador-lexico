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

    print('\nRecognize Tokens: ', token)