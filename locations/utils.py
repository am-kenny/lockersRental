
def fit_in_locker(locker_size: dict, luggage_size: dict):
    lockers_sizes = [locker_size.width, locker_size.height, locker_size.depth]
    luggage_sizes = [luggage_size["width"], luggage_size["height"], luggage_size["length"]]
    lockers_sizes.sort()
    luggage_sizes.sort()

    can_fit = True
    for i in range(3):
        if lockers_sizes[i] < luggage_sizes[i]:
            can_fit = False
            break

    return can_fit
