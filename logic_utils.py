def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    # FIXME: Logic broke here - Hard was 1-50, easier than Normal (1-100). Fixed: Hard is now 1-200.
    # FIX: Claude Code noticed Hard's range was smaller than Normal's; I approved raising it to 1-200.
    if difficulty == "Hard":
        return 1, 200
    return 1, 100


def parse_guess(raw: str, low: int = 1, high: int = 100):
    """
    Parse user input into an int guess within [low, high].

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # FIXME: Logic broke here - any number was accepted (0, -5, 150). Fixed: reject guesses outside [low, high].
    # FIX: I found this bug while playing and asked Claude Code to limit guesses to 1-100; verified in the browser + pytest.
    if value < low or value > high:
        return False, None, f"Enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIXME: Logic broke here - hints were backwards, and a try/except fell back to comparing
    # strings ("9" > "50" is True). Fixed: compare ints only, Too High -> Go LOWER.
    # FIX: I corrected the hint text first; Claude Code found the string-comparison fallback and removed it. Covered by pytest.
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIXME: Logic broke here - "Too High" added +5 on even attempts. Fixed: every wrong guess is -5.
    # FIX: Claude Code spotted the +5 on even attempts; I approved making every wrong guess -5.
    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
