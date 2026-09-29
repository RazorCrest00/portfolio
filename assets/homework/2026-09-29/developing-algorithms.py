# CODE_RUNNER: 3.09 Homework - Supply restock report
def restock_report(items, in_stock, target):
    # Validate parallel list lengths before matching names with quantities.
    if not (len(items) == len(in_stock) == len(target)):
        raise ValueError("Item, stock, and target lists must have equal lengths")
    # COLLECT only positive shortages, preserving the supplied order.
    short_items = []
    short_amounts = []
    for i in range(len(items)):
        if in_stock[i] < target[i]:
            short_items.append(items[i])
            short_amounts.append(target[i] - in_stock[i])
    # SUM shortages explicitly with a loop.
    total_needed = 0
    for amount in short_amounts:
        total_needed = total_needed + amount
    # FIND THE MAX by retaining its position; no position exists for an empty list.
    urgent_index = None
    for i in range(len(short_amounts)):
        if urgent_index is None or short_amounts[i] > short_amounts[urgent_index]:
            urgent_index = i
    # COMBINE the patterns into either the empty case or the requested report.
    if len(short_items) == 0:
        print("Fully stocked!")
    else:
        print("Restock needed:")
        for i in range(len(short_items)):
            print(short_items[i] + ": need " + str(short_amounts[i]))
        print("Total items needed:", total_needed)
        print("Most urgent: " + short_items[urgent_index] + " (short by " + str(short_amounts[urgent_index]) + ")")
    # Return evidence as data so tests do not have to duplicate the algorithms.
    return short_items, short_amounts, total_needed, urgent_index

# Supplied classroom inventory, not live nonprofit inventory.
items = ["Toothbrushes", "Blankets", "Socks", "Shampoo", "Notebooks"]
in_stock = [40, 8, 25, 5, 30]
target = [30, 20, 25, 15, 30]
restock_report(items, in_stock, target)
