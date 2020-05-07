import sys
from antlr4 import *
from gcode2Lexer import gcode2Lexer
from gcode2Parser import gcode2Parser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = gcode2Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gcode2Parser(stream)
    tree = parser.startRule()


if __name__ == '__main__':
    main(sys.argv)