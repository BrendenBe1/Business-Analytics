__author__ = 'Brenden'
import createDB
import dataGeneration
#import retrieve_data
#import data_analysis
import graphSelection

####################
# Creates database #
# Generates data   #
# Analyzes data    #
# Graphs data      #
####################

if __name__ == "__main__":
    DATA_GENERATION = False

 #   dataAnalysis.dataAnalysis(database)

    if DATA_GENERATION:
        # create list with amount of days in each month
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # loop thru number of months in a year
        for month in range(1, 13):
            # loop thru amount of days per month

            for day in range(1, (months[month-1])+1):
                new_db_name = (str(month) + "-" + str(day) + "-2016.db")
                database = createDB.createDB(new_db_name)
                dataGeneration.dataGeneration(database)

    GUI = graphSelection.GUI()
