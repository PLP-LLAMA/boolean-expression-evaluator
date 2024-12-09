// example: calculator - grammar reference:
// https://medium.com/@kv391/antlr4-grammar-a-quick-tutorial-e1f0fb6ca4ff

grammar Calculator;

// Parser rules
expr: term (('+' | '-') term)*;
term: factor (('*' | '/') factor)*;
factor: NUMBER | '(' expr ')' | ('-' | '+') factor;

// Lexer rules
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;