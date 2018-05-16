import pytest
with open('README.md') as f:
    line = f.readlines()
print(line[-1])
assert(line[-1]=='## just for testing purpose\n')
 