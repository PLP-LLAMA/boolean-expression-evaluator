# example: hello
# reference: https://yetanotherprogrammingblog.medium.com/antlr-with-python-974c756bdb1b

import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)


from antlr4 import InputStream, CommonTokenStream
from grammar.hello.HelloLexer import HelloLexer
from grammar.hello.HelloParser import HelloParser

input_text = input("> ")
lexer = HelloLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = HelloParser(stream)

tree = parser.r()

print(tree.toStringTree(recog=parser))
