from script import print_numbers


def test_print_numbers_returns_list():
    """Test that print_numbers returns a list"""
    result = print_numbers()
    assert isinstance(result, list)


def test_print_numbers_length():
    """Test that print_numbers returns exactly 100 items"""
    result = print_numbers()
    assert len(result) == 100


def test_print_numbers_fizz_replacement():
    """Test that multiples of 3 are replaced with 'fizz'"""
    result = print_numbers()
    
    # Check multiples of 3
    for i in range(1, 101):
        if i % 3 == 0:
            assert result[i - 1] == "fizz", f"Position {i} should be 'fizz' but got {result[i - 1]}"


def test_print_numbers_non_multiples():
    """Test that non-multiples of 3 are string representations of numbers"""
    result = print_numbers()
    
    # Check non-multiples of 3
    for i in range(1, 101):
        if i % 3 != 0:
            assert result[i - 1] == str(i), f"Position {i} should be '{i}' but got {result[i - 1]}"


def test_fizz_at_specific_positions():
    """Test that fizz appears at correct positions"""
    result = print_numbers()
    
    fizz_positions = [i for i in range(1, 101) if i % 3 == 0]
    expected_fizz_count = len(fizz_positions)
    actual_fizz_count = result.count("fizz")
    
    assert actual_fizz_count == expected_fizz_count, \
        f"Expected {expected_fizz_count} 'fizz' occurrences but got {actual_fizz_count}"


def test_fizz_multiples_of_3():
    """Test specific multiples of 3 have 'fizz'"""
    result = print_numbers()
    
    test_multiples = [3, 6, 9, 15, 30, 99]
    for num in test_multiples:
        assert result[num - 1] == "fizz", f"Position {num} should be 'fizz'"


def test_non_fizz_numbers():
    """Test specific non-multiples of 3 have correct numbers"""
    result = print_numbers()
    
    test_numbers = [1, 2, 4, 5, 7, 8, 10, 100]
    for num in test_numbers:
        assert result[num - 1] == str(num), f"Position {num} should be '{num}'"


def test_print_numbers_all_elements_are_strings():
    """Test that all elements in the result are strings"""
    result = print_numbers()
    
    for i, item in enumerate(result):
        assert isinstance(item, str), f"Item at position {i} is not a string: {type(item)}"


def test_print_numbers_first_and_last():
    """Test the first and last elements"""
    result = print_numbers()
    
    assert result[0] == "1", "First element should be '1'"
    assert result[-1] == "100", "Last element should be '100'"
