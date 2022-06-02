from lib2to3.pgen2.token import OP
from typing import List, MutableMapping, NamedTuple, Tuple, Union
from enum import Enum, auto
from itertools import product
from webbrowser import Opera


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
        #print(self.operation)
        if self.operation == Operator.convert:
            return "{} => {}".format(*self.value)
        else:
            symbol = "*" if self.operation == Operator.multiplication else ("-" if self.operation == Operator.subtraction else (
                "+" if self.operation == Operator.addition else "/" if self.operation == Operator.division else "<<" if self.operation == Operator.pop else "^" if self.operation == Operator.exponential else "+/-" if self.operation == Operator.switch else "rev" if self.operation == Operator.reverse else ""))
            
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
    for seq, item in enumerate(winning_patterns):
        if winning_patterns.count(item) > 1:
            winning_patterns.pop(seq)
    return winning_patterns

levels = [
    "Level 0 doesn't exist",
    solve(2, 2, 0, [Token(1, Operator.addition)]),
    solve(8, 3, 0, [
        Token(2, Operator.addition),
        Token(3, Operator.addition)]
    ),
    solve(12, 3, 0, [
        Token(2, Operator.addition),
        Token(1, Operator.addition),
        Token(4, Operator.multiplication)]
    ),
    solve(7, 3, 1, [
        Token(4, Operator.addition),
        Token(2, Operator.subtraction)]
    ),
    solve(20, 3, 0, [
        Token(4, Operator.multiplication),
        Token(4, Operator.addition)
    ]),
    solve(40, 4, 0, [
        Token(2, Operator.addition),
        Token(4, Operator.multiplication)
    ]),
    solve(10, 4, 100, [
        Token(3, Operator.addition),
        Token(5, Operator.division)
    ]),
    solve(4, 3, 4321, [Token(None, Operator.pop)]),
    solve(4, 3, 0, [
        Token(None, Operator.pop),
        Token(8, Operator.addition),
        Token(5, Operator.multiplication)
    ]),
    solve(9, 4, 50, [
        Token(None, Operator.pop),
        Token(5, Operator.division),
        Token(3, Operator.multiplication)
    ]),
    solve(100, 3, 99, [
        Token(None, Operator.pop),
        Token(8, Operator.subtraction),
        Token(11, Operator.multiplication)
    ]),
    solve(404, 5, 0, [
        Token(8, Operator.addition),
        Token(10, Operator.multiplication),
        Token(2, Operator.division)
    ]),
    solve(23, 4, 171, [
        Token(None, Operator.pop),
        Token(2, Operator.multiplication),
        Token(9, Operator.subtraction)
    ]),
    solve(21, 5, 0, [
        Token(None, Operator.pop),
        Token(5, Operator.addition),
        Token(3, Operator.multiplication),
        Token(5, Operator.multiplication)
    ]),
    solve(50, 3, 10, [
        Token(3, Operator.multiplication),
        Token(2, Operator.multiplication),
        Token(5, Operator.subtraction)
    ]),
    solve(2, 5, 0, [
        Token(None, Operator.pop),
        Token(4, Operator.addition),
        Token(9, Operator.multiplication)
    ]),
    solve(11, 2, 0, [Token(1, Operator.insert)]),
    solve(101, 3, 0, [
        Token(1, Operator.insert),
        Token(0, Operator.insert)
    ]),
    solve(44, 3, 0, [
        Token(2, Operator.insert),
        Token(2, Operator.multiplication)
    ]),
    solve(35, 2, 0, [
        Token(3, Operator.addition),
        Token(5, Operator.insert)
    ]),
    solve(56, 3, 0, [
        Token(1, Operator.insert),
        Token(5, Operator.addition)
    ]),
    solve(9, 4, 0, [
        Token(2, Operator.addition),
        Token(3, Operator.division),
        Token(1, Operator.insert)
    ]),
    solve(10, 4, 15, [
        Token(0, Operator.insert),
        Token(2, Operator.addition),
        Token(5, Operator.division)
    ]),
    solve(210, 5, 0, [
        Token(5, Operator.addition),
        Token(5, Operator.subtraction),
        Token(5, Operator.insert),
        Token(2, Operator.insert),
    ]),
    solve(2020, 4, 40, [
        Token(0, Operator.insert),
        Token(4, Operator.addition),
        Token(2, Operator.division),
    ]),
    solve(11, 4, 0, [
        Token(12, Operator.insert),
        Token(None, Operator.pop)
    ]),
    solve(102, 4, 0, [
        Token(10, Operator.insert),
        Token(1, Operator.addition),
        Token(None, Operator.pop)
    ]),
    solve(222, 4, 0, [
        Token(1, Operator.insert),
        Token((1, 2), Operator.convert)
    ]),
    solve(93, 4, 0, [
        Token(6, Operator.addition),
        Token(7, Operator.multiplication),
        Token((6, 9), Operator.convert)
    ]),
    solve(2321, 6, 0, [
        Token(1, Operator.insert),
        Token(2, Operator.insert),
        Token((1, 2), Operator.convert),
        Token((2, 3), Operator.convert),
    ]),
    solve(24, 5, 0, [
        Token(9, Operator.addition),
        Token(2, Operator.multiplication),
        Token((8, 4), Operator.convert)
    ]),
    solve(29, 5, 11, [
        Token(2, Operator.division),
        Token(3, Operator.addition),
        Token((1, 2), Operator.convert),
        Token((2, 9), Operator.convert),
    ]),
    solve(20, 5, 36, [
        Token(3, Operator.addition),
        Token(3, Operator.division),
        Token((1, 2), Operator.convert)
    ]),
    solve(15, 4, 2, [
        Token(3, Operator.division),
        Token(1, Operator.insert),
        Token(2, Operator.multiplication),
        Token((4, 5), Operator.convert)
    ]),
    solve(414, 4, 1234, [
        Token((23, 41), Operator.convert),
        Token((24, 14), Operator.convert),
        Token((12, 24), Operator.convert),
        Token((14, 2), Operator.convert)
    ]),
    solve(-85, 4, 0, [
        Token(7, Operator.subtraction),
        Token(6, Operator.addition),
        Token(5, Operator.insert)
    ]),
    solve(9, 3, 0, [
        Token(1, Operator.subtraction),
        Token(2, Operator.subtraction),
        Token(2, Operator.exponential)
    ]),
    solve(-120, 4, 0, [
        Token(5, Operator.multiplication),
        Token(6, Operator.subtraction),
        Token(4, Operator.insert)
    ]),
    solve(144, 3, 0, [
        Token(1, Operator.subtraction),
        Token(2, Operator.insert),
        Token(2, Operator.exponential)
    ]),
    solve(5, 1, -5, [
        Token(None, Operator.switch)
    ]),
    solve(-6, 3, 0, [
        Token(4, Operator.addition),
        Token(2, Operator.addition),
        Token(None, Operator.switch)
    ]),
    solve(-13, 4, 0, [
        Token(3, Operator.addition),
        Token(7, Operator.subtraction),
        Token(None, Operator.switch)
    ]),
    solve(60, 4, 0, [
        Token(5, Operator.addition),
        Token(10, Operator.subtraction),
        Token(4, Operator.multiplication),
        Token(None, Operator.switch)
    ]),
    solve(52, 5, 44, [
        Token(9, Operator.addition),
        Token(2, Operator.division),
        Token(4, Operator.multiplication),
        Token(None, Operator.switch)
    ]),
    solve(10, 5, 9, [
        Token(5, Operator.addition),
        Token(5, Operator.multiplication),
        Token(None, Operator.switch)
    ]),
    solve(12, 5, 14, [
        Token(6, Operator.insert),
        Token(5, Operator.addition),
        Token(8, Operator.division),
        Token(None, Operator.switch)
    ]),
    solve(13, 4, 55, [
        Token(9, Operator.addition),
        Token(None, Operator.switch),
        Token(None, Operator.pop)
    ]),
    solve(245, 5, 0, [
        Token(3, Operator.subtraction),
        Token(5, Operator.insert),
        Token(4, Operator.multiplication),
        Token(None, Operator.switch)
    ]),
    solve(12, 4, 39, [
        Token(-3, Operator.multiplication),
        Token(3, Operator.division),
        Token(9, Operator.addition),
        Token(None, Operator.switch)
    ]),
    solve(126, 6, 111, [
        Token(3, Operator.multiplication),
        Token(9, Operator.subtraction),
        Token(None, Operator.switch),
        Token(None, Operator.pop)
    ]),
    solve(3, 5, 34, [
        Token(5, Operator.subtraction),
        Token(8, Operator.addition),
        Token(7, Operator.division),
        Token(None, Operator.switch)
    ]),
    solve(4, 5, 25, [
        Token(4, Operator.subtraction),
        Token(-4, Operator.multiplication),
        Token(3, Operator.division),
        Token(8, Operator.division),
        Token(None, Operator.switch)
    ]),
    solve(21, 1, 12, [
        Token(None, Operator.reverse)
    ]),
    solve(51, 3, 0, [
        Token(6, Operator.addition),
        Token(9, Operator.addition),
        Token(None, Operator.reverse)
    ]),
    solve(101, 3, 100, [
        Token(1, Operator.insert),
        Token(9, Operator.addition),
        Token(None, Operator.reverse),
    ]),
    solve(100, 4, 1101, [
        Token(None, Operator.reverse),
        Token(1, Operator.subtraction)
    ]),
    solve(58, 4, 0, [
        Token(4, Operator.addition),
        Token(4, Operator.multiplication),
        Token(3, Operator.subtraction),
        Token(None, Operator.reverse)
    ]),
    solve(4, 3, 6, [
        Token(1, Operator.insert),
        Token(4, Operator.division),
        Token(None, Operator.reverse)
    ]),
    solve(21, 3, 15, [
        Token(9, Operator.addition),
        Token(5, Operator.multiplication),
        Token(None, Operator.reverse)
    ]),
    solve(13, 5, 100, [
        Token(2, Operator.division),
        Token(None, Operator.reverse)
    ]), 
    solve(11011, 4, 10, [
        Token(None, Operator.reverse),
        Token(1, Operator.insert)
    ]),
    solve(102, 4, 0, [
        Token(5, Operator.addition),
        Token(None, Operator.reverse),
        Token(10, Operator.insert),
        Token(4, Operator.multiplication)
    ])
]

print(levels[-1])
