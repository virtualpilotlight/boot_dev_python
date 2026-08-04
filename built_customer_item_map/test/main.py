def build_customer_item_map(orders):
    orders_dics = {}
    for order in orders:
        scope_set = set()
        if order["customer"] not in orders_dics:
            current_cust = order["customer"]
            #print(current_cust)
            #print(type(order["items"]))
            for items in order["items"]:
                #print(items)
                scope_set.add(items)
            #print(scope_set)
            orders_dics[current_cust] = scope_set
            #print(orders_dics)
        elif order["customer"] in orders_dics:
            current_cust = order["customer"]
            #print(current_cust)
            for items in order["items"]:
                print(items)
                orders_dics[current_cust].add(items)
                print(orders_dics[current_cust])
            

    return orders_dics

