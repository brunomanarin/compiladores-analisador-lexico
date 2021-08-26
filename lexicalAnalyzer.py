import re
class LexicalAnalyzer:
    lin_num = 1

    def tokenize(self, code):
        rules = [
            ('DEF', r'def'),            # def
            ('INT', r'int'),            # int
            ('FLOAT', r'float'),        # float
            ('IF', r'if'),              # if
            ('ELSE', r'else'),          # else
            ('READ', r'read'),          # read
            ('PRINT', r'print'),        # print
            ('RETURN', r'return'),      # return
            ('LBRACKET', r'\('),        # (
            ('RBRACKET', r'\)'),        # )
            ('LBRACE', r'\{'),          # {
            ('RBRACE', r'\}'),          # }
            ('LARRAY', r'\['),          # [
            ('RARRAY', r'\]'),          # ]
            ('COMMA', r','),            # ,
            ('PCOMMA', r';'),           # ;
            ('EQ', r'=='),              # ==
            ('NE', r'!='),              # !=
            ('LE', r'<='),              # <=
            ('GE', r'>='),              # >=
            ('ATTR', r'\='),            # =
            ('LT', r'<'),               # <
            ('GT', r'>'),               # >
            ('PLUS', r'\+'),            # +
            ('MINUS', r'-'),            # -
            ('MULT', r'\*'),            # *
            ('DIV', r'\/'),             # /
            ('MOD', r'%'),              # %
            ('IDENT', r'[a-zA-Z]\w*'),     # IDENTIFIERS
            ('FLOAT_CONST', r'\d(\d)*\.\d(\d)*'),   # FLOAT
            ('INTEGER_CONST', r'\d(\d)*'),          # INT
            ('STRING_CONST', r'["][\w\W\d\D\s]*["]'), # STRING
            ('NEWLINE', r'\n'),         # NEW LINE
            ('SKIP', r'[ \t]+'),        # SPACE and TABS
            ('MISMATCH', r'.'),         # ANOTHER CHARACTER
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)

        token = []
        lexeme = []

        for m in re.finditer(tokens_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                self.lin_num += 1
            elif token_type == 'SKIP':
                continue
            elif token_type == 'MISMATCH':
                raise RuntimeError('%r unexpected on line %d' % (token_lexeme, self.lin_num))
            elif token_type == 'IDENT':
                lexeme.append([token_lexeme, self.lin_num])

            token.append(token_type)
        return token, lexeme

                