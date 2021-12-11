from greek_stemmer.closets import POS


def test_pos_tags() -> None:

    assert isinstance(POS.total_pos_tags, list)

    assert isinstance(POS.pos_tags, dict)
