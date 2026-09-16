
from plover_stitching.stitching import (
    stitch_word,
    alternate_case,
)

def test_stitch_word():
    assert stitch_word(' testing ') == 't-e-s-t-i-n-g '
    assert stitch_word('have you got   ') == 'h-a-v-e y-o-u g-o-t   '
    assert stitch_word('have you got   ', delimiter='👏') == 'h👏a👏v👏e y👏o👏u g👏o👏t   '
    assert stitch_word('will\nyou\n') == 'w-i-l-l\ny-o-u\n'

def test_alternate_case():
    assert alternate_case(' testing ') == 'tEsTiNg '
    assert alternate_case('HAVE you GOT   ') == 'hAvE yOu gOt   '
    assert alternate_case("don't stop") == "dOn'T sToP"
    assert alternate_case('will\nyou\n') == 'wIlL\nyOu\n'

def test_alternate_case_invert():
    assert alternate_case(' testing ', invert=True) == 'TeStInG '
    assert alternate_case('HAVE you GOT   ', invert=True) == 'HaVe YoU GoT   '
    assert alternate_case("don't stop", invert=True) == "DoN't StOp"
