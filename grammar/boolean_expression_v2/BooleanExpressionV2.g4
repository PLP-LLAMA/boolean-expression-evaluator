grammar BooleanExpressionV2;

expr:
	expr AND term	# AndExpr
	| expr OR term	# OrExpr
	| term			# TermExpr;

term:
	NOT term		# NotTerm
	| comparison	# ComparisonTerm
	| TRUE			# TrueTerm
	| FALSE			# FalseTerm
	| ID			# VariableTerm
	| '(' expr ')'	# ParenExpr;

comparison:
	factor EQ factor	# EqualExpr
	| factor NEQ factor	# NotEqualExpr
	| factor LT factor	# LessThanExpr
	| factor GT factor	# GreaterThanExpr
	| factor LE factor	# LessEqualExpr
	| factor GE factor	# GreaterEqualExpr;

factor: ID # VariableFactor | NUMBER # NumberFactor;

AND: 'AND';
OR: 'OR';
NOT: 'NOT';
EQ: '==';
NEQ: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';
TRUE: 'True';
FALSE: 'False';
ID: [a-zA-Z_][a-zA-Z0-9_]*; // Variable names
NUMBER: [0-9]+ ('.' [0-9]+)?; // Integers and floats
WS: [ \t\r\n]+ -> skip; // Skip whitespace