
# Christine Qiao
# Tic-Tac-Toe AI
# Minimax Algorithm

def successors(state, turn):
    sli = [i for i in range(len(state)) if state[i] == '.']
    return [(state, state[:i] + turn + state[i + 1:]) for i in sli]


def terminal_test(state, tc):
    if '.' not in state:
        return True

    for li in tc:
        check_li = [state[x] for x in li]
        if len(set(check_li)) == 1 and check_li[0] != '.':
            return True

    return False


def utility(turn, tc, state):
    # Return 1 if turn wins, -1 if turn loses, 0 if tie
    for li in tc:
        check_li = [state[x] for x in li]

        if len(set(check_li)) == 1 and check_li[0] != '.':
            return 1 if check_li[0] == turn else -1

    return 0


def minimax(state, turn, tc):
    if turn == 'X':
        return max_value(state, turn, tc)[1]
    else:
        return min_value(state, turn, tc)[1]


def max_value(state, turn, tc):
    # X is the maximizing player
    if terminal_test(state, tc):
        return utility('X', tc, state), state

    v = float('-inf')
    best_state = None

    for _, new_state in successors(state, 'X'):
        min_v, _ = min_value(new_state, 'O', tc)

        if min_v > v:
            v = min_v
            best_state = new_state

    return v, best_state


def min_value(state, turn, tc):
    # O is the minimizing player
    if terminal_test(state, tc):
        return utility('X', tc, state), state

    v = float('inf')
    best_state = None

    for _, new_state in successors(state, 'O'):
        max_v, _ = max_value(new_state, 'X', tc)

        if max_v < v:
            v = max_v
            best_state = new_state

    return v, best_state


def get_turn(state):
    x_count = state.count('X')
    o_count = state.count('O')

    return 'X' if x_count == o_count else 'O'


def conditions_table(n=3, n2=9):
    ret = [[] for i in range(n * 2 + 2)]

    for i in range(n2):
        ret[i // n].append(i)
        ret[n + i % n].append(i)

        if i // n == i % n:
            ret[n + n].append(i)

        if i // n == n - i % n - 1:
            ret[n + n + 1].append(i)

    return ret


def display(state, n=3, n2=9):
    result = ""

    for i in range(n2):
        result += state[i] + ' '

        if i % n == n - 1:
            result += '\n'

    return result


def human_play(state, n, turn):
    available = [i for i in range(len(state)) if state[i] == '.']

    print("Available positions:")
    for i in available:
        print(f"[{i}] ({i // n}, {i % n})")

    while True:
        try:
            index = int(input("Enter your move (0-8): "))

            if index not in available:
                print("Invalid move. Choose an available position.")
                continue

            return state[:index] + turn + state[index + 1:]

        except ValueError:
            print("Please enter a number between 0 and 8.")


def validate_state(state, tc):
    if len(state) != 9:
        return False

    if any(c not in 'XO.' for c in state):
        return False

    x_count = state.count('X')
    o_count = state.count('O')

    if x_count != o_count and x_count != o_count + 1:
        return False

    x_wins = utility('X', tc, state) == 1
    o_wins = utility('O', tc, state) == 1

    # Detect wins separately because utility alone only reports
    # the first winning line encountered.
    winners = set()

    for line in tc:
        symbols = [state[i] for i in line]
        if len(set(symbols)) == 1 and symbols[0] != '.':
            winners.add(symbols[0])

    if len(winners) > 1:
        return False

    if 'X' in winners and x_count != o_count + 1:
        return False

    if 'O' in winners and x_count != o_count:
        return False

    return True


def main():
    tc = conditions_table(3, 9)

    while True:
        X = input("X is human or AI? (h: human, a: AI) ").lower()
        if X in ('h', 'a'):
            break
        print("Please enter 'h' or 'a'.")

    while True:
        O = input("O is human or AI? (h: human, a: AI) ").lower()
        if O in ('h', 'a'):
            break
        print("Please enter 'h' or 'a'.")

    while True:
        state = input(
            "Input state (ENTER for empty board): "
        ).upper().strip()

        if not state:
            state = '.........'

        if validate_state(state, tc):
            break

        print("Invalid board. Please enter a valid 9-character state.")

    turn = get_turn(state)

    print("\nGame start!")
    print(display(state))

    while not terminal_test(state, tc):
        print(f"{turn}'s turn:")

        if turn == 'X':
            if X == 'a':
                state = minimax(state, turn, tc)
            else:
                state = human_play(state, 3, turn)
        else:
            if O == 'a':
                state = minimax(state, turn, tc)
            else:
                state = human_play(state, 3, turn)

        print(display(state))

        turn = 'O' if turn == 'X' else 'X'

    print("Game over!")

    if utility('X', tc, state) == 1:
        print("X wins!")
    elif utility('O', tc, state) == 1:
        print("O wins!")
    else:
        print("It's a tie!")


if __name__ == '__main__':
    main()
