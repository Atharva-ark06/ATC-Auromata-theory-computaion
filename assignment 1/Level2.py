# ATC Assignment 1 - Level 2: Lexical Analyzer for MiniATC
# Course: Automata Theory and Computation (UE24CS2405)

# Token Types:
#   KEYWORD    - begin, end, int, print
#   IDENTIFIER - starts with letter, followed by letters/digits
#   NUMBER     - non-negative integers
#   OPERATOR   - + - * / =
#   DELIMITER  - ; ( )
#   UNKNOWN    - any unrecognized character

MAX_TOKEN_LEN = 256

# Token type constants
TOKEN_KEYWORD = "KEYWORD"
TOKEN_IDENTIFIER = "IDENTIFIER"
TOKEN_NUMBER = "NUMBER"
TOKEN_OPERATOR = "OPERATOR"
TOKEN_DELIMITER = "DELIMITER"
TOKEN_UNKNOWN = "UNKNOWN"
TOKEN_EOF = "EOF"

# Keywords table
keywords = ["begin", "end", "int", "print"]


# Token class
class Token:
    def __init__(self, token_type, value, line):
        self.type = token_type
        self.value = value
        self.line = line


# Lexer class
class Lexer:
    def __init__(self, source):
        self.src = source
        self.pos = 0
        self.line = 1

    # Peek current character
    def peek(self):
        if self.pos >= len(self.src):
            return '\0'
        return self.src[self.pos]

    # Move to next character
    def advance(self):
        ch = self.peek()
        self.pos += 1

        if ch == '\n':
            self.line += 1

        return ch

    # Skip spaces/newlines/tabs
    def skip_whitespace(self):
        while self.peek().isspace():
            self.advance()

    # Get next token
    def next_token(self):
        self.skip_whitespace()

        ch = self.peek()

        # EOF
        if ch == '\0':
            return Token(TOKEN_EOF, "EOF", self.line)

        # Identifier or Keyword
        if ch.isalpha() or ch == '_':
            value = ""

            while self.peek().isalnum() or self.peek() == '_':
                value += self.advance()

            if value in keywords:
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

        # Unknown character
        value = self.advance()
        return Token(TOKEN_UNKNOWN, value, self.line)


# Run lexer
def run_lexer(source):
    lexer = Lexer(source)

    print("\n{:<5} {:<14} {}".format("Line", "Type", "Value"))
    print("{:<5} {:<14} {}".format("----", "-------------", "-----"))

    count = {
        TOKEN_KEYWORD: 0,
        TOKEN_IDENTIFIER: 0,
        TOKEN_NUMBER: 0,
        TOKEN_OPERATOR: 0,
        TOKEN_DELIMITER: 0,
        TOKEN_UNKNOWN: 0
    }

    while True:
        tok = lexer.next_token()

        if tok.type == TOKEN_EOF:
            break

        print("{:<5} {:<14} {}".format(tok.line, tok.type, tok.value))

        if tok.type in count:
            count[tok.type] += 1

    # Summary
    print("\n--- Token Summary ---")
    print("Keywords:    ", count[TOKEN_KEYWORD])
    print("Identifiers: ", count[TOKEN_IDENTIFIER])
    print("Numbers:     ", count[TOKEN_NUMBER])
    print("Operators:   ", count[TOKEN_OPERATOR])
    print("Delimiters:  ", count[TOKEN_DELIMITER])

    if count[TOKEN_UNKNOWN] > 0:
        print("Unknown:     ", count[TOKEN_UNKNOWN], "<-- check your source")


# Main function
def main():
    print("==============================================")
    print("  ATC Assignment 1 (level-2)- MiniATC Lexical Analyzer")
    print("==============================================")

    # Built-in demo program
    demo = """begin
  int x;
  x = 10;
  int y;
  y = x + 5;
  print(x);
  print(y);
end
"""

    print("\nAnalyzing MiniATC Program:")
    print("----------------------------")
    print(demo)

    run_lexer(demo)

    # Interactive mode
    print("\n--- Interactive Mode ---")
    print("Enter a MiniATC program (end with a line containing only '###'):")

    lines = []

    while True:
        line = input()

        if line == "###":
            break

        lines.append(line)

    user_program = "\n".join(lines)

    if len(user_program) > 0:
        print("\nToken Table for your input:")
        run_lexer(user_program)


# Program execution starts here
if __name__ == "__main__":
    main()