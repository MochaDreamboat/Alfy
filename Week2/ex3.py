
def input_list():

    nums = []
    total = 0

    def input_list_helper():
        entry = input("Give us a number")
        if entry == "":
            return None
        else:
            return float(entry)

    while True:
        entry = input_list_helper()
        if entry == None:
            break
        else:
            total += entry
            nums.append(entry)

    nums.append(total)

    return nums


def check_monotonic_sequence(arr):
    ups = [False, False]
    downs = [False, False]

    monotonicity = 0
    strong = True

    def check_direction(a, b):
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0

    if arr == None:
        return [False, False, False, False]

    if len(arr) == 0 or len(arr) == 1:
        return [True, True, True, True]

    for i in range(len(arr) - 1):
        change = check_direction(arr[i], arr[i+1])
        if change != 0 and monotonicity != 0 and monotonicity != change:
            return ups + downs
        if change == 0:
            strong = False
        if change != 0 and change != monotonicity:
            monotonicity = change

    if monotonicity == 1:
        ups[0] = True
        ups[1] = strong
    elif monotonicity == -1:
        downs[0] = True
        downs[1] = strong
    else:
        ups[0] = True
        downs[0] = True

    return ups + downs


def check_monotonic_sequence_inverse(bools):
    #Up strong
    up_strong = [1, 2, 3, 4] # T T F F
    up_weak = [1, 1, 2, 3] # T F F F

    down_strong = [4, 3, 2, 1] # F F T T
    down_weak = [4, 3, 3, 2] # F F T F

    constant = [1, 1, 1, 1] # T F T F

    if bools == [True, True, False, False]:
        return up_strong
    elif bools == [True, False, False, False]:
        return up_weak
    elif bools == [False, False, True, True]:
        return down_strong
    elif bools == [False, False, True, False]:
        return down_weak
    elif bools == [True, False, True, False]:
        return constant
    elif bools == [True, True, True, True]:
        return [1]
    else:
        return None