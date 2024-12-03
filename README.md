# boolean-expression-evaluator

A Python-based tool to parse and evaluate Boolean expressions.

## Getting started

- Prerequisite: python3, pip
- Setup virtual env: `py -m venv <venv_name>`
- Activate virtual env (powershell): `.\<venv_name>\Scripts\activate`
- Install required library: `pip install -r requirements.txt`
- Run file: `py ./<target-file>.py`
  - e.g.
    ```powershell
    PS D:\code\y4s1\wif3010\boolean-expression-evaluator> py .\boolean_expression.py
    > bool a = True
    > line 1:13 missing ';' at '<EOF>'
    > (program (statement (declaration bool a = (expression True) <missing ';'>)))
    > PS D:\code\y4s1\wif3010\boolean-expression-evaluator> py .\boolean_expression.py
    > bool a = true;
    > (program (statement (declaration bool a = (expression true) ;)))
    ```

## References

- [ANTLR Tool](https://www.antlr.org/download/antlr-4.13.2-complete.jar)
- [ANTLR with Python](https://yetanotherprogrammingblog.medium.com/antlr-with-python-974c756bdb1b)

## Features

- **Lexer**: Tokenizes input expressions.
- **Parser**: Builds an Abstract Syntax Tree (AST) from tokens.
- **Evaluator**: Recursively evaluates the AST based on variable values.
- **Modular Design**: Easily extendable and maintainable.

---

## Project Structure

BooleanEvaluator/
├── lexer/
├── parser/
├── evaluator/
├── tests/
├── utils/
├── main.py
├── requirements.txt
└── README.md

---

## Project Structure Details

1. **lexer/**  
   **Purpose:** Handles the tokenization of input expressions.

   - `_init_.py`: Makes the lexer folder a Python package.
   - `lexer.py`: Contains the main Lexer class responsible for breaking down the input string into tokens.
   - `tokenizer.py` (Optional): Contains helper functions or classes for tokenizing specific parts of the expression.

2. **parser/**  
   **Purpose:** Parses tokens into an Abstract Syntax Tree (AST).

   - `_init_.py`: Makes the parser folder a Python package.
   - `parser.py`: Contains the Parser class that builds the AST from tokens.
   - `ast.py`: Defines AST node structures and related utilities.

3. **evaluator/**  
   **Purpose:** Evaluates the AST based on variable values.

   - `_init_.py`: Makes the evaluator folder a Python package.
   - `evaluator.py`: Contains the Evaluator class that recursively evaluates the AST.

4. **tests/**  
   **Purpose:** Contains unit tests for each module to ensure correctness.

   - `_init_.py`: Makes the tests folder a Python package.
   - `test_lexer.py`: Tests for the Lexer component.
   - `test_parser.py`: Tests for the Parser component.
   - `test_evaluator.py`: Tests for the Evaluator component.

5. **utils/**  
   **Purpose:** Contains utility functions or helper modules that are used across different components.

   - `_init_.py`: Makes the utils folder a Python package.
   - `helpers.py`: Example utility functions (e.g., logging, configuration parsing).

6. **main.py**  
   **Purpose:** The entry point of the application that ties all components together.

7. **requirements.txt**  
   **Purpose:** Lists all Python dependencies required for the project. This facilitates easy setup using pip.
   - Note: Since the project primarily uses Python’s standard library, requirements.txt may be minimal or even empty. However, if you add external libraries in the future (e.g. for advanced parsing), list them here.
