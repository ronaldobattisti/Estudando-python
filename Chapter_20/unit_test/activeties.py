def eat(food, is_healthy):
    if is_healthy:
        final = "and it's good"
    else:
        final = "and it's bad"
    return f"I'm eating {food} {final}"


def sleep(hours):
    if hours <= 8:
        return 'Still tired'
    else:
        return 'My back hurts'
