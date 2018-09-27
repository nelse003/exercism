def hey(phrase):
    """Bob, A teenager chat bot.

    Parameters
    ------------
    phrase: str
        Phrase that is said to bob.

    Returns
    -----------
    str
        Bob answers 'Sure.' if you ask him a question.
        He answers 'Whoa, chill out!' if you yell at him.
        He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
        He says 'Fine. Be that way!' if you address him without actually saying anything.
        He answers 'Whatever.' to anything else.

    """

    phrase = phrase.rstrip()

    if phrase.endswith("?") and phrase.isupper():
        return  "Calm down, I know what I'm doing!"
    elif phrase.endswith("?"):
        return "Sure."
    elif phrase == "":
        return "Fine. Be that way!"
    elif phrase.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."

