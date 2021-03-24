sample_dictionary = {"name": "Jose",
                     "marks": [70, 80, 90, 60, 40],
                     "exams": {
                         "final": 73,
                         "midterm": 50
                     }}

print(sample_dictionary["marks"])
print(sample_dictionary["marks"][2])

marks = sample_dictionary['marks']
print(marks[2])
print(sample_dictionary["exams"]["final"])
