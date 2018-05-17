def get_string():
    with open('README.md') as f:
        lines = f.readlines()
    return(lines[-1])

def test_string_equal():
    assert(get_string() == "### just for testing purpose\n")