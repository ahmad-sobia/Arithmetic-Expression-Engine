import math

class ExpressionEngine:
    def __init__(self):
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def is_operator(self, ch):
        return ch in self.precedence

    def is_operand(self, ch):
        return ch.isalnum()

    # INFIX → POSTFIX #

    def infix_to_postfix(self, expr):
        stack = []
        postfix = []

        print("\nStep-by-step Infix → Postfix:")
        print("Symbol\tStack\t\tPostfix")

        for ch in expr:
            if ch == ' ':
                continue

            if self.is_operand(ch):
                postfix.append(ch)
            elif ch == '(':
                stack.append(ch)
            elif ch == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1] != '(' and
                       self.precedence.get(stack[-1], 0) >= self.precedence[ch]):
                    postfix.append(stack.pop())
                stack.append(ch)

            print("{ch}\t{stack}\t\t{postfix}")

        while stack:
            postfix.append(stack.pop())

        return postfix

    #  INFIX → PREFIX  #

    def infix_to_prefix(self, expr):
        expr = expr[::-1]
        expr = expr.replace('(', '#').replace(')', '(').replace('#', ')')

        postfix = self.infix_to_postfix(expr)
        prefix = postfix[::-1]
        return prefix

    #  POSTFIX → INFIX  #

    def postfix_to_infix(self, expr):
        stack = []

        print("\nStep-by-step Postfix → Infix:")
        print("Symbol\tStack")

        for ch in expr:
            if ch == ' ':
                continue

            if self.is_operand(ch):
                stack.append(ch)
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(f"({a}{ch}{b})")

            print("{ch}\t{stack}")

        return stack[0]

    #  PREFIX → INFIX  #

    def prefix_to_infix(self, expr):
        stack = []

        print("\nStep-by-step Prefix → Infix:")
        print("Symbol\tStack")

        for ch in reversed(expr):
            if ch == ' ':
                continue

            if self.is_operand(ch):
                stack.append(ch)
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(f"({a}{ch}{b})")

            print("{ch}\t{stack}")

        return stack[0]

    # POSTFIX EVALUATION #

    def evaluate_postfix(self, expr):
        stack = []

        print("\nStep-by-step Postfix Evaluation:")
        print("Symbol\tStack")

        for ch in expr:
            if ch == ' ':
                continue

            if ch.isdigit():
                stack.append(int(ch))
            else:
                b = stack.pop()
                a = stack.pop()

                if ch == '+': stack.append(a + b)
                elif ch == '-': stack.append(a - b)
                elif ch == '*': stack.append(a * b)
                elif ch == '/': stack.append(a / b)
                elif ch == '^': stack.append(a ** b)

            print("{ch}\t{stack}")

        return stack[0]


#  MAIN MENU  #

engine = ExpressionEngine()

while True:
    print("\n=== Python Expression Engine ===")
    print("1. Infix to Postfix")
    print("2. Infix to Prefix")
    print("3. Postfix to Infix")
    print("4. Prefix to Infix")
    print("5. Evaluate Postfix Expression")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting...")
        break

    expr = input("Enter your expression: ")

    try:
        if choice == '1':
            result = engine.infix_to_postfix(expr)
            print("\nFinal Postfix:", " ".join(result))

        elif choice == '2':
            result = engine.infix_to_prefix(expr)
            print("\nFinal Prefix:", " ".join(result))

        elif choice == '3':
            result = engine.postfix_to_infix(expr)
            print("\nFinal Infix:", result)

        elif choice == '4':
            result = engine.prefix_to_infix(expr)
            print("\nFinal Infix:", result)

        elif choice == '5':
            result = engine.evaluate_postfix(expr)
            print("\nFinal Result:", result)

        else:
            print("Invalid choice!")

    except Exception as e:
        print("Error:", e)


