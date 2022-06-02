from main import solve, Token, Operator
import unittest


class TestLevels(unittest.TestCase):
    def test_level_01(self):
        level = solve(2, 2, 0, [Token(1, Operator.addition)])
        self.assertTrue([
            Token(1, Operator.addition),
            Token(1, Operator.addition)
        ] in level)

    def test_level_02(self):
        level = solve(8, 3, 0, [
            Token(2, Operator.addition),
            Token(3, Operator.addition)]
        )
        self.assertTrue([
            Token(3, Operator.addition),
            Token(2, Operator.addition),
            Token(3, Operator.addition)
        ] in level)

    def test_level_03(self):
        level = solve(12, 3, 0, [
            Token(2, Operator.addition),
            Token(1, Operator.addition),
            Token(4, Operator.multiplication)]
        )
        self.assertTrue([
            Token(2, Operator.addition),
            Token(1, Operator.addition),
            Token(4, Operator.multiplication)
        ] in level)

    def test_level_04(self):
        level = solve(7, 3, 1, [
            Token(4, Operator.addition),
            Token(2, Operator.subtraction)]
        )
        self.assertTrue([
            Token(4, Operator.addition),
            Token(2, Operator.subtraction),
            Token(4, Operator.addition)
        ] in level)

    def test_level_05(self):
        level = solve(20, 3, 0, [
            Token(4, Operator.multiplication),
            Token(4, Operator.addition)
        ])
        self.assertTrue([
            Token(4, Operator.addition),
            Token(4, Operator.multiplication),
            Token(4, Operator.addition),
        ] in level)

    def test_level_06(self):
        level = solve(10, 4, 100, [
            Token(3, Operator.addition),
            Token(5, Operator.division)
        ])
        self.assertTrue([
            Token(5, Operator.division),
            Token(5, Operator.division),
            Token(3, Operator.addition),
            Token(3, Operator.addition),
        ] in level)

    def test_level_07(self):
        level = solve(40, 4, 0, [
            Token(2, Operator.addition),
            Token(4, Operator.multiplication)
        ])
        self.assertTrue([
            Token(2, Operator.addition),
            Token(4, Operator.multiplication),
            Token(2, Operator.addition),
            Token(4, Operator.multiplication)
        ] in level)

    def test_level_08(self):
        level = solve(4, 3, 4321, [Token(None, Operator.pop)])
        self.assertTrue([
            Token(None, Operator.pop),
            Token(None, Operator.pop),
            Token(None, Operator.pop),
        ] in level)

    def test_level_09(self):
        level = solve(4, 3, 0, [
            Token(None, Operator.pop),
            Token(8, Operator.addition),
            Token(5, Operator.multiplication)
        ])
        self.assertTrue([
            Token(8, Operator.addition),
            Token(5, Operator.multiplication),
            Token(None, Operator.pop),
        ] in level)

    def test_level_10(self):
        level = solve(9, 4, 50, [
            Token(None, Operator.pop),
            Token(5, Operator.division),
            Token(3, Operator.multiplication)
        ])
        self.assertTrue([
            Token(None, Operator.pop),
            Token(5, Operator.division),
            Token(3, Operator.multiplication),
            Token(3, Operator.multiplication),
        ] in level)

    def test_level_11(self):
        level = solve(100, 3, 99, [
            Token(None, Operator.pop),
            Token(8, Operator.subtraction),
            Token(11, Operator.multiplication)
        ])
        self.assertTrue([
            Token(8, Operator.subtraction),
            Token(11, Operator.multiplication),
            Token(None, Operator.pop),
        ] in level)

    def test_level_12(self):
        level = solve(404, 5, 0, [
            Token(8, Operator.addition),
            Token(10, Operator.multiplication),
            Token(2, Operator.division)
        ])
        self.assertTrue([
            Token(8, Operator.addition),
            Token(10, Operator.multiplication),
            Token(10, Operator.multiplication),
            Token(8, Operator.addition),
            Token(2, Operator.division)
        ] in level)

    def test_level_13(self):
        level = solve(23, 4, 171, [
            Token(None, Operator.pop),
            Token(2, Operator.multiplication),
            Token(9, Operator.subtraction)
        ])
        self.assertTrue([
            Token(9, Operator.subtraction),
            Token(None, Operator.pop),
            Token(2, Operator.multiplication),
            Token(9, Operator.subtraction),
        ] in level)

    def test_level_14(self):
        level = solve(21, 5, 0, [
            Token(None, Operator.pop),
            Token(5, Operator.addition),
            Token(3, Operator.multiplication),
            Token(5, Operator.multiplication)
        ])
        self.assertTrue([
            Token(5, Operator.addition),
            Token(3, Operator.multiplication),
            Token(5, Operator.multiplication),
            Token(None, Operator.pop),
            Token(3, Operator.multiplication)
        ] in level)

    def test_level_15(self):
        level = solve(50, 3, 10, [
            Token(3, Operator.multiplication),
            Token(2, Operator.multiplication),
            Token(5, Operator.subtraction)
        ])
        self.assertTrue([
            Token(3, Operator.multiplication),
            Token(5, Operator.subtraction),
            Token(2, Operator.multiplication)
        ] in level)

    def test_level_16(self):
        level = solve(2, 5, 0, [
            Token(None, Operator.pop),
            Token(4, Operator.addition),
            Token(9, Operator.multiplication)
        ])
        self.assertTrue([
            Token(4, Operator.addition),
            Token(9, Operator.multiplication),
            Token(None, Operator.pop),
            Token(9, Operator.multiplication),
            Token(None, Operator.pop),
        ] in level)

    def test_level_17(self):
        level = solve(11, 2, 0, [Token(1, Operator.insert)])
        self.assertTrue([
            Token(1, Operator.insert),
            Token(1, Operator.insert),
        ] in level)

    def test_level_18(self):
        level = solve(101, 3, 0, [
            Token(1, Operator.insert),
            Token(0, Operator.insert)
        ])
        self.assertTrue([
            Token(1, Operator.insert),
            Token(0, Operator.insert),
            Token(1, Operator.insert),
        ] in level)

    def test_level_19(self):
        level = solve(44, 3, 0, [
            Token(2, Operator.insert),
            Token(2, Operator.multiplication)
        ])
        self.assertTrue([
            Token(2, Operator.insert),
            Token(2, Operator.insert),
            Token(2, Operator.multiplication),
        ] in level)

    def test_level_20(self):
        level = solve(35, 2, 0, [
            Token(3, Operator.addition),
            Token(5, Operator.insert)
        ])
        self.assertTrue([
            Token(3, Operator.addition),
            Token(5, Operator.insert),
        ] in level)

    def test_level_21(self):
        level = solve(56, 3, 0, [
            Token(1, Operator.insert),
            Token(5, Operator.addition)
        ])
        self.assertTrue([
            Token(5, Operator.addition),
            Token(1, Operator.insert),
            Token(5, Operator.addition),
        ] in level)

    def test_level_22(self):
        level = solve(9, 4, 0, [
            Token(2, Operator.addition),
            Token(3, Operator.division),
            Token(1, Operator.insert)
        ])
        self.assertTrue([
            Token(2, Operator.addition),
            Token(1, Operator.insert),
            Token(3, Operator.division),
            Token(2, Operator.addition),
        ] in level)

    def test_level_23(self):
        level = solve(10, 4, 15, [
            Token(0, Operator.insert),
            Token(2, Operator.addition),
            Token(5, Operator.division)
        ])
        self.assertTrue([
            Token(5, Operator.division),
            Token(2, Operator.addition),
            Token(0, Operator.insert),
            Token(5, Operator.division),
        ] in level)

    def test_level_24(self):
        level = solve(210, 5, 0, [
            Token(5, Operator.addition),
            Token(5, Operator.subtraction),
            Token(5, Operator.insert),
            Token(2, Operator.insert),
        ])
        self.assertTrue([
            Token(2, Operator.insert),
            Token(5, Operator.insert),
            Token(5, Operator.subtraction),
            Token(5, Operator.insert),
            Token(5, Operator.addition),
        ] in level)

    def test_level_25(self):
        level = solve(2020, 4, 40, [
            Token(0, Operator.insert),
            Token(4, Operator.addition),
            Token(2, Operator.division),
        ])
        self.assertTrue([
            Token(0, Operator.insert),
            Token(4, Operator.addition),
            Token(0, Operator.insert),
            Token(2, Operator.division),
        ] in level)

    def test_level_26(self):
        level = solve(11, 4, 0, [
            Token(12, Operator.insert),
            Token(None, Operator.pop)
        ])
        self.assertTrue([
            Token(12, Operator.insert),
            Token(None, Operator.pop),
            Token(12, Operator.insert),
            Token(None, Operator.pop),
        ] in level)

    def test_level_27(self):
        level = solve(102, 4, 0, [
            Token(10, Operator.insert),
            Token(1, Operator.addition),
            Token(None, Operator.pop)
        ])
        self.assertTrue([
            Token(10, Operator.insert),
            Token(10, Operator.insert),
            Token(None, Operator.pop),
            Token(1, Operator.addition),
        ] in level)

    def test_level_28(self):
        level = solve(222, 4, 0, [
            Token(1, Operator.insert),
            Token((1, 2), Operator.convert)
        ])
        self.assertTrue([
            Token(1, Operator.insert),
            Token(1, Operator.insert),
            Token(1, Operator.insert),
            Token((1, 2), Operator.convert),
        ] in level)

    def test_level_29(self):
        level = solve(93, 4, 0, [
            Token(6, Operator.addition),
            Token(7, Operator.multiplication),
            Token((6, 9), Operator.convert)
        ])
        self.assertTrue([
            Token(6, Operator.addition),
            Token((6, 9), Operator.convert),
            Token(7, Operator.multiplication),
            Token((6, 9), Operator.convert),
        ] in level)

    def test_level_30(self):
        level = solve(2321, 6, 0, [
            Token(1, Operator.insert),
            Token(2, Operator.insert),
            Token((1, 2), Operator.convert),
            Token((2, 3), Operator.convert),
        ])
        self.assertTrue([
            Token(1, Operator.insert),
            Token(2, Operator.insert),
            Token(1, Operator.insert),
            Token((2, 3), Operator.convert),
            Token((1, 2), Operator.convert),
            Token(1, Operator.insert),
        ] in level)

    def test_level_31(self):
        level = solve(24, 5, 0, [
            Token(9, Operator.addition),
            Token(2, Operator.multiplication),
            Token((8, 4), Operator.convert)
        ])
        self.assertTrue([
            Token(9, Operator.addition),
            Token(9, Operator.addition),
            Token((8, 4), Operator.convert),
            Token(2, Operator.multiplication),
            Token((8, 4), Operator.convert)
        ] in level)

    def test_level_32(self):
        level = solve(29, 5, 11, [
            Token(2, Operator.division),
            Token(3, Operator.addition),
            Token((1, 2), Operator.convert),
            Token((2, 9), Operator.convert),
        ])
        self.assertTrue([
            Token(3, Operator.addition),
            Token((1, 2), Operator.convert),
            Token(2, Operator.division),
            Token((2, 9), Operator.convert),
            Token((1, 2), Operator.convert)
        ] in level)

    def test_level_33(self):
        level = solve(20, 5, 36, [
            Token(3, Operator.addition),
            Token(3, Operator.division),
            Token((1, 2), Operator.convert)
        ])
        self.assertTrue([
            Token(3, Operator.addition),
            Token(3, Operator.addition),
            Token(3, Operator.division),
            Token(3, Operator.addition),
            Token(3, Operator.addition)
        ] in level)

    def test_level_34(self):
        level = solve(15, 4, 2, [
            Token(3, Operator.division),
            Token(1, Operator.insert),
            Token(2, Operator.multiplication),
            Token((4, 5), Operator.convert)
        ])
        self.assertTrue([
            Token(1, Operator.insert),
            Token(3, Operator.division),
            Token(2, Operator.multiplication),
            Token((4, 5), Operator.convert)
        ] in level)

    def test_level_35(self):
        level = solve(414, 4, 1234, [
            Token((23, 41), Operator.convert),
            Token((24, 14), Operator.convert),
            Token((12, 24), Operator.convert),
            Token((14, 2), Operator.convert)
        ])
        self.assertTrue([
            Token((12, 24), Operator.convert),
            Token((24, 14), Operator.convert),
            Token((14, 2), Operator.convert),
            Token((23, 41), Operator.convert)
        ] in level)

    def test_level_36(self):
        level = solve(-85, 4, 0, [
            Token(7, Operator.subtraction),
            Token(6, Operator.addition),
            Token(5, Operator.insert)
        ])
        self.assertTrue([
            Token(7, Operator.subtraction),
            Token(7, Operator.subtraction),
            Token(6, Operator.addition),
            Token(5, Operator.insert)
        ] in level)

    def test_level_37(self):
        level = solve(9, 3, 0, [
            Token(1, Operator.subtraction),
            Token(2, Operator.subtraction),
            Token(2, Operator.exponential)
        ])
        self.assertTrue([
            Token(1, Operator.subtraction),
            Token(2, Operator.subtraction),
            Token(2, Operator.exponential)
        ] in level)

    def test_level_38(self):
        level = solve(-120, 4, 0, [
            Token(5, Operator.multiplication),
            Token(6, Operator.subtraction),
            Token(4, Operator.insert)
        ])
        self.assertTrue([
            Token(4, Operator.insert),
            Token(6, Operator.subtraction),
            Token(4, Operator.insert),
            Token(5, Operator.multiplication)
        ] in level)

    def test_level_39(self):
        level = solve(144, 3, 0, [
            Token(1, Operator.subtraction),
            Token(2, Operator.insert),
            Token(2, Operator.exponential)
        ])
        self.assertTrue([
            Token(1, Operator.subtraction),
            Token(2, Operator.insert),
            Token(2, Operator.exponential)
        ] in level)

    def test_level_40(self):
        level = solve(5, 1, -5, [
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(None, Operator.switch)
        ] in level)

    def test_level_41(self):
        level = solve(-6, 3, 0, [
            Token(4, Operator.addition),
            Token(2, Operator.addition),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(4, Operator.addition),
            Token(2, Operator.addition),
            Token(None, Operator.switch)
        ] in level)

    def test_level_42(self):
        level = solve(-13, 4, 0, [
            Token(3, Operator.addition),
            Token(7, Operator.subtraction),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(3, Operator.addition),
            Token(3, Operator.addition),
            Token(None, Operator.switch),
            Token(7, Operator.subtraction)
        ] in level)

    def test_level_43(self):
        level = solve(60, 4, 0, [
            Token(5, Operator.addition),
            Token(10, Operator.subtraction),
            Token(4, Operator.multiplication),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(5, Operator.addition),
            Token(5, Operator.addition),
            Token(5, Operator.addition),
            Token(4, Operator.multiplication)
        ] in level)

    def test_level_44(self):
        level = solve(52, 5, 44, [
            Token(9, Operator.addition),
            Token(2, Operator.division),
            Token(4, Operator.multiplication),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(2, Operator.division),
            Token(None, Operator.switch),
            Token(9, Operator.addition),
            Token(4, Operator.multiplication),
            Token(None, Operator.switch)
        ] in level)

    def test_level_45(self):
        level = solve(10, 5, 9, [
            Token(5, Operator.addition),
            Token(5, Operator.multiplication),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(None, Operator.switch),
            Token(5, Operator.addition),
            Token(5, Operator.addition),
            Token(5, Operator.multiplication),
            Token(5, Operator.addition)
        ] in level)

    def test_level_46(self):
        level = solve(12, 5, 14, [
            Token(6, Operator.insert),
            Token(5, Operator.addition),
            Token(8, Operator.division),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(None, Operator.switch),
            Token(5, Operator.addition),
            Token(6, Operator.insert),
            Token(None, Operator.switch),
            Token(8, Operator.division)
        ] in level)

    def test_level_47(self):
        level = solve(13, 4, 55, [
            Token(9, Operator.addition),
            Token(None, Operator.switch),
            Token(None, Operator.pop)
        ])
        self.assertTrue([
            Token(None, Operator.pop),
            Token(None, Operator.switch),
            Token(9, Operator.addition),
            Token(9, Operator.addition)
        ] in level)

    def test_level_48(self):
        level = solve(245, 5, 0, [
            Token(3, Operator.subtraction),
            Token(5, Operator.insert),
            Token(4, Operator.multiplication),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(3, Operator.subtraction),
            Token(3, Operator.subtraction),
            Token(4, Operator.multiplication),
            Token(5, Operator.insert),
            Token(None, Operator.switch)
        ] in level)

    def test_level_49(self):
        level = solve(12, 4, 39, [
            Token(-3, Operator.multiplication),
            Token(3, Operator.division),
            Token(9, Operator.addition),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(3, Operator.division),
            Token(None, Operator.switch),
            Token(9, Operator.addition),
            Token(-3, Operator.multiplication)
        ] in level)

    def test_level_50(self):
        level = solve(126, 6, 111, [
            Token(3, Operator.multiplication),
            Token(9, Operator.subtraction),
            Token(None, Operator.switch),
            Token(None, Operator.pop)
        ])
        self.assertTrue([
            Token(3, Operator.multiplication),
            Token(None, Operator.pop),
            Token(None, Operator.switch),
            Token(9, Operator.subtraction),
            Token(3, Operator.multiplication),
            Token(None, Operator.switch)
        ] in level)

    def test_level_51(self):
        level = solve(3, 5, 34, [
            Token(5, Operator.subtraction),
            Token(8, Operator.addition),
            Token(7, Operator.division),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(5, Operator.subtraction),
            Token(None, Operator.switch),
            Token(8, Operator.addition),
            Token(None, Operator.switch),
            Token(7, Operator.division)
        ] in level)

    def test_level_52(self):
        level = solve(4, 5, 25, [
            Token(4, Operator.subtraction),
            Token(-4, Operator.multiplication),
            Token(3, Operator.division),
            Token(8, Operator.division),
            Token(None, Operator.switch)
        ])
        self.assertTrue([
            Token(4, Operator.subtraction),
            Token(3, Operator.division),
            Token(4, Operator.subtraction),
            Token(4, Operator.subtraction),
            Token(-4, Operator.multiplication)
        ] in level)

    def test_level_53(self):
        level = solve(21, 1, 12, [
            Token(None, Operator.reverse)
        ])
        self.assertTrue([
            Token(None, Operator.reverse)
        ] in level)

    def test_level_54(self):
        level = solve(51, 3, 0, [
            Token(6, Operator.addition),
            Token(9, Operator.addition),
            Token(None, Operator.reverse)
        ])
        self.assertTrue([
            Token(6, Operator.addition),
            Token(9, Operator.addition),
            Token(None, Operator.reverse)
        ] in level)

    def test_level_55(self):
        level = solve(101, 3, 100, [
            Token(1, Operator.insert),
            Token(9, Operator.addition),
            Token(None, Operator.reverse),
        ])
        self.assertTrue([
            Token(1, Operator.insert),
            Token(9, Operator.addition),
            Token(None, Operator.reverse)
        ] in level)

    def test_level_56(self):
        level = solve(100, 4, 1101, [
            Token(None, Operator.reverse),
            Token(1, Operator.subtraction)
        ])
        self.assertTrue([
            Token(None, Operator.reverse),
            Token(1, Operator.subtraction),
            Token(None, Operator.reverse),
            Token(1, Operator.subtraction)
        ] in level)

    def test_level_57(self):
        level = solve(58, 4, 0, [
            Token(4, Operator.addition),
            Token(4, Operator.multiplication),
            Token(3, Operator.subtraction),
            Token(None, Operator.reverse)
        ])
        self.assertTrue([
            Token(4, Operator.addition),
            Token(4, Operator.multiplication),
            Token(None, Operator.reverse),
            Token(3, Operator.subtraction)
        ] in level)

    def test_level_58(self):
        level = solve(4, 3, 6, [
            Token(1, Operator.insert),
            Token(4, Operator.division),
            Token(None, Operator.reverse)
        ])
        self.assertTrue([
            Token(1, Operator.insert),
            Token(None, Operator.reverse),
            Token(4, Operator.division)
        ] in level)

    def test_level_59(self):
        level = solve(21, 3, 15, [
            Token(9, Operator.addition),
            Token(5, Operator.multiplication),
            Token(None, Operator.reverse)
        ])
        self.assertTrue([
            Token(9, Operator.addition),
            Token(5, Operator.multiplication),
            Token(None, Operator.reverse)
        ] in level)

    def test_level_60(self):
        level = solve(13, 5, 100, [
            Token(2, Operator.division),
            Token(None, Operator.reverse)
        ])
        self.assertTrue([
            Token(2, Operator.division),
            Token(2, Operator.division),
            Token(None, Operator.reverse),
            Token(2, Operator.division),
            Token(2, Operator.division),
        ] in level)

    def test_level_61(self):
        level = solve(11011, 4, 10, [
            Token(None, Operator.reverse),
            Token(1, Operator.insert)
        ])
        self.assertTrue([
            Token(1, Operator.insert),
            Token(1, Operator.insert),
            Token(None, Operator.reverse),
            Token(1, Operator.insert),
        ] in level)


if __name__ == '__main__':
    unittest.main()
