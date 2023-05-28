from design_patterns.structural.adapter_object import RoundPeg, SquarePeg, SquarePegAdapter, RoundHole

def test_1_square_peg_adapter_fits_into_round_hole_pass():
    round_hole = RoundHole(5)
    square_peg = SquarePeg(7)
    square_peg_adapter = SquarePegAdapter(square_peg)
    assert round_hole.fits(square_peg_adapter)

def test_2_square_peg_adapter_fits_into_round_hole_fail():
    round_hole = RoundHole(5)
    square_peg = SquarePeg(8)
    square_peg_adapter = SquarePegAdapter(square_peg)
    assert not round_hole.fits(square_peg_adapter)