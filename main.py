__author__ = 'Brenden'
import create_DB
import data_generation
#import retrieve_data
#import data_analysis
import graph_selection

####################
# Creates database #
# Generates data   #
# Analyzes data    #
# Graphs data      #
####################

if __name__ == "__main__":
    #database = create_DB.createDB("sampledatabse.db")
    #data_generation.dataGeneration(database)
 #   dataAnalysis.dataAnalysis(database)
    #  GUI = graph_selection.GUI()

    # create list with amount of days in each month
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # loop thru number of months in a year
    for month in range(1, 13):
        # loop thru amount of days per month

        for day in range(1, (months[month-1])+1):
        #for day in range(1, 4): this is for smaller sample
            # hardcoding year as 2018 so not leap year like 2016 and i dont like 2017.
            new_db_name = (str(month) + "-" + str(day) + "-2018.db")
            database = create_DB.createDB(new_db_name)
            data_generation.dataGeneration(database)