grammar BooleanExpression;

// The entry point of the grammar
program: statement*;

statement: declaration | expression;

declaration:
	'bool' ID '=' expression ';'; // Variable declaration with a Boolean value

expression:
	expression 'AND' expression // AndExpr
	| expression 'OR' expression // OrExpr
	| 'NOT' expression // NotExpr
	| expression comparisonOp expression // Comparison (==, !=, <, >)
	| '(' expression ')' // Parentheses for grouping
	| ID // Variable
	| 'true' // Boolean literal true
	| 'false' ; // Boolean literal false

comparisonOp: '==' | '!=' | '<' | '>'; // Comparison operators

ID: [a-zA-Z_][a-zA-Z_0-9]*; // Variable name (identifier)

WS: [ \t\r\n]+ -> skip; // Skip whitespaces