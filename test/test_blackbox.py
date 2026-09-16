from plover_build_utils.testing import BlackboxTester
from plover.registry import registry
from plover import system

class TestsBlackbox(BlackboxTester):

    @classmethod
    def setup_class(cls):
        super().setup_class()
        registry.update()
        system.setup('English Stenotype')

    def test_stitch_last_word(self):
        r'''
        "TEFT": "test",
        "S": "{:stitch_last_word}",

        TEFT/S  " t-e-s-t"
        '''

    def test_stitch_last_word_nonword(self):
        r'''
        "TEFT": "test",
        "KW-BG": "{,}",
        "PHE": "me",
        "S": "{:stitch_last_word:3}",

        TEFT/KW-BG/PHE/S  " t-e-s-t, m-e"
        '''

    def test_stitch_fingerspelling(self):
        r'''
        "A": "{:stitch:A}",
        "PW": "{:stitch:B}",
        "KR": "{:stitch:C}",
        "KW-BG": "{,}",

        A             ' A'
        PW/KR         ' A-B-C'
        *             ' A-B'
        *             ' A'
        PW/KW-BG/A/KR ' A-B, A-C'
        '''

    def test_altcase_last_word(self):
        r'''
        "TEFT": "test",
        "S": "{:altcase_last_word}",

        TEFT/S  " tEsT"
        '''

    def test_altcase_last_word_multiple(self):
        r'''
        "TEFT": "test",
        "KW-BG": "{,}",
        "PHE": "me",
        "S": "{:altcase_last_word:3}",

        TEFT/KW-BG/PHE/S  " tEsT, mE"
        '''

    def test_altcase_fingerspelling(self):
        r'''
        "A": "{:altcase:a}",
        "PW": "{:altcase:b}",
        "KR": "{:altcase:c}",
        "KW-BG": "{,}",

        A             ' a'
        PW/KR         ' aBc'
        *             ' aB'
        *             ' a'
        PW/KW-BG/A/KR ' aB, aC'
        '''

    def test_altcase_last_word_invert(self):
        r'''
        "TEFT": "test",
        "S": "{:altcase_last_word::1}",

        TEFT/S  " TeSt"
        '''

    def test_altcase_fingerspelling_invert(self):
        r'''
        "A": "{:altcase:a:1}",
        "PW": "{:altcase:b:1}",
        "KR": "{:altcase:c:1}",
        "KW-BG": "{,}",

        A             ' A'
        PW/KR         ' AbC'
        *             ' Ab'
        *             ' A'
        PW/KW-BG/A/KR ' Ab, Ac'
        '''
