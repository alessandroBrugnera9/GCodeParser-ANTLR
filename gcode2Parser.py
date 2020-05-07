# Generated from gcode2.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("N\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\t\5\t<\n\t\3\t\5\t?\n\t\3\n\3")
        buf.write("\n\3\n\5\nD\n\n\3\n\5\nG\n\n\3\13\5\13J\n\13\3\13\3\13")
        buf.write("\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\4\3\2\5\6\3\2\7")
        buf.write("\b\2K\2\27\3\2\2\2\4\35\3\2\2\2\6+\3\2\2\2\b-\3\2\2\2")
        buf.write("\n\62\3\2\2\2\f\64\3\2\2\2\16\66\3\2\2\2\208\3\2\2\2\22")
        buf.write("@\3\2\2\2\24I\3\2\2\2\26\30\5\6\4\2\27\26\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\34\5\4\3\2\34\3\3\2\2\2\35\36\5\b\5\2\36\37\5\n\6\2\37")
        buf.write("\5\3\2\2\2 !\5\b\5\2!\"\5\16\b\2\"#\5\20\t\2#$\5\22\n")
        buf.write("\2$%\5\24\13\2%,\3\2\2\2&\'\5\b\5\2\'(\5\f\7\2()\5\24")
        buf.write("\13\2),\3\2\2\2*,\5\24\13\2+ \3\2\2\2+&\3\2\2\2+*\3\2")
        buf.write("\2\2,\7\3\2\2\2-.\7\3\2\2./\7\r\2\2/\60\7\r\2\2\60\61")
        buf.write("\7\r\2\2\61\t\3\2\2\2\62\63\7\4\2\2\63\13\3\2\2\2\64\65")
        buf.write("\t\2\2\2\65\r\3\2\2\2\66\67\t\3\2\2\67\17\3\2\2\289\7")
        buf.write("\t\2\29;\7\r\2\2:<\7\r\2\2;:\3\2\2\2;<\3\2\2\2<>\3\2\2")
        buf.write("\2=?\7\r\2\2>=\3\2\2\2>?\3\2\2\2?\21\3\2\2\2@A\7\n\2\2")
        buf.write("AC\7\r\2\2BD\7\r\2\2CB\3\2\2\2CD\3\2\2\2DF\3\2\2\2EG\7")
        buf.write("\r\2\2FE\3\2\2\2FG\3\2\2\2G\23\3\2\2\2HJ\7\13\2\2IH\3")
        buf.write("\2\2\2IJ\3\2\2\2JK\3\2\2\2KL\7\f\2\2L\25\3\2\2\2\t\31")
        buf.write("+;>CFI")
        return buf.getvalue()


class gcode2Parser ( Parser ):

    grammarFileName = "gcode2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'N'", "'M30'", "'M02'", "'M01'", "'G01'", 
                     "'G00'", "'X'", "'Y'", "'\r'", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "ID", 
                      "WS" ]

    RULE_prg = 0
    RULE_fimprograma = 1
    RULE_statement = 2
    RULE_numerolinha = 3
    RULE_mfim = 4
    RULE_mfunc = 5
    RULE_codfunc = 6
    RULE_coordx = 7
    RULE_coordy = 8
    RULE_fimdelinha = 9

    ruleNames =  [ "prg", "fimprograma", "statement", "numerolinha", "mfim", 
                   "mfunc", "codfunc", "coordx", "coordy", "fimdelinha" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    INT=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PrgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fimprograma(self):
            return self.getTypedRuleContext(gcode2Parser.FimprogramaContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gcode2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(gcode2Parser.StatementContext,i)


        def getRuleIndex(self):
            return gcode2Parser.RULE_prg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrg" ):
                listener.enterPrg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrg" ):
                listener.exitPrg(self)




    def prg(self):

        localctx = gcode2Parser.PrgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 20
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 23 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 25
            self.fimprograma()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FimprogramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numerolinha(self):
            return self.getTypedRuleContext(gcode2Parser.NumerolinhaContext,0)


        def mfim(self):
            return self.getTypedRuleContext(gcode2Parser.MfimContext,0)


        def getRuleIndex(self):
            return gcode2Parser.RULE_fimprograma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFimprograma" ):
                listener.enterFimprograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFimprograma" ):
                listener.exitFimprograma(self)




    def fimprograma(self):

        localctx = gcode2Parser.FimprogramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fimprograma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.numerolinha()
            self.state = 28
            self.mfim()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numerolinha(self):
            return self.getTypedRuleContext(gcode2Parser.NumerolinhaContext,0)


        def codfunc(self):
            return self.getTypedRuleContext(gcode2Parser.CodfuncContext,0)


        def coordx(self):
            return self.getTypedRuleContext(gcode2Parser.CoordxContext,0)


        def coordy(self):
            return self.getTypedRuleContext(gcode2Parser.CoordyContext,0)


        def fimdelinha(self):
            return self.getTypedRuleContext(gcode2Parser.FimdelinhaContext,0)


        def mfunc(self):
            return self.getTypedRuleContext(gcode2Parser.MfuncContext,0)


        def getRuleIndex(self):
            return gcode2Parser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = gcode2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.numerolinha()
                self.state = 31
                self.codfunc()
                self.state = 32
                self.coordx()
                self.state = 33
                self.coordy()
                self.state = 34
                self.fimdelinha()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.numerolinha()
                self.state = 37
                self.mfunc()
                self.state = 38
                self.fimdelinha()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.fimdelinha()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumerolinhaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gcode2Parser.INT)
            else:
                return self.getToken(gcode2Parser.INT, i)

        def getRuleIndex(self):
            return gcode2Parser.RULE_numerolinha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumerolinha" ):
                listener.enterNumerolinha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumerolinha" ):
                listener.exitNumerolinha(self)




    def numerolinha(self):

        localctx = gcode2Parser.NumerolinhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_numerolinha)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(gcode2Parser.T__0)
            self.state = 44
            self.match(gcode2Parser.INT)
            self.state = 45
            self.match(gcode2Parser.INT)
            self.state = 46
            self.match(gcode2Parser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MfimContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcode2Parser.RULE_mfim

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMfim" ):
                listener.enterMfim(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMfim" ):
                listener.exitMfim(self)




    def mfim(self):

        localctx = gcode2Parser.MfimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_mfim)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(gcode2Parser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MfuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcode2Parser.RULE_mfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMfunc" ):
                listener.enterMfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMfunc" ):
                listener.exitMfunc(self)




    def mfunc(self):

        localctx = gcode2Parser.MfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            _la = self._input.LA(1)
            if not(_la==gcode2Parser.T__2 or _la==gcode2Parser.T__3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodfuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcode2Parser.RULE_codfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodfunc" ):
                listener.enterCodfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodfunc" ):
                listener.exitCodfunc(self)




    def codfunc(self):

        localctx = gcode2Parser.CodfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_codfunc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            _la = self._input.LA(1)
            if not(_la==gcode2Parser.T__4 or _la==gcode2Parser.T__5):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gcode2Parser.INT)
            else:
                return self.getToken(gcode2Parser.INT, i)

        def getRuleIndex(self):
            return gcode2Parser.RULE_coordx

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordx" ):
                listener.enterCoordx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordx" ):
                listener.exitCoordx(self)




    def coordx(self):

        localctx = gcode2Parser.CoordxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_coordx)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(gcode2Parser.T__6)
            self.state = 55
            self.match(gcode2Parser.INT)
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 56
                self.match(gcode2Parser.INT)


            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==gcode2Parser.INT:
                self.state = 59
                self.match(gcode2Parser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gcode2Parser.INT)
            else:
                return self.getToken(gcode2Parser.INT, i)

        def getRuleIndex(self):
            return gcode2Parser.RULE_coordy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordy" ):
                listener.enterCoordy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordy" ):
                listener.exitCoordy(self)




    def coordy(self):

        localctx = gcode2Parser.CoordyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_coordy)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(gcode2Parser.T__7)
            self.state = 63
            self.match(gcode2Parser.INT)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 64
                self.match(gcode2Parser.INT)


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==gcode2Parser.INT:
                self.state = 67
                self.match(gcode2Parser.INT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FimdelinhaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gcode2Parser.RULE_fimdelinha

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFimdelinha" ):
                listener.enterFimdelinha(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFimdelinha" ):
                listener.exitFimdelinha(self)




    def fimdelinha(self):

        localctx = gcode2Parser.FimdelinhaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_fimdelinha)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==gcode2Parser.T__8:
                self.state = 70
                self.match(gcode2Parser.T__8)


            self.state = 73
            self.match(gcode2Parser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





