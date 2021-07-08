from random import randint


def get_element_index(progression):
    element_index = randint(0, len(progression))
    return element_index


def get_element_val(progression, element_index):
    element_val = str(progression[element_index])
    return element_val


def get_changed_progression(progression, element_val):
    progression = " ".join(map(str, progression))
    changed_progression = progression.replace(str(element_val), '..', 1)
    return changed_progression
