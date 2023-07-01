from pynput.mouse import Listener

def on_left_click(x, y, button, pressed):
    if button == button.left and pressed:
        print(f"Координаты: x={x}, y={y}")

# Создание слушателя событий нажатия кнопки мыши
with Listener(on_click=on_left_click) as listener:
    listener.join()
