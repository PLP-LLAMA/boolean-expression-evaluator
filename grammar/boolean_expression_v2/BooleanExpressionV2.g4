grammar BooleanExpressionV2;

// Parser rules
expr
    : expr OR expr           # OrExpr
    | expr AND expr          # AndExpr
    | NOT expr               # NotExpr
    | expr '<' expr          # LessThanExpr
    | expr '>' expr          # GreaterThanExpr
    | expr '==' expr         # EqualsExpr
    | expr '!=' expr         # NotEqualsExpr
    | '(' expr ')'           # ParenExpr
    | IDENTIFIER             # VarExpr
    | BOOL                   # BoolExpr
    | NUMBER                 # NumberExpr
    ;

// Lexer rules
AND         : 'AND';
OR          : 'OR';
NOT         : 'NOT';
BOOL        : 'true' | 'false';
IDENTIFIER  : [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER      : [0-9]+;
WS          : [ \t\r\n]+ -> skip;