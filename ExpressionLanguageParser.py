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

def p_stm_ifSingle(p):
    ''' stm : IF LPAREN exp RPAREN stm optElse '''
    if(p[6] != None):
        p[6].exp = p[3]
        p[6].stm = p[5]
        p[0] = p[6]
    else:
        p[0] = sa.StmIf(p[3], stm=p[5]);

def p_stm_ifBlock(p): 
    ''' stm : IF LPAREN exp RPAREN body optElse '''
    if(p[6] != None):
        p[6].exp = p[3]
        p[6].stm = p[5]
        p[0] = p[6]
    else:
        p[0] = sa.StmIf(p[3], block=p[5]);

def p_stm_optElseBlock(p):
    ''' optElse : ELSE body
                | '''
    if(len(p) == 2):
        p[0] = sa.StmIf(block2=p[2]) 

def p_stm_optElseSingle(p):
    ''' optElse : ELSE stm '''
    p[0] = sa.StmIf(stm2=p[2]) 

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

def p_exp_potencia(p):
    '''exp8 : exp8 POT exp9
         | exp9'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.PotExp(p[1], p[3])

def p_exp_multiplicacao(p):
    '''exp7 : exp7 VEZES exp8
         | exp8'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.MulExp(p[1], p[3])

def p_exp_divisao(p):
    '''exp7 : exp7 BARRA exp8 '''
    p[0] = sa.DivExp(p[1], p[3])

def p_exp_diferenca(p):
    '''exp7 : exp7 DIFERENCA exp8 '''
    p[0] = sa.DiferancaExp(p[1], p[3])

def p_exp_soma(p):
    '''exp6 : exp6 SOMA exp7
         | exp7'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.SomaExp(p[1], p[3])

def p_exp_subtracao(p):
    '''exp6 : exp6 SUBTRACAO exp7 '''
    p[0] = sa.SubtracaoExp(p[1], p[3])

def p_exp_Ldesc(p):
    '''exp5 : exp5 DESLOCAMENTOESQ exp6
         | exp6'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.LdescExp(p[1], p[3])

def p_exp_Rdesc(p):
    '''exp5 : exp5 DESLOCAMENTODIR exp6 '''
    p[0] = sa.RdescExp(p[1], p[3])

def p_exp_menorQue(p):
    '''exp4 : exp4 MENORQUE exp5 '''
    p[0] = sa.MenorQueExp(p[1], p[3])

def p_exp_maiorQue(p):
    '''exp4 : exp4 MAIORQUE exp5 '''
    p[0] = sa.MaiorQueExp(p[1], p[3])

def p_exp_menorIgual(p):
    '''exp4 : exp4 MENORIGUAL exp5 '''
    p[0] = sa.MenorIgualExp(p[1], p[3])

def p_exp_maiorIgual(p):
    '''exp4 : exp4 MAIORIGUAL exp5
         | exp5'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.MaiorIgualExp(p[1], p[3])

def p_exp_igualDuplo(p):
    '''exp3 : exp3 IGUALDUPLO exp4
            | exp4 '''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.DuploIgualExp(p[1], p[3])

def p_exp_diferente(p):
    '''exp3 : exp3 DIFERENTE exp4 '''
    p[0] = sa.DiferenteExp(p[1], p[3])

def p_exp_and(p):
    '''exp2 : exp2 AND exp3
         | exp3'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.AndExp(p[1], p[3])

def p_exp_or(p):
    '''exp1 : exp1 OR exp2
         | exp2'''
    if len(p) == 2:
        p[0] = p[1]
    else:
       p[0] = sa.OrExp(p[1], p[3])

def p_exp(p):
    '''exp : exp IGUAL exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.AssignExp(p[1], p[3])

def p_exp9_number(p):
    '''exp9 :  NUMBER '''
    p[0] = sa.NumExp(p[1])

def p_exp9_id(p):
    '''exp9 :  ID '''
    p[0] = sa.IdExp(p[1])

def p_exp9_boolean(p):
    '''exp9 :  TRUE
            |  FALSE '''
    p[0] = sa.BooleanExp(p[1])


def p_exp9_call(p):
    '''exp9 : call'''
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