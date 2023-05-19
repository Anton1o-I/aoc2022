
def read_file(file):
    return open(file)

def my_decision_pts(x):
    if 'X' in x:
        return 1
    if 'Y' in x:
        return 2
    if 'Z' in x:
        return 3
    
win_cond_dict = {
    'A X': 3,
    'A Y': 6,
    'A Z': 0,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 6,
    'C Y': 0,
    'C Z': 3
}
def win_pts(x):
    return win_cond_dict[x.strip()]

def calc_pts_rnd1(rnd):
    return sum([my_decision_pts(rnd), win_pts(rnd)])

def calc_total_part1(f):
    return sum([calc_pts_rnd1(rnd) for rnd in f])

our_decision_pts_dict = {
    'A': 1,
    'B': 2,
    'C': 3
}

our_decision_dict = {
    'A X': 'C',
    'A Y': 'A',
    'A Z': 'B',
    'B X': 'A',
    'B Y': 'B',
    'B Z': 'C',
    'C X': 'B',
    'C Y': 'C',
    'C Z': 'A'
}

def win_loss_pts(x):
    if 'X' in x:
        return 0
    if 'Y' in x:
        return 3
    if 'Z' in x:
        return 6

def calc_pts_rnd2(x):
    return sum([win_loss_pts(x), our_decision_pts_dict[our_decision_dict[x.strip()]]])
    
def calc_total_part2(f):
    return sum([calc_pts_rnd2(rnd) for rnd in f])

if __name__ == '__main__':
    f = read_file('./values.txt')
    rounds = [r for r in f]
    print(calc_total_part1(rounds))
    print(calc_total_part2(rounds))

