import pandas as pd

# Run this script to build the model into an xlsx file

# Each part of the model, as a csv or xlsx file, read as a dataframe
countries = pd.read_excel(r"C:\\Users\\gusta\\GitHub\\Data501_Project\\European Countries.xlsx")
msci = pd.read_csv(r"C:\\Users\\gusta\\GitHub\\Data501_Project\\governance\\MSCI Ratings Aggregated.csv")
ccpi = pd.read_csv(r"C:\\Users\\gusta\\GitHub\\Data501_Project\\Environmental\\ccpi_2024.csv")
wpr = pd.read_csv(r"C:\\Users\\gusta\\GitHub\\Data501_Project\\Climate_risk\\2023_WPR_Natural_Disaster_Index_Europe.csv")


# Recall that the nominal_gdp data is in billions, and the bonds are to the dollar
bonds_per_gdp = pd.read_csv(r"C:\\Users\\gusta\\GitHub\\Data501_Project\\Bonds\\Europe_Green_Bonds_Percentage_of_GDP.csv")
bonds_per_gdp.replace({"Slovak Republic": "Slovakia"}, inplace=True)

# Resulting model
model = pd.merge(countries, msci, on = 'Country', how = 'left')\
            .merge(ccpi, on = 'Country', how = 'left')\
            .merge(wpr, on = 'Country', how = 'left')\
            .merge(bonds_per_gdp, on="Country", how="left")

model.to_excel("Current_Model_Build.xlsx", index=False)