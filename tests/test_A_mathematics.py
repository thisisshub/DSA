import sys

sys.path.append("../")

from A_mathematics import (
    A_count_digits,
    B_palindrome,
    C_gcd,
    D_lcm,
    E_factorial,
    F_prime_number,
    G_prime_factors,
    H_sieve_of_erathosthenes,
)


class Test_A_mathematics:
    def test_A_count_digits(self):
        assert A_count_digits.method1(-1234) == 4
        assert A_count_digits.method1(0) == 1
        assert A_count_digits.method1(1234) == 4
        assert A_count_digits.method2(-1234) == 4
        assert A_count_digits.method2(0) == 1
        assert A_count_digits.method2(1234) == 4

    def test_B_palindrome(self):
        assert B_palindrome.method1("aibohphobia") == True
        assert B_palindrome.method1("string") == False

    def test_C_gcd(self):
        assert C_gcd.method1(-123, -32) == 1
        assert C_gcd.method1(12, 18) == 6
        assert C_gcd.method1(-4, 14) == 2
        assert C_gcd.method2(-123, -32) == 1
        assert C_gcd.method2(12, 18) == 6
        assert C_gcd.method2(-4, 14) == 2

    def test_D_lcm(self):
        assert D_lcm.method1(2, 3) == 6
        assert D_lcm.method1(-2, 3) == 6
        assert D_lcm.method1(-2, -3) == 6
        assert D_lcm.method1(2, -3) == 6
        assert D_lcm.method2(2, 3) == 6
        assert D_lcm.method2(-2, 3) == 6
        assert D_lcm.method2(-2, -3) == 6
        assert D_lcm.method2(2, -3) == 6

    def test_E_factorial(self):
        assert E_factorial.method1(4) == 24
        assert E_factorial.method1(3) != 12
        assert E_factorial.method1(3) == 6
        assert E_factorial.method1(2) == 2
        assert E_factorial.method1(1) == 1
        assert E_factorial.method1(0) == 1

    def test_F_prime_number(self):
        assert F_prime_number.method1(-1) == False
        assert F_prime_number.method1(0) == False
        assert F_prime_number.method1(1) == False
        assert F_prime_number.method1(3) != False
        assert F_prime_number.method1(1) == False
        assert F_prime_number.method2(1) == False
        assert F_prime_number.method2(0) == False
        assert F_prime_number.method2(1) == False
        assert F_prime_number.method2(3) == True

    def G_prime_factors(self):
        assert G_prime_factors.method1(2) == []
        assert G_prime_factors.method1(4) == [2]
        assert G_prime_factors.method1(6) == [2, 3]
        assert G_prime_factors.method1(15) == [3, 5]
        assert G_prime_factors.method1(-10) == []

    def H_sieve_of_erathosthenes(self):
        assert H_sieve_of_erathosthenes.method1(-1) == []
        assert H_sieve_of_erathosthenes.method1(0) == []
        assert H_sieve_of_erathosthenes.method1(1) == []
        assert H_sieve_of_erathosthenes.method1(2) == []
        assert H_sieve_of_erathosthenes.method1(3) == [2]
        assert H_sieve_of_erathosthenes.method1(4) == [2, 3]
