import createDB
import dataGeneration
import retrieveData
import dataAnalysis
import graphSelection

####################
# Creates database #
# Generates data   #
# Analyzes data    #
# Graphs data      #
####################

if __name__ == "__main__":
    database = createDB.createDB()
    dataGeneration.dataGeneration(database)
 #   dataAnalysis.dataAnalysis(database)
    GUI = graphSelection.GUI()