import pygal
from Die_roll import Die

#   Create two D6 dice.

die1 = Die()
die2 = Die()

#   Make some rolls, and store results in a list.
results = []

for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

    # Analyze the results
    frequencies = []
    max_result = die1.num_sides + die2.num_sides

    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)

#  Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
hist.x_title = "Result"
hist.y_title = "Frequency Of Result"

hist.add("D6 + D6", frequencies)
hist.render_to_file("dice_visual.svg")
print(frequencies)
