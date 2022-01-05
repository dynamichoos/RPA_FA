from pynput import mouse

# class MyException(Exception): pass
def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed:
            ## Press = True : 버튼이 눌린 상태에서 유지
            #print("i'm in pressed")
            #print(pressed)

            pass

        else:
            ## Press = False : 버튼이 release된 상태에서 진입
            #print("i'm in button")
            #print(button)
            # button = Button.left 이며 raise를 통해서 Exception에 e로 보내짐

            raise Exception(button)


def on_click_right(x, y, button, pressed):
    if button == mouse.Button.right:
        if pressed:
            ## Press = True : 버튼이 눌린 상태에서 유지
            #print("i'm in pressed")
            #print(pressed)

            pass

        else:
            ## Press = False : 버튼이 release된 상태에서 진입
            #print("i'm in button")
            #print(button)
            # button = Button.left 이며 raise를 통해서 Exception에 e로 보내짐

            raise Exception(button)

def mouse_listener():
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except Exception as e:

            print('{0} was clicked'.format(e.args[0]))

            return x, y


def get_mouse_location():
    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except Exception as e:

            print('{0} was clicked'.format(e.args[0]))

            mouse_drag = mouse.Controller()
            xy_position = mouse_drag.position #현재 마우스 커서의 위치를 변수에 대입한다
            
            ##커서의 위치를 출력하고 tuple로 return
            print(xy_position)
            
            return xy_position


def get_mouse_location_right():
    with mouse.Listener(on_click=on_click_right) as listener:
        try:
            listener.join()
        except Exception as e:

            print('{0} was clicked'.format(e.args[0]))

            mouse_drag = mouse.Controller()
            xy_position = mouse_drag.position #현재 마우스 커서의 위치를 변수에 대입한다
            
            ##커서의 위치를 출력하고 tuple로 return
            print(xy_position)
            
            return xy_position