'''
Columns of interest in followmedata.csv export data:

 "Position ID":          unique ID associated with a Job Share position at a company
 "Position Seat Count":  # of seats available for a specific "Position ID"
 "Wishlist Order":       how student ranked this company,  0 = highest, 2 = lowest
 "Company Name":         for mapping "Position ID" to a company
 "Student Name":         for mapping wishlist positions to a student
'''
import pandas as pd
from utils import printSummaryStats, printAllocationStats, printStudentResults
from alg1 import compute1, preFill

# Read job share data into Pandas dataframe
followme = pd.read_csv("./followmedata.csv")
followme = followme.reset_index()  # make sure indexes pair with number of rows

# iterate over exported data, building data structures for managing lottery algorithm
PositionDict = {}       # position ID, company name, position slots and position count wishlisted
StudentDict = {}        # student name, wishlist positions, assigned position and what wishlist rank they got

# Initialize data structures for tracking job allocations
for index, row in followme.iterrows():
    # initialize position table
    PositionDict[row["Position ID"]] = [row["Position ID"], 
                                        row["Company Name"],
                                        row["Position Seat Count"],
                                        0,   # desired 1st choice count
                                        0]   # number allocated
    # initialize student table
    StudentDict[row["Student Name"]] = [None, None, None, None, None]

# 2nd pass for StudentDict to populate wishlist choices
for index, row in followme.iterrows():
    if row["Wishlist Order"] == 0:
        StudentDict[row["Student Name"]][0] = row["Position ID"]
    if row["Wishlist Order"] == 1:
        StudentDict[row["Student Name"]][1] = row["Position ID"]
    if row["Wishlist Order"] == 2:
        StudentDict[row["Student Name"]][2] = row["Position ID"]

# Now calculate desired wishlist 0 position counts and update the Position dict
for index, row in followme.iterrows():
    if (row["Wishlist Order"] == 0):
        PositionDict[row["Position ID"]][3] += 1

# Print stats about positions and students to cross check with followmejobshadow.com site
printSummaryStats(PositionDict, StudentDict)

# If you want to pre-fill specific Job IDs, put the list here and uncomment this line
preferredJobs = { 341: .90,     # Flex
                  332: .90,     # Lockheed
                  331: .90,     # Intuitive Surgical
                  301: .90,     # HPE
                  340: .90,     # Amazon Devices
                  }      
#preFill(PositionDict, StudentDict, preferredJobs)

# Compute and output results of algorithm 1 selection
compute1(PositionDict, StudentDict)

# print 1st, 2nd, 3rd choide stats
printAllocationStats(PositionDict, StudentDict)

# Print 
printStudentResults(PositionDict, StudentDict)

