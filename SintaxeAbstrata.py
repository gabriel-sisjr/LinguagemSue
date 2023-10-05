from abc import abstractmethod
from abc import ABCMeta

'''
Declaracao de funcao
FuncDecl
'''
class FuncDecl(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class FuncDeclConcrete(FuncDecl):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        return visitor.visitFuncDeclConcrete(self)

'''
Assinatura de funcao
Signature
'''
class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class SignatureConcrete(Signature):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitSignatureConcrete(self)
'''
Parametros de assinatura de funcao
SigParams
'''

class SigParams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleSigParams(SigParams):
    def __init__(self, type, id):
        self.type = type
        self.id = id
    def accept(self, visitor):
        return visitor.visitSingleSigParams(self)


class CompoundSigParams(SigParams):
    def __init__(self, type, id, sigParams):
        self.type = type
        self.id = id
        self.sigParams = sigParams
    def accept(self, visitor):
        return visitor.visitCompoundSigParams(self)

'''
Corpo de uma funcao
Body
'''

class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class BodyConcrete(Body):
    def __init__(self, stms):
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitBodyConcrete(self)

'''
Comandos
Stms
'''

class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SingleStm(Stms):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitSingleStm(self)

class CompoundStm(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        return visitor.visitCompoundStm(self)

'''
Comando
Stm
'''

class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class StmExp(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmExp(self)

class StmWhile(Stm):
    def __init__(self, exp, block):
        self.exp = exp
        self.block = block
    def accept(self, visitor):
        return visitor.visitStmWhile(self)

class StmReturn(Stm):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitStmReturn(self)

class StmForSingle(Stm):
    def __init__(self, exp, exp2, exp3, stm):
        self.exp = exp
        self.exp2 = exp2
        self.exp3 = exp3
        self.stm = stm
    def accept(self, visitor):
        return visitor.visitStmForSingle(self)
    
class StmForBlock(Stm):
    def __init__(self, exp, exp2, exp3, block):
        self.exp = exp
        self.exp2 = exp2
        self.exp3 = exp3
        self.block = block
    def accept(self, visitor):
        return visitor.visitStmForBlock(self)

class StmIf(Stm):
    def __init__(self, label):
        self.label = label
    def accept(self, visitor):
        return visitor.visitStmGoTo(self)



class StmGoTo(Stm):
    def __init__(self, label):
        self.label = label
    def accept(self, visitor):
        return visitor.visitStmGoTo(self)

class StmContinue(Stm):
    def accept(self, visitor):
        return visitor.visitStmContinue(self)

class StmBreak(Stm):
    def accept(self, visitor):
        return visitor.visitStmBreak(self)

'''
Expressoes
Exp
'''

class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAssignExp(self)

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitSomaExp(self)

class SubtracaoExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitSubtracaoExp(self)

class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMulExp(self)

class DivExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitDivExp(self)

class LdescExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitLdescExp(self)
class RdescExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitRdescExp(self)
class DiferancaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitDiferencaExp(self)
class PotExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitPotExp(self)

class MenorQueExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMenorQueExp(self)
    
class MaiorQueExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMaiorQueExp(self)
    
class MenorIgualExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMenorIgualExp(self)

class MaiorIgualExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitMaiorIgualExp(self)
    
class DuploIgualExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitDuploIgualExp(self)

class DiferenteExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitDiferenteExp(self)  
class AndExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitAndExp(self)
    
class OrExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitOrExp(self)

class CallExp(Exp, Stm):
    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        return visitor.visitCallExp(self)

class NumExp(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor):
        return visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitIdExp(self)

class BooleanExp(Exp):
    def __init__(self, boolValue):
        self.boolValue = boolValue
    def accept(self, visitor):
        return visitor.visitBooleanExp(self)

'''
Chamada de funcao
Call
'''
class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParamsCall(Call):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def accept(self, visitor):
        return visitor.visitParamsCall(self)

class NoParamsCall(Call):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        return visitor.visitNoParamsCall(self)


'''
Parametros de uma chamada de funcao
Params
'''
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        return visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        return visitor.visitSingleParam(self)


