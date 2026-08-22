

STATE_START = 0
STATE_VALID = 1
STATE_DEAD = 2


# Returns next DFA state given current state and input character
def dfa_transition(state, ch):
    if state == STATE_START:
        if ch.isalpha() or ch == '_':
            return STATE_VALID
        else:
            return STATE_DEAD

    elif state == STATE_VALID:
        if ch.isalnum() or ch == '_':
            return STATE_VALID
        else:
            return STATE_DEAD

    return STATE_DEAD


# Returns True if the string is a valid identifier
def is_valid_identifier(string):
    if len(string) == 0:
        return False

    state = STATE_START

    for ch in string:
        state = dfa_transition(state, ch)

        if state == STATE_DEAD:
            return False

    return state == STATE_VALID


def main():
    print("==============================================")
    print("  ATC Assignment 1 (level-1) - Identifier Recognition")
    print("==============================================")
    print("Enter identifiers to check (type 'exit' to quit)\n")

    while True:
        user_input = input("Enter string: ")

        if user_input == "exit":
            break

        if is_valid_identifier(user_input):
            print(f'Result: "{user_input}" is a VALID identifier.\n')
        else:
            print(f'Result: "{user_input}" is an INVALID identifier.\n')

    # Automated test cases
    print("\n--- Running Built-in Test Cases ---")

    tests = [
        "x", "total1", "sum2", "_var", "abc123",
        "1x", "ab-c", "a$b", "", "123"
    ]

    for test in tests:
        if len(test) == 0:
            print('"" -> INVALID (empty string)')
            continue

        result = "VALID" if is_valid_identifier(test) else "INVALID"
        print(f'"{test}" -> {result}')


if __name__ == "__main__":
    main()