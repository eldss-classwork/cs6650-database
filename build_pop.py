'''
Creates a populate.sql script programatically.
author: Evan Douglass
'''

resorts = [
    "Aspen Highlands Ski Resort",
    "Heavenly Mountain Resort",
    "Arapahoe Basin Ski Area",
    "Deer Valley Resort",
    "Whistler Blackcomb Ski Resort",
    "Aspen Snowmass",
    "Park City Mountain",
    "Big Sky Resort",
    "Sugar Bowl Resort",
    "Buttermilk Ski Resort",
    "Northstar California Resort",
    "Stevens Pass",
    "Silver Mountain",
]
lifts_per_resort = 60
num_skiers = 50000

with open("populate.sql", "w") as file:

    # Write some comments
    file.write(
        "-- Populates some simple data into the database.\n-- Large file since it needs to support up to 50k skiers.")
    file.write("\n\n")

    # Populate resorts
    file.write("INSERT INTO Resorts(resortID) VALUES ")
    for i in range(len(resorts) - 1):
        resort = resorts[i]
        file.write(f'({repr(resort)}),')
    file.write(f'({repr(resorts[-1])});\n\n')

    # Populate skiers
    # Break up into 50 lines of 1000
    skierID = 1
    for _ in range(50):
        file.write("INSERT INTO Skiers(skierID) VALUES ")
        for _ in range(999):
            file.write(f'({skierID}),')
            skierID += 1
        file.write(f'({skierID});\n')
        skierID += 1
    file.write("\n")

    # Populate lifts
    # Will give each resort the max number of lifts,
    # in reality this would not be how it works at all.
    # Be cautious in queries. Keep this in mind.
    #
    # The vertical will also be strange, as lift 60 will
    # always be 600m vertical rise. That is a tall lift!
    vertical_multiplier = 10
    for i in range(1, 62):
        file.write("INSERT INTO Lifts(liftNum, resortID, vertical) VALUES ")
        for j in range(len(resorts)-1):
            file.write(f'({i},{repr(resorts[j])},{i * vertical_multiplier}),')
        file.write(f'({i},{repr(resorts[-1])},{i * vertical_multiplier});\n')
