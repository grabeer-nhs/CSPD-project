from script import print_numbers


def test_print_numbers_output(capsys):
    """Test that print_numbers outputs numbers 1-100"""
    # Call the function
    print_numbers()

    # Capture stdout
    captured = capsys.readouterr().out.strip().split("\n")

    # Verify we have 100 lines
    assert len(captured) == 100

    # Verify each line contains the correct number
    for i, line in enumerate(captured, start=1):
        assert int(line) == i


def test_print_numbers_range(capsys):
    """Test that output covers the range 1-100"""
    print_numbers()
    captured = capsys.readouterr().out.strip().split("\n")
    numbers = [int(line) for line in captured]

    assert numbers[0] == 1
    assert numbers[-1] == 100
    assert set(numbers) == set(range(1, 101))
