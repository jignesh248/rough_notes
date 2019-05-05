from abc import ABCMeta, abstractmethod
from enum import Enum


class ButtonDirection(Enum):
    DOWN = -1
    UP = 1


class ElevatorDirection(Enum):
    DOWN = -1
    UP = 1
    IDLE = 0


class ButtonStatus(Enum):
    ON = 1
    OFF = 0


class IsQueud(Enum):
    YES = 1
    NO = 0


class DoorStatus(Enum):
    OPEN = 1
    CLOSE = 0


class Button(object):
    def __init__(self):
        self.status = ButtonStatus.OFF

    def press(self):
        if self.status == ButtonStatus.OFF:
            self.status = ButtonStatus.ON
        elif self.status == ButtonStatus.ON:
            self.status = ButtonStatus.OFF

    def get_status(self):
        return self.status


class FloorButton(Button):

    def __init__(self, direction):
        super().__init__()
        self.direction = direction

    def press(self, floor, elevator):
        super().press()
        if elevator.status == ElevatorDirection.IDLE and elevator.current_floor < floor.level:
            elevator.status = ElevatorDirection.UP
            elevator.move()
        elif elevator.status == ElevatorDirection.IDLE and elevator.current_floor > floor.level:
            elevator.status = ElevatorDirection.DOWN
            elevator.move()


class ElevatorButton(Button):
    def __init__(self,floor_object):
        super().__init__()
        self.floor = floor_object

    def press(self, elevator):
        self.floor.toggle_floor()
        elevator.move()


class Floor(object):
    def __init__(self, level):
        self.level = level
        self.up_button = FloorButton(ButtonDirection.UP)
        self.down_button = FloorButton(ButtonDirection.DOWN)
        self.is_set = IsQueud.NO

    def toggle_floor(self):
        if self.is_set == IsQueud.YES:
            self.is_set = IsQueud.NO
        else:
            self.is_set = IsQueud.YES

    def get_buttons(self):
        return self.up_button, self.down_button


class Elevator(object):
    def __init__(self, floors):
        self.floors = floors
        self.buttons = []
        self.door_status = DoorStatus.CLOSE
        self.status = ElevatorDirection.IDLE
        self.current_floor = 0
        for floor in floors:
            self.buttons.append(ElevatorButton(floor))

    def set_floor(self, floor_no):
        self.current_floor = floor_no

    def open(self):
        print("open door on {}".format(self.current_floor))
        self.door_status = DoorStatus.OPEN

    def close(self):
        print("close door on {}".format(self.current_floor))
        self.door_status = DoorStatus.CLOSE

    def next_up_set(self):
        for i in range(self.current_floor, len(self.floors)):
            if self.floors[i].is_set == IsQueud.YES or self.floors[i].up_button.get_status() == ButtonStatus.ON:
                return i

        for i in range(self.current_floor, len(self.floors)):
            if self.floors[i].down_button.get_status() == ButtonStatus.ON:
                return i

        return -1

    def next_down_set(self):
        for i in range(self.current_floor,-1,-1):
            if self.floors[i].is_set == IsQueud.YES or self.floors[i].down_button.get_status() == ButtonStatus.ON:
                return i

        for i in range(self.current_floor,-1,-1):
            if self.floors[i].up_button.get_status() == ButtonStatus.ON:
                return i
        return len(self.floors)+1

    def move(self):

        while True :
            while self.status == ElevatorDirection.UP and self.current_floor < self.next_up_set():
                self.current_floor += 1
                print("on floor {}".format(self.current_floor))
                if self.floors[self.current_floor].is_set == IsQueud.YES or self.floors[self.current_floor].up_button.get_status() == ButtonStatus.ON:
                    self.open()
                    # wait
                    self.floors[self.current_floor].toggle_floor()
                    self.floors[self.current_floor].up_button = ButtonStatus.OFF
                    self.close()

            if self.status != ElevatorDirection.DOWN and self.next_down_set() == self.current_floor:
                self.open()
                # wait
                self.floors[self.current_floor].down_button.status = ButtonStatus.OFF
                self.close()
                self.status = ElevatorDirection.DOWN
            else:
                break

            while self.status == ElevatorDirection.DOWN and self.current_floor > self.next_down_set():
                self.current_floor -= 1
                print("on floor {}".format(self.current_floor))
                if self.floors[self.current_floor].is_set == IsQueud.YES or self.floors[self.current_floor].down_button.get_status() == ButtonStatus.ON:
                    self.open()
                    self.floors[self.current_floor].down_button.status = ButtonStatus.ON
                    # wait
                    self.floors[self.current_floor].toggle_floor()
                    self.close()

            if self.status != ElevatorDirection.UP and self.next_up_set() == self.current_floor:
                self.open()
                # wait
                self.floors[self.current_floor].up_status = ButtonStatus.OFF
                self.close()
                self.status = ElevatorDirection.UP
            else:
                break


class ElevatorController(object):
    def __init__(self, floor_count):
        self.floors = []
        for i in range(floor_count+1):
            self.floors.append(Floor(i))

        self.elevator = Elevator(self.floors)

    '''
    This method will run elevator floor detection code for initialization
    For eg. purpose it is set to 0
    '''
    def initialize_elevator_location(self):
        self.elevator.set_floor(0)

    def get_elevator(self):
        return self.elevator

    def get_floors(self):
        return self.floors


if __name__ == "__main__":
    controller = ElevatorController(10)
    floors = controller.get_floors()
    elevator = controller.get_elevator()
    floors[5].down_button.press(floors[5], elevator)
    elevator.buttons[3].press(elevator)




