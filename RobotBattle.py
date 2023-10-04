import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.energy = 100.0
        self.octant = 0  # Starting direction (facing upwards)
        self.commands = []
        self.current_command_index = 0

    def add_commands(self, command_string):
        self.commands.extend(command_string.split("\n"))

    def execute_command(self):
        """Execute the current command in the robot's sequence."""
        if not self.commands or self.energy <= 0:
            return

        command = self.commands[self.current_command_index]

        # Check for conditional command
        if command.startswith('='):
            condition, action = command.split(":")
            condition = condition[1:]

            # Check conditions
            if condition == 'R' and random.choice([True, False]):  # Simulate robot detection
                print(f"{self.name} detected a robot and will execute action: {action}")
                self._perform_action(action)
            elif condition == 'W' and random.choice([True, False]):  # Simulate wall detection
                print(f"{self.name} detected a wall and will execute action: {action}")
                self._perform_action(action)
            elif condition == '?':  # Random command
                if random.choice([True, False]):
                    print(f"{self.name} decided to execute random action: {action}")
                    self._perform_action(action)
            else:
                self._perform_action(command)

        else:
            self._perform_action(command)

        # Move to the next command (loop back to the start if at the end of the list)
        self.current_command_index = (self.current_command_index + 1) % len(self.commands)

def _perform_action(self, action):
    """Helper function to execute an action."""
    cmd = action[0]

    # Check if the action has an associated value (like "F8")
    val = int(action[1:]) if len(action) > 1 else None

    if cmd == "F":  # Forward
        # Simulating energy costs
        if random.choice([True, False]):  # Random choice to simulate hitting a wall or robot
            self.energy -= 0.33
        print(f"{self.name} moved forward!")
    elif cmd == "T":  # Turn clockwise
        self.octant = (self.octant + val) % 8
        print(f"{self.name} turned {val} octants clockwise!")
    elif cmd == "D":  # Turn to a specific octant
        self.octant = val % 8
        print(f"{self.name} turned to face octant {self.octant}!")
    elif cmd == "XL":  # Fire laser
        print(f"{self.name} fired a laser!")
        self.energy -= 0.10
    elif cmd == "XM":  # Fire missile
        print(f"{self.name} fired a missile!")
        self.energy -= 0.33
    elif cmd == "H":  # Halt
        print(f"{self.name} halted for {val} counts!")


def status(self):
        """Display the robot's current status."""
        print(f"{self.name} is facing octant {self.octant} with energy {self.energy}.\n")

def battle(robot1, robot2, rounds=10):
    """Simulate a battle between two robots for a given number of rounds."""
    for _ in range(rounds):
        print(f"--- Round {_+1} ---")
        robot1.execute_command()
        robot1.status()

        robot2.execute_command()
        robot2.status()

        # Check for victory conditions
        if robot1.energy <= 0:
            print(f"{robot2.name} is the winner!")
            break
        elif robot2.energy <= 0:
            print(f"{robot1.name} is the winner!")
            break

if __name__ == "__main__":
    # Initialize two robots
    alpha = Robot("Alpha")
    omega = Robot("Omega")

    # Add commands to the robots
    alpha.add_commands("=R:XM\n=W:T2\n=?:T1\nF8")
    omega.add_commands("D0:XL\nD1:XL\nD2:XL\nD3:XL")

    # Simulate a battle between the two robots
    battle(alpha, omega, 20)
