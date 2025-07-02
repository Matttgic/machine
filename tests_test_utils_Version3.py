from src.utils import format_player_name

def test_format_player_name():
    assert format_player_name("Jannik Sinner [ITA]") == "Sinner J."
    assert format_player_name("Carlos Alcaraz") == "Alcaraz C."
    assert format_player_name("Novak Djokovic") == "Djokovic N."
    assert format_player_name("Sinner Jannik") == "Jannik S."
    assert format_player_name("Roger Federer") == "Federer R."