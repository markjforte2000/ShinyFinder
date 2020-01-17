import cv2


def resize(frame):
    height, width, channels = frame.shape
    height = height // 2
    width = width // 2
    frame = cv2.resize(frame, (width, height))
    return frame


def write_text(frame, text, point):
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (0, 0, 255)
    font_scale = 1
    thickness = 2
    frame = cv2.putText(frame, text, point, font, font_scale, color, thickness, cv2.LINE_AA)
    return frame


def write_frame_info(model):
    height, width, channels = model.frame.shape
    height = int(0.8 * height)
    new_width = int(0.8 * width)
    point = (new_width, height)
    model.frame = write_text(model.frame, 'Battles: {}'.format(model.num_battles), point)
    new_width = int(0.1 * width)
    point = (new_width, height)
    model.frame = write_text(model.frame, 'Shinies: {}'.format(model.num_shinies), point)
    return model


def show(model):
    model = write_frame_info(model)
    frame = resize(model.frame)
    cv2.imshow('Frame', frame)

