import solution


def rgb2tuple(rgb):
    return rgb.red, rgb.green, rgb.blue


def test_instances():
    assert isinstance(solution.red, solution.RGB)
    assert isinstance(solution.green, solution.RGB)
    assert isinstance(solution.blue, solution.RGB)


def test_attributes():
    assert rgb2tuple(solution.red) == (255, 0, 0)
    assert rgb2tuple(solution.green) == (0, 255, 0)
    assert rgb2tuple(solution.blue) == (0, 0, 255)