from collections import deque
import random


class Lift:
    def __init__(self, num_floors):
        self.queue = deque()
        self.current_floor = 1
        self.num_floors = num_floors
        self.direction = "up"

    def request_floor(self, floor):
        if 1 <= floor <= self.num_floors:
            self.queue.append(floor)
            print(f"Floor {floor} requested.")
        else:
            print(f"Invalid floor request: {floor}")

    def move(self):
        if not self.queue:
            print("No pending requests.")
            return

        destination = self.queue.popleft()

        while self.current_floor != destination:
            if self.current_floor < destination:
                self.current_floor += 1
                self.direction = "up"
            else:
                self.current_floor -= 1
                self.direction = "down"
            print(f"Lift is at floor {self.current_floor}, moving {self.direction}.")

        print(f"Lift has arrived at floor {self.current_floor}.")

    def run(self):
        while True:
            action = input("Enter 'r' to request a floor, 'm' to move the lift, or 'q' to quit: ").lower()
            if action == 'r':
                floor = int(input("Enter the floor number: "))
                self.request_floor(floor)
            elif action == 'm':
                self.move()
            elif action == 'q':
                print("Exiting lift management system.")
                break
            else:
                print("Invalid action. Please try again.")

            print(f"Current queue: {list(self.queue)}")
            print(f"Lift is currently at floor {self.current_floor}")
            print()


# Create a lift with 10 floors
lift = Lift(10)

# Run the lift management system
lift.run()