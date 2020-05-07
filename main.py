import sys
from antlr4 import *
from gcode2Lexer import gcode2Lexer
from gcode2Parser import gcode2Parser
from gcode2Listener import gcode2Listener


def main(argv):
    input_stream = FileStream(argv)
    lexer = gcode2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gcode2Parser(stream)
    tree = parser.prg()

    listener = gcode2Listener()

    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    # print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    # main(sys.argv)
    main("input.txt")