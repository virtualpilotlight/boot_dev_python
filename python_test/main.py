def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name not in enemies_dict:
            #i = 1
            enemies_dict[enemy_name] = 1
        else:
            x = enemies_dict.get(enemy_name)
            #print(x)
            x += 1
            #print(x)
            enemies_dict.update({enemy_name: x})
    return enemies_dict
