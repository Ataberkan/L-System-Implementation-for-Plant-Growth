import matplotlib.pyplot as plt
import math

# L-system parameters
angle = 25
iterations = 5  # You can change the number of iterations
axiom = "X"
rules = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}

# Function to generate the L-system string
def generate_lsystem(axiom, rules, iterations):
    current_string = axiom
    for _ in range(iterations):
        next_string = "".join(rules.get(char, char) for char in current_string)
        current_string = next_string
    return current_string

# Function to draw the L-system
def draw_lsystem(commands, angle):
    stack = []
    x, y = 0, 0
    current_angle = 90
    positions = [(x, y)]
    
    for command in commands:
        if command == 'F':
            x += math.cos(math.radians(current_angle))
            y += math.sin(math.radians(current_angle))
            positions.append((x, y))
        elif command == '+':
            current_angle += angle
        elif command == '-':
            current_angle -= angle
        elif command == '[':
            stack.append((x, y, current_angle))
        elif command == ']':
            x, y, current_angle = stack.pop()
            positions.append((None, None))  # Marker for pen lift
            
    return positions

# Generate the L-system string
lsystem_string = generate_lsystem(axiom, rules, iterations)

# Get the positions to draw
positions = draw_lsystem(lsystem_string, angle)

# Plotting the L-system
plt.figure(figsize=(10, 10))
x_values, y_values = [], []

for pos in positions:
    if pos[0] is None:  # Pen lift
        if x_values and y_values:
            plt.plot(x_values, y_values, color='green')
        x_values, y_values = [], []
    else:
        x_values.append(pos[0])
        y_values.append(pos[1])

if x_values and y_values:
    plt.plot(x_values, y_values, color='green')

plt.axis('equal')
plt.show()
