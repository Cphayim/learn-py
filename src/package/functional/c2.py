origin = 0


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(5))
