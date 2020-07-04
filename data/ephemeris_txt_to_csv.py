"""
Script for transforming the raw Tesla Roadster Ephemeris into a CSV for
parsing by the API.
"""

import csv 

with open("./tesla_ephemeris.txt", "r") as tesla_ephemeris:
    ephemeris_data = tesla_ephemeris.read().split("\n")

data_start_line = 176
data_end_line = 26437

right_ascension_data = [["Date", "Right Ascension"]]

for index in range(data_start_line, data_end_line):
    line_data = ephemeris_data[index].split(" ")
    date = line_data[1]
    right_ascension = " ".join(line_data[7:10])
    right_ascension_data.append([date, right_ascension])

with open("./tesla_right_ascension.csv", "w+") as tesla_right_ascension:
    csv_writer = csv.writer(tesla_right_ascension)
    for line in right_ascension_data:
        csv_writer.writerow(line)

