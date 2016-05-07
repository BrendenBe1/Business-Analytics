import createDB
import dataGeneration
import graphSelection

if __name__ == "__main__":
    DATA_GENERATION = False

    # Create new databases
    if DATA_GENERATION:

        # Create list with amount of days in each month
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Loop through number of months in a year
        for month in range(1, 13):

            # Loop through amount of days per month
            for day in range(1, (months[month-1])+1):
                new_db_name = (str(month) + "-" + str(day) + "-2016.db")
                database = createDB.createDB(new_db_name)
                dataGeneration.dataGeneration(database)

    # Open the GUI
    GUI = graphSelection.GUI()
