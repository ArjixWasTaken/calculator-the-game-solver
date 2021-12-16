from typing import List, NamedTuple
from enum import Enum, auto
from itertools import product


class Operator(Enum):
    addition = auto()
    subtraction = auto()
    division = auto()
    multiplication = auto()
    pop = auto()


class Token(NamedTuple):
    value: str
    operation: Operator

    def __repr__(self):
        symbol = "*" if self.operation == Operator.multiplication else ("-" if self.operation == Operator.subtraction else (
            "+" if self.operation == Operator.addition else "/" if self.operation == Operator.division else "<<"))
        return f"{symbol}{self.value if self.value != None else ''}"


def solve(goal: int, moves: int, start: int, tokens: List[Token]) -> List[List[Token]]:
    possibilities = []
    for args in product(tokens, repeat=moves):
        possibilities.append(args)

    winning_patterns = []

    for possibility in possibilities:
        begin = start
        used = []
        solved = False
        if possibility[0].operation in (Operator.multiplication, Operator.division) and begin == 0:
            continue

        for token in possibility:
            if begin == goal:
                solved = True
                break
            if token.operation == Operator.addition:
                begin += token.value
                used.append(token)
            elif token.operation == Operator.division:
                used.append(token)
                begin /= token.value
            elif token.operation == Operator.multiplication:
                used.append(token)
                begin *= token.value
            elif token.operation == Operator.subtraction:
                used.append(token)
                begin -= token.value
            elif token.operation == Operator.pop:
                used.append(token)
                new_begin = str(begin)[:-1]
                if new_begin.isdigit():
                    begin = int(new_begin)
                else:
                    begin = 0

            if begin == goal:
                solved = True
                break

        if solved:
            winning_patterns.append(used)

    return winning_patterns


level_one = solve(2, 2, 0, [Token(1, Operator.addition)])
level_two = solve(8, 3, 0, [
    Token(2, Operator.addition),
    Token(3, Operator.addition)]
)
level_three = solve(12, 3, 0, [
    Token(2, Operator.addition),
    Token(1, Operator.addition),
    Token(4, Operator.multiplication)]
)
level_four = solve(7, 3, 1, [
    Token(4, Operator.addition),
    Token(2, Operator.subtraction)]
)
level_five = solve(20, 3, 0, [
    Token(4, Operator.multiplication),
    Token(4, Operator.addition)
])
level_six = solve(40, 4, 0, [
    Token(2, Operator.addition),
    Token(4, Operator.multiplication)
])
level_seven = solve(10, 4, 100, [
    Token(3, Operator.addition),
    Token(5, Operator.division)
])
level_eight = solve(4, 3, 4321, [Token(None, Operator.pop)])

level_nine = solve(4, 3, 0, [
    Token(None, Operator.pop),
    Token(8, Operator.addition),
    Token(5, Operator.multiplication)
])
level_ten = solve(9, 4, 50, [
    Token(None, Operator.pop),
    Token(5, Operator.division),
    Token(3, Operator.multiplication)
])
level_eleven = solve(100, 3, 99, [
    Token(None, Operator.pop),
    Token(8, Operator.subtraction),
    Token(11, Operator.multiplication)
])
level_twelve = solve(404, 5, 0, [
    Token(8, Operator.addition),
    Token(10, Operator.multiplication),
    Token(2, Operator.division)
])
level_thirteen = solve(23, 4, 171, [
    Token(None, Operator.pop),
    Token(2, Operator.multiplication),
    Token(9, Operator.subtraction)
])
level_fourteen = solve(21, 5, 0, [
    Token(None, Operator.pop),
    Token(5, Operator.addition),
    Token(3, Operator.multiplication),
    Token(5, Operator.multiplication)
])
