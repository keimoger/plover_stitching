################
Plover Stitching
################

Write stitched words like T-H-I-S or define stitched sequences like heh-heh-heh

Usage
=====

Stitched Fingerspelling
-----------------------

``{:stitch:letter:delimiter?}``

-  **letter**: the letter or word to fingerspell
-  **delimiter** *(optional)*: the character or word to join stitched letters with, *defaults to -*

Examples
^^^^^^^^

- Stitched capital letter alphabet

  - {:stitch:A}{:stitch:B} → A-B

- Joining repeated words

  - {:stitch:ha} → ha
  - {:stitch:ha}{:stitch:ha}{:stitch:ha} → ha-ha-ha

- Custom delimiter

  - {:stitch:lol:o} → lol
  - {:stitch:lol:o}{:stitch:lol:o}{:stitch:lol:o} → lololololol


Stitch Last Words
-----------------

``{:stitch_last_word:count?:delimiter?}``

- **count** *(optional)*: number of previous words to stitch, *defaults to 1*
- **delimiter** *(optional)*: the character or word to join stitched letters with, *defaults to -*

Examples
^^^^^^^^

- Stitch last word

  - this is a test{:stitch_last_word} → this is a t-e-s-t

- Stitch last 2 words

  - my name is John Doe{:stitch_last_word:2} → my name is J-o-h-n D-o-e

- Stitch last word with custom delimiter

  - I'm feeling fabulous{:stitch_last_word:1:✨} → I'm feeling f✨a✨b✨u✨l✨o✨u✨s

Alternating Case
-----------------

``{:altcase:letter:invert?}``

-  **letter**: the letter to add, alternating case each stroke
-  **invert** *(optional)*: a non-empty value starts a fresh run uppercase instead of lowercase

Examples
^^^^^^^^

- Alternating-case fingerspelling

  - {:altcase:s}{:altcase:o}{:altcase:m}{:altcase:e} → sOmE

- Inverted (uppercase-start) alternating-case fingerspelling

  - {:altcase:s:1}{:altcase:o:1}{:altcase:m:1}{:altcase:e:1} → SoMe

Alternating-Case Last Words
----------------------------

``{:altcase_last_word:count?:invert?}``

- **count** *(optional)*: number of previous words to re-case, *defaults to 1*
- **invert** *(optional)*: a non-empty value starts each word uppercase instead of lowercase

Examples
^^^^^^^^

- Re-case last word

  - something{:altcase_last_word} → sOmEtHiNg

- Re-case last 2 words

  - hello world{:altcase_last_word:2} → hElLo wOrLd

- Re-case last word, inverted (uppercase-start)

  - something{:altcase_last_word::1} → SoMeThInG

Fingerspelling Alphabet
=======================

Here is a fingerspelling dictionary so that you can stitch in capital letters, like when someone is spelling out a name:

.. code:: json

    {
        "A*FPLT": "{:stitch:A}",
        "PW*FPLT": "{:stitch:B}",
        "KR*FPLT": "{:stitch:C}",
        "TK*FPLT": "{:stitch:D}",
        "*EFPLT": "{:stitch:E}",
        "TP*FPLT": "{:stitch:F}",
        "TKPW*FPLT": "{:stitch:G}",
        "H*FPLT": "{:stitch:H}",
        "*EUFPLT": "{:stitch:I}",
        "SKWR*FPLT": "{:stitch:J}",
        "K*FPLT": "{:stitch:K}",
        "HR*FPLT": "{:stitch:L}",
        "PH*FPLT": "{:stitch:M}",
        "TPH*FPLT": "{:stitch:N}",
        "O*FPLT": "{:stitch:O}",
        "P*FPLT": "{:stitch:P}",
        "KW*FPLT": "{:stitch:Q}",
        "R*FPLT": "{:stitch:R}",
        "S*FPLT": "{:stitch:S}",
        "T*FPLT": "{:stitch:T}",
        "*UFPLT": "{:stitch:U}",
        "SR*FPLT": "{:stitch:V}",
        "W*FPLT": "{:stitch:W}",
        "KP*FPLT": "{:stitch:X}",
        "KWR*FPLT": "{:stitch:Y}",
        "STK*FPLT": "{:stitch:Z}",
        "STKPW*FPLT": "{:stitch:Z}"
    }
