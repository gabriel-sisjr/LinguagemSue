# -------------------------
# ExpressionLanguageLex.py
#----------------------
import ply.lex as lex
reservadas = {
   'while' : 'WHILE',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'return' : 'RETURN'
}
tokens = ['COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN',
          'RPAREN', 'IGUAL', 'LCHAV', 'RCHAV', 'PV', 'DIVISAO', 'DIFERENCA', 'DESLOCAMENTOESQ',
          'DESLOCAMENTODIR','MENORQUE', 'MAIORQUE', 'MENORIGUAL', 'MAIORIGUAL',
          'IGUALDUPLO', 'DIFERENTE', 'BARRA', 'AND', 'OR'] + list(reservadas.values())

t_IGUAL= r'='
t_SOMA = r'\+'
t_VEZES = r'\*'
t_POT = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_LCHAV = r'{'
t_RCHAV = r'}'
t_PV = r';'
t_DIVISAO = r'\/'
t_DIFERENCA = r'\%'
t_DESLOCAMENTOESQ = r'\<\<'
t_DESLOCAMENTODIR = r'\>\>'
t_MENORQUE = r'<'
t_MAIORQUE = r'>'
t_MENORIGUAL = r'\<\='
t_MAIORIGUAL = r'\>\='
t_IGUALDUPLO = r'\=\='
t_DIFERENTE = r'\!\='
t_BARRA = r'\|'
t_AND = r'&&'
t_OR = r'\|\|'

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reservadas.get(t.value,'ID')
   return t

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)

def t_STRING(t):
    r'[\".*\"][\'.*\']'
    return t

t_ignore = ' \t'

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)


def main():
   f = open("input1.su", "r")
   lexer = lex.lex(debug=1)
   lexer.input(f.read())
   print('\n\n# lexer output:')
   for tok in lexer:
      print ('type:', tok.type, ', value:',tok.value)


if __name__ == "__main__":
   main()