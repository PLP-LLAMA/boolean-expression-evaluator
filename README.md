# boolean-expression-evaluator

A Python-based tool to parse and evaluate Boolean expressions.

## Getting Started

- Prerequisite: python3, pip
- Setup virtual env: `py -m venv <venv_name>`
- Activate virtual env (powershell): `.\<venv_name>\Scripts\activate`
- Install required library: `pip install -r requirements.txt`
- Run file: `py ./<target-file>.py`
  - e.g.
    ```powershell
    PS D:\code\y4s1\wif3010\boolean-expression-evaluator> py .\boolean_expression.py
    > bool a = True         # type the input
    line 1:13 missing ';' at '<EOF>'
    (program (statement (declaration bool a = (expression True) <missing ';'>)))
    PS D:\code\y4s1\wif3010\boolean-expression-evaluator> py .\boolean_expression.py
    > bool a = true;
    (program (statement (declaration bool a = (expression true) ;)))
    ```

## Generate Lexer / Parser From Grammar

- Prerequisite: java, check using `java --version`
- Generate using antlr tool `java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 <path of.g4 file>`
- e.g: `java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 .\grammar\hello\Hello.g4` generate `HelloLexer.py`, `HelloParser.py` & `HelloParser.py`

## References

- [ANTLR Tool](https://www.antlr.org/download/antlr-4.13.2-complete.jar)
- [ANTLR with Python](https://yetanotherprogrammingblog.medium.com/antlr-with-python-974c756bdb1b)
- [Using Antlr Parse Calculate Expression - Java](https://weareadaptive.com/2018/11/21/using-antlr-parse-calculate-expressions-part/)

## Features

- **Lexer**: Tokenizes input expressions.
- **Parser**: Builds an Abstract Syntax Tree (AST) from tokens.
- **Evaluator**: Recursively evaluates the AST based on variable values.
- **Modular Design**: Easily extendable and maintainable.


## Project Structure
```powershell
boolean-expression-evaluator/
├── grammar/                # ANTLR grammar files
│   ├── boolean_expression/ # Specific grammar for the boolen expression        
│   └── error_handlers/     # Error Handlers for the system 
├── tests/                  # Unit tests for the Lexer, Parser, Evaluator
├── utils/                  # Utility modules for common tasks
├── main.py                 # Entry point of the application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Project Structure Details

1. **grammar/**

- Stores the ANTLR grammar files (.g4 files) for defining the structure of Boolean expressions.
- Divided into subfolders like boolean_expression, and error_handlers.

2. **tests/**

- Contains unit tests for testing the Lexer, Parser, and Evaluator components.
- Includes tests like test_lexer.py, test_parser.py, and test_evaluator.py.

3. **utils/**

- Contains helper functions and utilities used across the project.

4. **main.py**

- The main file that brings all components together and provides the entry point to the program.
