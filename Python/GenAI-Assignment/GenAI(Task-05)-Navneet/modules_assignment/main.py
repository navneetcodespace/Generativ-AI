import Math_utils
import string_utils
from Math_utils import square
from Math_utils import add
from Math_utils import subtract
from string_utils import capitalize_words
from string_utils import reverse_string
from string_utils import word_count

from shop_package import (
    apply_discount,
    flat_discount,
    calculate_total,
    apply_tax,
)

print(square(3))
print(add(10,34))
print(subtract(23,89))

print(capitalize_words("hello world"))
print(reverse_string("hello world"))
print(word_count("How are you"))


print(apply_discount(20000, 13))
print(flat_discount(1000))
print(calculate_total([23, 12, 34, 56, 76]))
print(apply_tax(20000))