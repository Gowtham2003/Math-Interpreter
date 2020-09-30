from lexer import Lexer

while True:
    text = input("Calc > ")
    tokens = Lexer(text).generate_tokens()

    print(list(tokens))


