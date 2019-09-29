import pytest
from main import *

print("Initiating test \n\n\n\n\n\n")
assert cursorUp(0) == -1
assert cursorUp(-1) == -1
assert cursorUp(-100) == -1
assert cursorUp(0.1) == -1
assert cursorUp(1) == 0
assert cursorUp(5) == 0
print("Completed Test")