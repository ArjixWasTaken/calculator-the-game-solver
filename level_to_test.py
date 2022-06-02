from main import solve, Operator, Token

if False:
    # To make the IDE recognise them as used imports
    solve
    Operator


def get_test_for_level(level: str):
    """Example usage:
```
    get_test_for_level("solve(2, 2, 0, [Token(1, Operator.addition)])")
```

returns a string of:
```
    def test_level_9000000(self):
        level = solve(2, 2, 0, [Token(1, Operator.addition)])
        self.assertTrue([
                Token(1, addition),
                Token(1, addition)
        ] in level)
```
"""

    results: list[list[Token]] = eval(level)
    pad = " "*4

    result = "[\n{}".format(pad * 4) + \
        ((f",\n{pad*4}").join([f"Token({x.value}, Operator.{x.operation.name})" for x in results[0]])) + \
        "\n{}]".format(pad * 2)

    return "{}def test_level_9000000(self):\n{}{}level = {}\n".format(
        pad, pad, pad, level
    ) + ("{}self.assertTrue({} in level)".format(pad * 2, result))


print(
    get_test_for_level(
        "solve(7, 4, 0, [Token(2, Operator.insert), Token(1, Operator.addition), Token(3, Operator.division), Token(None, Operator.reverse)])"
    )
)
