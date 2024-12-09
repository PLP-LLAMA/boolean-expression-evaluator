from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self):
        super(CustomErrorListener, self).__init__()

    def syntaxError(self, recognizer, offending_symbol, line, column, msg, e):
        offending_symbol_text = (
            offending_symbol.text if offending_symbol else "Unknown symbol"
        )
        print(
            f"Syntax Error at line {line}, column {column}:\n"
            f"  Message: {msg}\n"
            f"  Offending Symbol: {offending_symbol_text}\n"
            f"  Recognizer: {type(recognizer).__name__}\n"
            f"  Exception: {str(e) if e else 'None'}"
        )

    @staticmethod
    def handle_custom_error(message):
        print(f"Encountered: {message}")