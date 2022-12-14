def sort_set(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

        items_greater = []
        items_lower = []

        for item in sequence:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
        
        return sort_set(items_lower) + [pivot] + sort_set(items_greater)