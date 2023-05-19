def read_file(file):
    return open(file)

def create_inventory(f):
    total_inv = []
    temp_inv = []
    for x in f:
        if x == '\n':
            total_inv.append(temp_inv)
            temp_inv = []
        else:
            temp_inv.append(int(x))
    return total_inv

def sum_inventory(inventory_lists):
    return [sum(ind_inv) for ind_inv in inventory_lists]

def get_top_n(sums, n):
    sums.sort(reverse=True)
    return sums[:n]

def sum_top(top):
    return sum(top)
    
if __name__ == '__main__':
    f = read_file('./values.txt')
    inventory = create_inventory(f)
    sums = sum_inventory(inventory)
    print(f'Part 1: {get_top_n(sums, 1)}')
    print(f'Part 2: {sum_top(get_top_n(sums, 3))}')
    