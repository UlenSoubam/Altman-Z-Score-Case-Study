import pandas as pd

df = pd.read_csv(r"C:\Users\ulens\OneDrive\Documents\COURSERA\Google Data Analytics Professional Certificate\Financial Analysis project\reliance_industries_z_score\extracted_data.csv")
df
# Convert 'year' column to datetime format
df['year'] = pd.to_datetime(df['year'], format='%d-%m-%Y')
# Extract only the year, since date and months are the same
df['year'] = df['year'].dt.year.astype('Int64')

#remove duplicate
df = df.drop_duplicates()
#remove every other characters
df= df.apply(lambda col: col.str.replace
              (r"[,/;=?]", "", regex=True) 
              if col.dtype == "object" else col)
#remove NaN row
df= df.dropna()
#I wanted the data only from the financial statements
df = df.drop(['ebit', 'book_value_of_equity'], axis=1) 
#Export the cleaned file for calculation.
df.to_csv("cleaned_re.csv")
