# =========================================================
# ATC Assignment 1 - MiniATC Lexer + Recursive Descent Parser
# Course: Automata Theory and Computation (UE24CS2405)
# =========================================================

# ---------------- TOKEN TYPES ----------------

TOKEN_KEYWORD = "KEYWORD"
TOKEN_IDENTIFIER = "IDENTIFIER"
TOKEN_NUMBER = "NUMBER"
TOKEN_OPERATOR = "OPERATOR"
TOKEN_DELIMITER = "DELIMITER"
TOKEN_UNKNOWN = "UNKNOWN"
TOKEN_EOF = "EOF"

# Keywords
KEYWORDS = ["begin", "end", "int", "print"]


# =========================================================
# TOKEN CLASS
# =========================================================

class Token:
    def __init__(self, token_type, value, line):
        self.type = token_type
        self.value = value
        self.line = line


# =========================================================
# LEXER
# =========================================================

class Lexer:
    def __init__(self, source):
        self.src = source
        self.pos = 0
        self.line = 1

    def peek(self):
        if self.pos >= len(self.src):
            return '\0'
        return self.src[self.pos]

    def advance(self):
        ch = self.peek()
        self.pos += 1

        if ch == '\n':
            self.line += 1

        return ch

    def skip_whitespace(self):
        while self.peek().isspace():
            self.advance()

    def next_token(self):

        self.skip_whitespace()

        ch = self.peek()

        # EOF
        if ch == '\0':
            return Token(TOKEN_EOF, "EOF", self.line)

        # Identifier / Keyword
        if ch.isalpha() or ch == '_':
            value = ""

            while self.peek().isalnum() or self.peek() == '_':
                value += self.advance()

            if value in KEYWORDS:
                return Token(TOKEN_KEYWORD, value, self.line)
            else:
                return Token(TOKEN_IDENTIFIER, value, self.line)

        # Number
        if ch.isdigit():
            value = ""

            while self.peek().isdigit():
                value += self.advance()

            return Token(TOKEN_NUMBER, value, self.line)

        # Operator
        if ch in ['+', '-', '*', '/', '=']:
            value = self.advance()
            return Token(TOKEN_OPERATOR, value, self.line)

        # Delimiter
        if ch in [';', '(', ')']:
            value = self.advance()
            return Token(TOKEN_DELIMITER, value, self.line)

        # Unknown
        value = self.advance()
        return Token(TOKEN_UNKNOWN, value, self.line)


# =========================================================
# PARSER
# =========================================================

class Parser:

    def __init__(self, source):
        self.lexer = Lexer(source)
        self.current = self.lexer.next_token()
        self.errors = 0

    def parser_advance(self):
        self.current = self.lexer.next_token()

    # Match exact value
    def match_val(self, expected):

        if self.current.value == expected:
            print(f"  Matched '{expected}'")
            self.parser_advance()

        else:
            print(f"  [ERROR] Line {self.current.line}: "
                  f"Expected '{expected}', found '{self.current.value}'")

            self.errors += 1
            self.parser_advance()

    # Match token type
    def match_type(self, token_type, name):

        if self.current.type == token_type:
            print(f"  Matched {name}: {self.current.value}")
            self.parser_advance()

        else:
            print(f"  [ERROR] Line {self.current.line}: "
                  f"Expected {name}, found '{self.current.value}'")

            self.errors += 1
            self.parser_advance()

    # =====================================================
    # Grammar Functions
    # =====================================================

    # Program -> begin StmtList end
    def parse_program(self):

        print("[Parsing: Program]")

        self.match_val("begin")

        self.parse_stmt_list()

        self.match_val("end")

    # StmtList -> Stmt StmtList | epsilon
    def parse_stmt_list(self):

        print("[Parsing: StmtList]")

        while self.current.value not in ["end", "EOF"]:
            self.parse_stmt()

    # Stmt
    def parse_stmt(self):

        print("[Parsing: Stmt]")

        # int id ;
        if self.current.value == "int":

            print("  [DeclStmt]")

            self.match_val("int")
            self.match_type(TOKEN_IDENTIFIER, "identifier")
            self.match_val(";")

        # print ( id ) ;
        elif self.current.value == "print":

            print("  [PrintStmt]")

            self.match_val("print")
            self.match_val("(")
            self.match_type(TOKEN_IDENTIFIER, "identifier")
            self.match_val(")")
            self.match_val(";")

        # id = Expr ;
        elif self.current.type == TOKEN_IDENTIFIER:

            print("  [AssignStmt]")

            self.match_type(TOKEN_IDENTIFIER, "identifier")
            self.match_val("=")

            self.parse_expr()

            self.match_val(";")

        else:
            print(f"  [ERROR] Line {self.current.line}: "
                  f"Unexpected token '{self.current.value}'")

            self.errors += 1
            self.parser_advance()

    # Expr -> Term ExprTail
    def parse_expr(self):

        print("[Parsing: Expr]")

        self.parse_term()
        self.parse_expr_tail()

    # ExprTail -> + Term ExprTail | - Term ExprTail | epsilon
    def parse_expr_tail(self):

        if self.current.value in ["+", "-"]:

            print(f"[Parsing: ExprTail with '{self.current.value}']")

            self.parser_advance()

            self.parse_term()

            self.parse_expr_tail()

    # Term -> Factor TermTail
    def parse_term(self):

        print("[Parsing: Term]")

        self.parse_factor()
        self.parse_term_tail()

    # TermTail -> * Factor TermTail | / Factor TermTail | epsilon
    def parse_term_tail(self):

        if self.current.value in ["*", "/"]:

            print(f"[Parsing: TermTail with '{self.current.value}']")

            self.parser_advance()

            self.parse_factor()

            self.parse_term_tail()

    # Factor -> id | number | ( Expr )
    def parse_factor(self):

        print("[Parsing: Factor]")

        if self.current.type == TOKEN_IDENTIFIER:

            self.match_type(TOKEN_IDENTIFIER, "identifier")

        elif self.current.type == TOKEN_NUMBER:

            self.match_type(TOKEN_NUMBER, "number")

        elif self.current.value == "(":

            self.match_val("(")

            self.parse_expr()

            self.match_val(")")

        else:
            print(f"  [ERROR] Line {self.current.line}: "
                  f"Invalid factor '{self.current.value}'")

            self.errors += 1
            self.parser_advance()


# =========================================================
# RUN PARSER
# =========================================================

def run_parser(source):

    print("\nSource Program:")
    print("----------------------------")
    print(source)
    print("----------------------------")

    parser = Parser(source)

    parser.parse_program()

    print("\n============ Parse Result ============")

    if parser.errors == 0:
        print("  SUCCESS: Program is syntactically CORRECT.")

    else:
        print(f"  FAILED: {parser.errors} syntax error(s) found.")

    print("======================================\n")


# =========================================================
# MAIN
# =========================================================

def main():

    print("==============================================")
    print(" ATC Assignment 1 (Level-3) - MiniATC Lexer + Parser")
    print("==============================================")

    # Test 1: Valid program
    run_parser(
        """begin
  int x;
  x = 10;
  int y;
  y = x + 5;
  print(x);
  print(y);
end"""
    )

    # Test 2: Invalid program
    run_parser(
        """begin
  int x
  x = 10;
end"""
    )

    # Interactive Mode
    print("--- Interactive Parser Mode ---")
    print("Enter MiniATC program (end line with '###'):")

    lines = []

    while True:

        line = input()

        if line == "###":
            break

        lines.append(line)

    user_program = "\n".join(lines)

    if len(user_program) > 0:
        run_parser(user_program)


# Program starts here
if __name__ == "__main__":
    main()