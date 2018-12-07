from pytest_bdd import given, when, then, scenario


@scenario(
    'przyklad.feature',
    'Przykładowy scenariusz',
    example_converters={'start': int, 'eat': float, 'left': str}
)
def test_przykladowy():
    pass


@given('Mając <start> ogórków')
def start_cucumbers(start):
    assert isinstance(start, int)
    return [start]


@when('Zjadłem <eat> ogórków')
def eat_cucumbers(start_cucumbers, eat):
    assert isinstance(eat, float)
    start_cucumbers.append(eat)


@then('Powinno mi zostać <left> ogórków')
def should_have_left_cucumbers(start_cucumbers, start, eat, left):
    assert isinstance(left, str)
    assert start - eat == int(left)
    assert start_cucumbers[0] == start
    assert start_cucumbers[1] == eat
