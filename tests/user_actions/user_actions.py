#TODO write tests here

from functools import partial

from main.user_actions.actions_dictfile import actions


def act(action=""):
    """
    Performs action from actions specified in actions_dictfile
    (str) -> <function_call>

    :param action: specified by string
    :return: nothing
    """
    actions.get(action.lower(), partial(print, "No such action..."))()
    return actions.get(action.lower(), None)
