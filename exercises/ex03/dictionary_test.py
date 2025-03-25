__author__: str = "730567389"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_1() -> None:
    """Tests to invert a number of farm animals"""
    assert invert({"cow": "sheep", "turtle": "bird"}) == {
        "sheep": "cow",
        "bird": "turtle",
    }


def test_invert_2() -> None:
    """Tests to invert a list of popular duos in Overwatch"""
    assert invert({"Tracer": "Winston", "Lucio": "Ana", "Mercy": "Ball"}) == {
        "Winston": "Tracer",
        "Ana": "Lucio",
        "Ball": "Mercy",
    }


def test_invert_edge_case() -> None:
    """Tests for an empty dictionary input"""
    assert invert({}) == {}


def test_count_1() -> None:
    """Tests for counting foods"""
    assert count(["Apple", "Apple", "Pear", "Apple", "Pear"]) == {"Apple": 3, "Pear": 2}


def test_count_2() -> None:
    """Tests for counting the votes of favorite colors"""
    assert count(["Blue", "Red", "Blue", "Blue", "Blue"]) == {"Blue": 4, "Red": 1}


def test_count_edge_case() -> None:
    """Tests for an empty list input"""
    assert count([]) == {}


def test_favorite_color_1() -> None:
    """Tests for my friend's favorite color"""
    assert (
        favorite_color(
            {
                "Caleb": "Green",
                "Austin": "Blue",
                "Jillian": "Green",
                "Xavier": "Blue",
                "Timmothy": "Green",
            }
        )
        == "Green"
    )


def test_favorite_color_2() -> None:
    """Tests for my family's favorite color"""
    assert (
        favorite_color(
            {"Brendan": "Red", "Emma": "Red", "Pamela": "Green", "Jason": "Green"}
        )
        == "Red"
    )


def test_favorite_color_edge_case() -> None:
    """Tests for an empty  dictionary input"""
    assert favorite_color({}) == ""


def test_bin_len_1() -> None:
    """Tests for a list of foods"""
    assert bin_len(["pear", "apple", "grape"]) == {4: {"pear"}, 5: {"apple", "grape"}}


def test_bin_len_2() -> None:
    """Tests for a list of three names"""
    assert bin_len(["Caleb", "Austin", "Jillian"]) == {
        5: {"Caleb"},
        6: {"Austin"},
        7: {"Jillian"},
    }


def test_bin_len_edge_case() -> None:
    """Tests for an empty list input"""
    assert bin_len([]) == {}
