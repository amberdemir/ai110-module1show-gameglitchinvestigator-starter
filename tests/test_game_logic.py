from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_out_of_range_rejected():
    # Guesses below 1 or above 100 should be rejected
    ok, _, _ = parse_guess("0", 1, 100)
    assert not ok
    ok, _, _ = parse_guess("101", 1, 100)
    assert not ok

def test_guess_at_range_edges_accepted():
    # 1 and 100 are valid guesses
    assert parse_guess("1", 1, 100) == (True, 1, None)
    assert parse_guess("100", 1, 100) == (True, 100, None)

def test_hint_compares_numbers_not_strings():
    # Bug: the secret was turned into a string on even attempts, so "9" > "50" was True.
    # As numbers, 9 is lower than 50 and 100 is higher than 82.
    outcome, _ = check_guess(9, 50)
    assert outcome == "Too Low"
    outcome, _ = check_guess(100, 82)
    assert outcome == "Too High"

def test_hint_messages_point_the_right_way():
    # Bug: "Too High" told the player to go HIGHER (and vice versa).
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
