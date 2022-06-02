from typing import List, NamedTuple, Tuple, Union
from enum import Enum, auto
from itertools import product


class Operator(Enum):
    addition = auto()
    subtraction = auto()
    division = auto()
    multiplication = auto()
    pop = auto()
    insert = auto()
    convert = auto()
    exponential = auto()
    switch = auto()
    reverse = auto()


class Token(NamedTuple):
    value: Union[int, Tuple[int, int]]
    operation: Operator

    def __repr__(self):
        if self.operation == Operator.convert:
            return "{} => {}".format(*self.value)
        else:
            symbol = "*" if self.operation == Operator.multiplication else ("-" if self.operation == Operator.subtraction else (
                "+" if self.operation == Operator.addition else "/" if self.operation == Operator.division else "<<" if self.operation == Operator.pop else "^" if self.operation == Operator.exponential else "+/-" if self.operation == Operator.switch else "rev" if self.operation == Operator.reverse else ""))

            return f"{symbol}{self.value if self.value != None else ''}"


def solve(goal: int, moves: int, start: int, tokens: List[Token]) -> List[List[Token]]:
    possibilities = product(tokens, repeat=moves)

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
                if token.value > begin:
                    break
                if (begin/token.value).is_integer():
                    begin = int(begin / token.value)
                else:
                    break
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
            elif token.operation == Operator.insert:
                used.append(token)
                begin = int(f"{begin if begin != 0 else ''}{token.value}")
            elif token.operation == Operator.convert:
                used.append(token)
                begin = int(str(begin).replace(
                    str(token.value[0]), str(token.value[1]))
                )
            elif token.operation == Operator.exponential:
                used.append(token)
                begin **= token.value
            elif token.operation == Operator.switch:
                used.append(token)
                begin = -begin
            elif token.operation == Operator.reverse:
                used.append(token)
                try:
                    begin = int(str(begin)[::-1])
                except ValueError as err:
                    break
            if begin == goal:
                solved = True
                break

        if solved:
            winning_patterns.append(used)

    return winning_patterns
