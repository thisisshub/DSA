import pytest
from A_mathematics import (
    A_count_digits,
    B_palindrome,
    C_gcd,
    D_lcm,
    E_factorial,
    F_prime_number,
    G_prime_factors,
    H_sieve_of_erathosthenes
)
 
class Test_A_mathematics:
    def test_count_digits(self):
        assert A_count_digits.method1(-1234) == 4
        assert A_count_digits.method1(0) == 1
        assert A_count_digits.method1(1234) == 4
        assert A_count_digits.method2(-1234) == 4
        assert A_count_digits.method2(0) == 1
        assert A_count_digits.method2(1234) == 4