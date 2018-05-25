def get_string():
    with open('README.md') as f:
        line = f.readline()
    return(line)

def test_string_equal():
    assert(get_string() == "!!! demo-CI-test\n")