import pytest
with open('README.md') as f:
    line = f.readline()
assert(line=="# demo-CI-test\n")