def gardners_equation(velocity):
    alpha = 0.31
    beta = 0.25
    if velocity < 0:
        raise ValueError("negative value")

    return alpha * (velocity**beta)