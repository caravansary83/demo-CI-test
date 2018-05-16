import pytest
with open('README.md') as f:
    line = f.readlines()
assert(line[-1]=='just for testing purpose\n')
 