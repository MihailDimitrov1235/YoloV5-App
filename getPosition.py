def get_position(*xywh):
    print(*xywh)
    x, y = get_center(*xywh)

    if x < 0.2:
        x_pos = "left"
    elif x < 0.4:
        x_pos = "slightly left"
    elif x < 0.6:
        x_pos = "middle"
    elif x < 0.8:
        x_pos = "slightly right"
    else:
        x_pos = "right"

    if y < 0.2:
        y_pos = "top"
    elif y < 0.4:
        y_pos = "slightly up"
    elif y < 0.6:
        y_pos = "middle"
    elif y < 0.8:
        y_pos = "slightly down"
    else:
        y_pos = "bottom"

    return f"{x_pos}, {y_pos}"

def get_center(*xywh):
    print(*xywh)
    x, y, w, h = xywh
    center_x = x + w/2
    center_y = y + h/2
    return (center_x, center_y)