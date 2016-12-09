# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break
            fields = line.split(",")
            entry = {}

            for i, value in enumerate(fields):
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1

    print("data[0]: ", data[0])
    return data 



def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline

    
test()

#1st draft

# def parse_file(datafile):
#     data = []
#     with open(datafile, "r") as f:
#         for line in f:
#             #print line
#             data.append(line.split(','))
#     #print("this is the data: ", data)

#     new_data = []
#     #NEW_DICT ={}
#     ##print("data[0]: ", data[0])
#     # ('data[0]: ', ['Title', 'Released', 'Label', 'UK Chart Position', 'US Chart Position', 'BPI Certification', 'RIAA Certification\n'])
#     labels = len(data[0]) #7
#     ##print("len(data[0]): ", labels)
#     len_data = len(data) #28
#     ##print("len(data): ", len_data)
#     for y in range(1, len_data): #from 1 to 27
#         NEW_DICT ={}
#         for x in range(0, labels): #from 0 to 6
#             NEW_DICT[data[0][x]] = data[y][x]
#         ##print("NEW_DICT: ", NEW_DICT)
#         new_data.append(NEW_DICT)
#     ##print("new_data[0] is: ", new_data[0])
#     ##print("new_data[1] is: ", new_data[1])
#     ##print("new_data[2] is: ", new_data[2])
#     data = new_data
#     print("data[0]: ", data[0])
#     return data

#Return value:
#('data[0]: ', {'Title': 'Please Please Me', 'RIAA Certification\n': 'Platinum\n', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'BPI Certification': 'Gold'})

#Expected value:
#firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}

#Difference: Order of 2 labels

