def parse_potion_count(count_text):
    try:
        number = int(count_text)
    except ValueError:
        raise ValueError(f"invalid potion count: {count_text}")    
    
    if number < 0:

        raise ValueError("potion count cannot be negative")

    return number
        

def use_potions(starting_potions, used_text):
    a_number = parse_potion_count(used_text)
    
    if a_number > starting_potions:
        raise ValueError("not enough potions")

    return starting_potions - a_number


def report_potions_left(starting_potions, used_text):
    try:
        potions = use_potions(starting_potions, used_text)
        return f"Potions left: {potions}"
    except ValueError as e:
        return f"Error: {e}"
        




    

