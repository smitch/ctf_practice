import sys
# import unittest

def sum(str_list):
    res=0
    for i in str_list:
        if i.startswith("0b"):
            res+=int(i, 2)
        elif i.startswith("0o"):
            res+=int(i, 8)
        elif i.startswith("0x"):
            res+=int(i, 16)
    return res

# class TestSum(unittest.TestCase):
#     def test_binary(self):
#         self.assertEqual(int("0b111", 2), 7)
#     def test_octal(self):
#         self.assertEqual(int("0o111", 8), 73)
#     def test_hexel(self):
#         self.assertEqual(int("0x111", 16), 273)
#     def test_sum_b(self):
#         self.assertEqual(sum(["0b111"]), 7)
#     def test_sum_o(self):
#         self.assertEqual(sum(["0o111"]), 73)
#     def test_sum_x(self):
#         self.assertEqual(sum(["0x111"]), 273)
#     def test_sum(self):
#         self.assertEqual(sum(["0b111", "0o111", "0x111"]), 353)
#         self.assertEqual(sum(["0b111", "0o111", "0x111", "0b111", "0o111"]), 433)

# class TestIO(unittest.TestCase):
#     def test_input(self):
#         self.assertEqual("0b111 0o111".split(" "), ["0b111", "0o111"])

if __name__ == '__main__':
    line=sys.stdin.readline()
    sys.stderr.write(line)
    ans = sum(line.split(" "))
    sys.stderr.write(str(ans)+"\n")
    print(ans)
    sys.stdout.flush()
    flag = sys.stdin.readline()
    sys.stderr.write(flag)
