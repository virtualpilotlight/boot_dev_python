def build_customer_item_map(orders):
    orders_dics = {}
    for order in orders:
        scope_set = set()
        if order["customer"] not in orders_dics:
            current_cust = order["customer"]
            for items in order["items"]:
                scope_set.add(items)
            orders_dics[current_cust] = scope_set
        elif order["customer"] in orders_dics:
            current_cust = order["customer"]
            for items in order["items"]:
                orders_dics[current_cust].add(items)

    return orders_dics

