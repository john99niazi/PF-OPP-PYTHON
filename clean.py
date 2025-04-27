# cleaning empty cells
#One way to deal with empty cells is to remove rows that contain empty cells.

#import pandas as pd

#df = pd.read_csv("D:/python/opp_in_python/New Text Document.csv")

#new_df = df.dropna()
##########################One way to deal with empty cells is to remove rows that contain empty cells.
#print(new_df.to_string())


#df.dropna(inplace = True)
###########################Remove all rows with NULL values
#print(df.to_string())

###########################Replace NULL values with the number 130:
#j=df.fillna(130, inplace = True)
#print(df.to_string())

#############Replace NULL values in the "Calories" columns with the number 130:
#df["calories"].fillna(130, inplace = True)
#print(df.to_string())



#Calculate the MEAN, and replace any empty values with it:
#x = df["calories"].mean()
#df["calories"].fillna(x, inplace = True)
#print(df.to_string())

#Calculate the MEDIAN, and replace any empty values with it:
#x = df["calories"].median()
#df["calories"].fillna(x, inplace = True)
#print(df.to_string())


#Calculate the mode, and replace any empty values with it:
#x = df["calories"].mode()[0]
#df["calories"].fillna(x, inplace = True)
#print(df.to_string())

###########################################claening wrong fromat
#Cells with data of wrong format can make it difficult, or even impossible, to analyze data.

#To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.



'''
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("D:/python/opp_in_python/New Text Document.csv")

# Attempt to convert the 'date' column to datetime, handling errors
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Optionally drop rows with invalid date entries
df.dropna(subset=['date'], inplace=True)

# Reset index after dropping rows (if necessary)
df.reset_index(drop=True, inplace=True)

# Display the DataFrame to check if dates are correctly parsed
print(df.head())'''




