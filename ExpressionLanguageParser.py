# Rascunho da gramatica
# program → funcdecl | funcdecl program
# funcdecl → signature body
# signature → id id ( sigParams)
# sigparams → ID ID | ID ID COMMA sigparams
# body → { stms }
# stms → stm  | stm  stms
# stm → exp ;  | while ( exp ) body | return exp ;
# call → id ( params )
# exp → exp + exp | exp * exp | exp ^ exp | call | assign | num | id
# call → id (params) | id ( )
# params → exp, params | exp
# assign → id = exp
import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

def p_program(p):
    '''program : funcdecl
                | funcdecl program
                '''
    if (len(p) == 3):
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_funcdecl(p):
    '''funcdecl : signature body'''
    p[0] = sa.FuncDeclConcrete(p[1], p[2])

def p_signature(p):
    '''signature : ID ID LPAREN sigparams RPAREN
                 | ID ID LPAREN RPAREN'''
    if (isinstance(p[4], sa.SigParams)):
        p[0] = sa.SignatureConcrete(p[1], p[2], p[4])
    else:
        p[0] = sa.SignatureConcrete(p[1], p[2], None)

def p_sigparams(p):
    '''sigparams : ID ID
                  | ID ID COMMA sigparams
    '''
    if (len(p) == 3):
        p[0] = sa.SingleSigParams(p[1], p[2])
    else:
        p[0] = sa.CompoundSigParams(p[1], p[2], p[4])

def p_body(p):
    ''' body : LCHAV stms RCHAV
             | LCHAV RCHAV'''
    if (len(p) == 4):
        p[0] = sa.BodyConcrete(p[2])
    else:
        p[0] = sa.BodyConcrete(None)

def p_stms(p):
    ''' stms : stm
            | stm stms'''
    if (len(p) == 2):
        p[0] = sa.SingleStm(p[1])
    else:
        p[0] = sa.CompoundStm(p[1], p[2])

def p_stm(p):
    ''' stm :  exp PV '''
    p[0] = sa.StmExp(p[1])

def p_stm_while(p):
    ''' stm : WHILE LPAREN opt_exp RPAREN body'''
    p[0] = sa.StmWhile(p[3], p[5])

def p_stm_return(p):
    ''' stm : RETURN exp PV '''
    p[0] = sa.StmReturn(p[2])

def p_stm_forSingle(p):
    ''' stm : FOR LPAREN opt_exp PV opt_exp PV opt_exp RPAREN stm '''
    p[0] = sa.StmForSingle(p[3], p[5], p[7], p[9]);

def p_stm_forBlock(p):
    ''' stm : FOR LPAREN opt_exp PV opt_exp PV opt_exp RPAREN body '''
    p[0] = sa.StmForBlock(p[3], p[5], p[7], p[9]);

def p_stm_if(p):
    ''' stm : IF LPAREN exp RPAREN body optElse
            | IF LPAREN exp RPAREN stm optElse '''

def p_stm_optElse(p):
    ''' optElse : ELSE body
                | ELSE stm
                | '''

def p_stm_GoTo(p):
    ''' stm : GOTO ID PV '''
    p[0] = sa.StmGoTo(p[2])

def p_stm_break(p):
    ''' stm : BREAK '''
    p[0] = sa.StmBreak()

def p_stm_continue(p):
    ''' stm : CONTINUE '''
    p[0] = sa.StmContinue()

def p_opt_exp(p):
    ''' opt_exp : exp
                | '''
    if len(p) == 2:
        p[0] = p[1]

def p_exp(p):
    '''exp : exp IGUAL exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.AssignExp(p[1], p[3])

def p_exp_soma(p):
    '''exp : exp SOMA exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.SomaExp(p[1], p[3])

def p_exp_subtracao(p):
    '''exp : exp SUBTRACAO exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.SubtracaoExp(p[1], p[3])

def p_exp_multiplicacao(p):
    '''exp : exp VEZES exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.MulExp(p[1], p[3])

def p_exp_divisao(p):
    '''exp : exp BARRA exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.DivExp(p[1], p[3])

def p_exp_potencia(p):
    '''exp : exp POT exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.PotExp(p[1], p[3])

def p_exp_diferenca(p):
    '''exp : exp DIFERENCA exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.DiferancaExp(p[1], p[3])

def p_exp_Ldesc(p):
    '''exp : exp DESLOCAMENTOESQ exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.LdescExp(p[1], p[3])

def p_exp_Rdesc(p):
    '''exp : exp DESLOCAMENTODIR exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.RdescExp(p[1], p[3])

def p_exp_menorQue(p):
    '''exp : exp MENORQUE exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.MenorQueExp(p[1], p[3])

def p_exp_maiorQue(p):
    '''exp : exp MAIORQUE exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.MaiorQueExp(p[1], p[3])

def p_exp_menorIgual(p):
    '''exp : exp MENORIGUAL exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.MenorIgualExp(p[1], p[3])

def p_exp_maiorIgual(p):
    '''exp : exp MAIORIGUAL exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.MaiorIgualExp(p[1], p[3])

def p_exp_igualDuplo(p):
    '''exp : exp IGUALDUPLO exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.DuploIgualExp(p[1], p[3])

def p_exp_diferente(p):
    '''exp : exp DIFERENTE exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.DiferenteExp(p[1], p[3])

def p_exp_and(p):
    '''exp : exp AND exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.AndExp(p[1], p[3])

def p_exp_or(p):
    '''exp : exp OR exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.OrExp(p[1], p[3])

def p_exp4_number(p):
    '''exp4 :  NUMBER '''
    p[0] = sa.NumExp(p[1])

def p_exp4_id(p):
    '''exp4 :  ID '''
    p[0] = sa.IdExp(p[1])

def p_exp4_boolean(p):
    '''exp4 :  TRUE
            |  FALSE '''
    p[0] = sa.BooleanExp(p[1])


def p_exp4_call(p):
    '''exp4 : call'''
    p[0] = sa.CallExp(p[1])


def p_call_id_params(p):
    '''call : ID LPAREN params RPAREN
            | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = sa.ParamsCall(p[1], p[3])
    else:
        p[0] = sa.NoParamsCall(p[1])


def p_params_ids(p):
    '''params : exp COMMA params
            | exp '''
    if len(p) == 2:
        p[0] = sa.SingleParam(p[1])
    elif len(p) == 4:
        p[0] = sa.CompoundParams(p[1], p[3])

def p_error(p):
    print("Syntax error in input!")


def main():
    f = open("input1.su", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()