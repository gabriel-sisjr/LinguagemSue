from Visitor import *
import SymbolTable as st

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
    else:
        return None

class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')

    def visitFuncDeclConcrete(self, funcDeclConcrete):
        funcDeclConcrete.signature.accept(self)
        funcDeclConcrete.body.accept(self)

    def visitSignatureConcrete(self, signatureConcrete):
        params = {}
        if (signatureConcrete.sigParams!= None):
            params = signatureConcrete.sigParams.accept(self)
            st.addFunction(signatureConcrete.id, params, signatureConcrete.type)
        else:
            st.addFunction(signatureConcrete.id, params, signatureConcrete.type)
        st.beginScope(signatureConcrete.id)
        for k in range(0, len(params), 2):
            st.addVar(params[k], params[k+1])

    def visitSingleSigParams(self, singleSigParams):
        return [singleSigParams.id, singleSigParams.type]

    def visitCompoundSigParams(self, compoundSigParams):
        return [compoundSigParams.id, compoundSigParams.type] + compoundSigParams.sigParams.accept(self)

    def visitBodyConcrete(self, bodyConcrete):
        if (bodyConcrete.stms != None):
            bodyConcrete.stms.accept(self)

    def visitSingleStm(self, singlestm):
        singlestm.stm.accept(self)

    def visitCompoundStm(self, compoundStm):
        compoundStm.stm.accept(self)
        compoundStm.stms.accept(self)

    def visitStmExp(self, stmExp):
        stmExp.exp.accept(self)

    def visitStmWhile(self, stmWhile):
        type = stmWhile.exp.accept(self)
        if (type != st.BOOL):
            stmWhile.exp.accept(self.printer)
            print ("\n\t[Erro] A expressao ", end='')
            stmWhile.exp.accept(self.printer)
            print(" eh", type, end='')
            print (". Deveria ser boolean\n")
        stmWhile.block.accept(self)

    def visitStmIf(self, stmIf):
        type = stmIf.exp.accept(self)
        if(type != st.BOOL):
            stmIf.exp.accept(self.printer)
            print ("\n\t[Erro] A expressao ", end='')
            stmIf.exp.accept(self.printer)
            print(" eh", type, end='')
            print (". Deveria ser boolean\n")
        if(stmIf.stm != None):
            stmIf.stm.accept(self)
        if(stmIf.block != None):
            stmIf.block.accept(self)
        if(stmIf.stm2 != None):
            stmIf.stm2.accept(self)
        if(stmIf.block2 != None):
            stmIf.block2.accept(self)

    def visitStmReturn(self, stmReturn):
        typeExp = stmReturn.exp.accept(self)
        scope = st.symbolTable[-1][st.SCOPE]
        bindable = st.getBindable(scope)
        if (typeExp != bindable[st.TYPE]):
            stmReturn.accept(self.printer)
            print('\t[Erro] O retorno da funcao', scope, 'eh do tipo', bindable[st.TYPE],end='')
            print(' no entanto, o retorno passado foi do tipo', typeExp, '\n')
        st.endScope()

    def visitAssignExp(self, assignExp):
        typeVar = assignExp.exp2.accept(self)
        if (isinstance(assignExp.exp1, sa.IdExp)):
            st.addVar(assignExp.exp1.id, typeVar)
            return typeVar
        return None

    def visitSomaExp(self, somaExp):
        tipoExp1 = somaExp.exp1.accept(self)
        tipoExp2 = somaExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            somaExp.accept(self.printer)
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            somaExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            somaExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c

    def visitSubtracaoExp(self, subtracaoExp):
        tipoExp1 = subtracaoExp.exp1.accept(self)
        tipoExp2 = subtracaoExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            subtracaoExp.accept(self.printer)
            print('\n\t[Erro] Subtracao invalida. A expressao ', end='')
            subtracaoExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            subtracaoExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c

    def visitMulExp(self, mulExp):
        tipoExp1 = mulExp.exp1.accept(self)
        tipoExp2 = mulExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            mulExp.accept(self.printer)
            print('\n\t[Erro] Multiplicacao invalida. A expressao ', end='')
            mulExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            mulExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitDivExp(self, divisaoExp):
        tipoExp1 = divisaoExp.exp1.accept(self)
        tipoExp2 = divisaoExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            divisaoExp.accept(self.printer)
            print('\n\t[Erro] Divisao invalida. A expressao ', end='')
            divisaoExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            divisaoExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitLdescExp(self, LdescExp):
        tipoExp1 = LdescExp.exp1.accept(self)
        tipoExp2 = LdescExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            LdescExp.accept(self.printer)
            print('\n\t[Erro] Desdencia pela esquerda invalida. A expressao ', end='')
            LdescExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            LdescExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitRdescExp(self, RdescExp):
        tipoExp1 = RdescExp.exp1.accept(self)
        tipoExp2 = RdescExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            RdescExp.accept(self.printer)
            print('\n\t[Erro] Desdencia pela direita invalida. A expressao ', end='')
            RdescExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            RdescExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitDiferencaExp(self, DiferencaExp):
        tipoExp1 = DiferencaExp.exp1.accept(self)
        tipoExp2 = DiferencaExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            DiferencaExp.accept(self.printer)
            print('\n\t[Erro] Diferença invalida. A expressao ', end='')
            DiferencaExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            DiferencaExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitPotExp(self, potExp):
        tipoExp1 = potExp.exp1.accept(self)
        tipoExp2 = potExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            potExp.accept(self.printer)
            print('\n\t[Erro] Potencia invalida. A expressao ', end='')
            potExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            potExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitMenorQueExp(self, menorQueExp):
        tipoExp1 = menorQueExp.exp1.accept(self)
        tipoExp2 = menorQueExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            menorQueExp.accept(self.printer)
            print('\n\t[Erro] Menor que invalido. A expressao ', end='')
            menorQueExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            menorQueExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitMaiorQueExp(self, maiorQueExp):
        tipoExp1 = maiorQueExp.exp1.accept(self)
        tipoExp2 = maiorQueExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            maiorQueExp.accept(self.printer)
            print('\n\t[Erro] Maior que invalido. A expressao ', end='')
            maiorQueExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            maiorQueExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitMenorIgualExp(self, menorIgualExp):
        tipoExp1 = menorIgualExp.exp1.accept(self)
        tipoExp2 = menorIgualExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            menorIgualExp.accept(self.printer)
            print('\n\t[Erro] MenorIgual invalido. A expressao ', end='')
            menorIgualExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            menorIgualExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitMaiorIgualExp(self, maiorIgualExp):
        tipoExp1 = maiorIgualExp.exp1.accept(self)
        tipoExp2 = maiorIgualExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            maiorIgualExp.accept(self.printer)
            print('\n\t[Erro] MaiorIgual invalido. A expressao ', end='')
            maiorIgualExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            maiorIgualExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitDuploIgualExp(self, duploIgualExp):
        tipoExp1 = duploIgualExp.exp1.accept(self)
        tipoExp2 = duploIgualExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            duploIgualExp.accept(self.printer)
            print('\n\t[Erro] Duplo Igual invalido. A expressao ', end='')
            duploIgualExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            duploIgualExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitDiferenteExp(self, diferenteExp):
        tipoExp1 = diferenteExp.exp1.accept(self)
        tipoExp2 = diferenteExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            diferenteExp.accept(self.printer)
            print('\n\t[Erro] Diferente invalido. A expressao ', end='')
            diferenteExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            diferenteExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitAndExp(self, andExp):
        tipoExp1 = andExp.exp1.accept(self)
        tipoExp2 = andExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            andExp.accept(self.printer)
            print('\n\t[Erro] And invalido. A expressao ', end='')
            andExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            andExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c
    
    def visitOrExp(self, orExp):
        tipoExp1 = orExp.exp1.accept(self)
        tipoExp2 = orExp.exp2.accept(self)
        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            orExp.accept(self.printer)
            print('\n\t[Erro] Or invalido. A expressao ', end='')
            orExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            orExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2,'\n')
        return c

    def visitCallExp(self, callExp):
        callExp.call.accept(self)

    def visitNumExp(self, numExp):
        if (isinstance(numExp.num, int)):
            return st.INT
        elif (isinstance(numExp.num, float)):
            return st.FLOAT

    def visitIdExp(self, idExp):
        idName = st.getBindable(idExp.id)
        if (idName != None):
            return idName[st.TYPE]
        return None

    def visitBooleanExp(self, booleanExp):
        return st.BOOL

    def visitParamsCall(self, paramsCall):
        bindable = st.getBindable(paramsCall.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            typeParams = paramsCall.params.accept(self)
            if (list(bindable[st.PARAMS][1::2]) == typeParams):
                return bindable[st.TYPE]
            paramsCall.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao invalida. Tipos passados na chamada sao:", typeParams)
            print('\tenquanto que os tipos definidos no metodo sao:', bindable[st.PARAMS][1::2], '\n')
        else:
            paramsCall.accept(self.printer)
            print("\n\t[Erro] Chamada de funcao invalida. O id", paramsCall.id,
                  "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None

    def visitNoParamsCall(self, simpleCall):
        bindable = st.getBindable(simpleCall.id)
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            return bindable[st.TYPE]
        simpleCall.accept(self.printer)
        print("\n\t[Erro] Chamada de funcao invalida. O id", simpleCall.id, "nao eh de uma funcao, nao foi definido ou foi definido apos esta funcao\n")
        return None

    def visitCompoundParams(self, compoundParams):
        return [compoundParams.exp.accept(self)] + compoundParams.params.accept(self)

    def visitSingleParam(self, singleParam):
        return [singleParam.exp.accept(self)]


def main():
    f = open("input1.su", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    svisitor = SemanticVisitor()
    for r in result:
        r.accept(svisitor)


if __name__ == "__main__":
    main()