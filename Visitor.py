from AbstractVisitor import AbstractVisitor
from ExpressionLanguageParser import *
# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def visitFuncDeclConcrete(self, funcDeclConcrete):
        funcDeclConcrete.signature.accept(self)
        funcDeclConcrete.body.accept(self)

    def visitSignatureConcrete(self, signatureConcrete):
        print (blank(), signatureConcrete.type, ' ', end='', sep='')
        print(signatureConcrete.id, '(', end = '', sep='')
        if (signatureConcrete.sigParams != None):
            signatureConcrete.sigParams.accept(self)
        print(')', end = '')

    def visitSingleSigParams(self, singleSigParams):
        print(singleSigParams.type, ' ', end='', sep='')
        print(singleSigParams.id, end='', sep='')

    def visitCompoundSigParams(self, compoundSigParams):
        print(compoundSigParams.type, ' ', end='', sep='')
        print(compoundSigParams.id, ', ', end='', sep='')
        compoundSigParams.sigParams.accept(self)

    def visitBodyConcrete(self, bodyConcrete):
        global tab
        print ('{ ')
        tab =  tab + 3
        if (bodyConcrete.stms != None):
            bodyConcrete.stms.accept(self)
        tab =  tab - 3
        print (blank(), '} ', sep='')

    def visitSingleStm(self, singleStm):
        singleStm.stm.accept(self)

    def visitCompoundStm(self, compoundStm):
        compoundStm.stm.accept(self)
        compoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        print(blank(),sep='',end='')
        stmExp.exp.accept(self)
        print('')

    def visitStmWhile(self, stmWhile):
        print (blank(), 'while (', end='', sep='')
        stmWhile.exp.accept(self)
        print (')', end='', sep='')
        stmWhile.block.accept(self)

    def visitStmReturn(self, stmReturn):
        print (blank(), 'return ', end='', sep='')
        stmReturn.exp.accept(self)
        print (';')

    def visitAssignExp(self, assignExp):
        # print("visitAssignExp")
        assignExp.exp1.accept(self)
        print(' = ', end='')
        assignExp.exp2.accept(self)

    def visitSomaExp(self, somaExp):
        # print("visitSomaExp")
        somaExp.exp1.accept(self)
        print(' + ', end='')
        somaExp.exp2.accept(self)

    def visitSubtracaoExp(self, subExp):
        # print("visitSubExp")
        subExp.exp1.accept(self)
        print(' - ', end='')
        subExp.exp2.accept(self)

    def visitDivExp(self, divExp):
        # print("visitDivExp")
        divExp.exp1.accept(self)
        print(' / ', end='')
        divExp.exp2.accept(self)

    def visitMulExp(self, mulExp):
        # print("visitMulExp")
        mulExp.exp1.accept(self)
        print(' * ', end='')
        mulExp.exp2.accept(self)

    def visitPotExp(self, potExp):
        # print("visitPotExp")
        potExp.exp1.accept(self)
        print(' ^ ', end='')
        potExp.exp2.accept(self)

    def visitDiferencaExp(self, difExp):
        # print("visitDiferencaExp")
        difExp.exp1.accept(self)
        print(' % ', end='')
        difExp.exp2.accept(self)
   
    def visitLdescExp(self, lDescExp):
        # print("visitLdescExp")
        lDescExp.exp1.accept(self)
        print(' << ', end='')
        lDescExp.exp2.accept(self)

    def visitRdescExp(self, rDescExp):
        # print("visitRdescExp")
        rDescExp.exp1.accept(self)
        print(' >> ', end='')
        rDescExp.exp2.accept(self)

    def visitMenorQueExp(self, menorExp):
        # print("visitMenorQueExp")
        menorExp.exp1.accept(self)
        print(' < ', end='')
        menorExp.exp2.accept(self)

    def visitMaiorQueExp(self, maiorExp):
        # print("visitMaiorQueExp")
        maiorExp.exp1.accept(self)
        print(' > ', end='')
        maiorExp.exp2.accept(self)

    def visitMenorIgualExp(self, menorIgaulExp):
        # print("visitMenorIgualExp")
        menorIgaulExp.exp1.accept(self)
        print(' <= ', end='')
        menorIgaulExp.exp2.accept(self)

    def visitMaiorIgualExp(self, maiorIgualExp):
        # print("visitMaiorIgualExp")
        maiorIgualExp.exp1.accept(self)
        print(' >= ', end='')
        maiorIgualExp.exp2.accept(self)

    def visitDuploIgualExp(self, duploIgualExp):
        # print("visitDuploIgualExp")
        duploIgualExp.exp1.accept(self)
        print(' == ', end='')
        duploIgualExp.exp2.accept(self)

    def visitDiferenteExp(self, difExp):
        # print("visitDiferenteExp")
        difExp.exp1.accept(self)
        print(' ! ', end='')
        difExp.exp2.accept(self)

    def visitAndExp(self, andExp):
        # print("visitAndExp")
        andExp.exp1.accept(self)
        print(' && ', end='')
        andExp.exp2.accept(self)

    def visitOrExp(self, orExp):
        # print("visitOrExp")
        orExp.exp1.accept(self)
        print(' || ', end='')
        orExp.exp2.accept(self)

    def visitStmForSingle(self, stm):
        print('for (', end='')
        stm.exp.accept(self)
        print(';', end='')
        stm.exp2.accept(self)
        print(';', end='')
        stm.exp3.accept(self)
        print(')', end='')

    def visitStmForBlock(self, block):
        print('for (', end='')
        block.exp.accept(self)
        print(';', end='')
        block.exp2.accept(self)
        print(';', end='')
        block.exp3.accept(self)
        print(')', end='')

    def visitStmIf(self, stm):
        global tab
        print(blank(), 'if (', end='')
        stm.exp.accept(self)
        print(') \n', end='')
        tab =  tab + 3
        if(stm.stm != None):
            stm.stm.accept(self)
        if(stm.block != None):
            stm.block.accept(self)
        tab =  tab - 3
        print(blank(), 'else \n', end='')
        tab =  tab + 3
        if(stm.stm2 != None):
            stm.stm2.accept(self)
        if(stm.block2 != None):
            stm.block2.accept(self)
        tab =  tab - 3

    def visitCallExp(self, callExp):
        # print("visitCallExp")
        callExp.call.accept(self)

    def visitNumExp(self, numExp):
        # print("visitNumExp")
        print(numExp.num, end='')

    def visitIdExp(self, idExp):
        # print("visitIdExp")
        print(idExp.id, end='')

    def visitBooleanExp(self, booleanExp):
        print(booleanExp.boolValue, end='')

    def visitParamsCall(self, paramsCall):
        # print("visitParamsCall")
        print(paramsCall.id, '(', end='', sep='')
        paramsCall.params.accept(self)
        print(')', end='')

    def visitNoParamsCall(self, simpleCall):
        # print("visitSimpleCall")
        print(blank(), simpleCall.id, '()', end='', sep='')

    def visitCompoundParams(self, compoundParams):
        # print("visitCompoundParams")
        compoundParams.exp.accept(self)
        print(', ', end='')
        compoundParams.params.accept(self)

    def visitSingleParam(self, singleParam):
        # print("visitSingleParam")
        singleParam.exp.accept(self)


def main():
    f = open("input1.su", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
    for r in result:
        r.accept(visitor)

if __name__ == "__main__":
    main()