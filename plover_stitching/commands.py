from plover_stitching.stitching import stitch_word, alternate_case

def stitch(ctx, cmdline):
    action = ctx.copy_last_action()
    # {:stitch:word:delimiter?}
    # E.g. {:stitch:A} {:stitch:B:~}
    args = cmdline.split(':')
    try:
        word = args[0]
    except IndexError:
        # A word was not provided
        return action
    try:
        delimiter = args[1]
    except IndexError:
        # Optional delimiter not provided, default to hyphen
        delimiter = '-'

    action = ctx.new_action()
    action.prev_attach = ctx.last_action.glue or ctx.last_action.next_attach
    action.glue = True
    action.text = delimiter + word if ctx.last_action.glue else word

    return action

def stitch_last_word(ctx, cmdline):
    args = cmdline.split(':')
    try:
        if args[0]:
            num_words_to_stitch = int(args[0])
        else:
            num_words_to_stitch = 1
    except IndexError:
        num_words_to_stitch = 1
    try:
        delimiter = args[1]
    except IndexError:
        # Optional delimiter not provided, default to hyphen
        delimiter = '-'

    action = ctx.copy_last_action()

    last_words = "".join(ctx.last_words(count=num_words_to_stitch))
    if last_words:
        action.text = stitch_word(last_words, delimiter=delimiter)
        action.prev_replace = last_words
        action.prev_attach = True
        action.word = None

    return action

def altcase(ctx, cmdline):
    # {:altcase:letter:invert?}
    # E.g. {:altcase:a} {:altcase:B} -- case is normalized per the
    # alternating rule below, so either case works as input.
    # A fresh run starts lowercase, unless a non-empty <invert> is given
    # (e.g. {:altcase:s:1}), which starts it uppercase instead.
    action = ctx.copy_last_action()
    args = cmdline.split(':')
    try:
        letter = args[0]
    except IndexError:
        # A letter was not provided
        return action
    invert = len(args) > 1 and bool(args[1])

    prev_text = ctx.last_action.text or ''
    is_continuation = bool(prev_text) and prev_text[-1].isalpha() and (
        ctx.last_action.glue or ctx.last_action.next_attach
    )
    use_upper = prev_text[-1].islower() if is_continuation else invert

    action = ctx.new_action()
    action.prev_attach = ctx.last_action.glue or ctx.last_action.next_attach
    action.glue = True
    action.text = letter.upper() if use_upper else letter.lower()

    return action

def altcase_last_word(ctx, cmdline):
    # {:altcase_last_word:count?:invert?}
    # Each word starts lowercase, unless a non-empty <invert> is given
    # (e.g. {:altcase_last_word::1}), which starts each word uppercase.
    args = cmdline.split(':')
    try:
        if args[0]:
            num_words_to_altcase = int(args[0])
        else:
            num_words_to_altcase = 1
    except IndexError:
        num_words_to_altcase = 1
    invert = len(args) > 1 and bool(args[1])

    action = ctx.copy_last_action()

    last_words = "".join(ctx.last_words(count=num_words_to_altcase))
    if last_words:
        action.text = alternate_case(last_words, invert=invert)
        action.prev_replace = last_words
        action.prev_attach = True
        action.word = None

    return action
