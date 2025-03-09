import csv

with open('restructured2.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    read_data_columns = reader.fieldnames
    # Find the index of each desired column
    ryear_index = read_data_columns.index('year')
    rstate_index = read_data_columns.index('state')
    rstate_po_index = read_data_columns.index('state_po')
    rcounty_name_index = read_data_columns.index('county_name')
    rcounty_fips_index = read_data_columns.index('county_fips')
    rdemocrat_index = read_data_columns.index('DEMOCRAT')
    print(rdemocrat_index)
    rrepublican_index = read_data_columns.index('REPUBLICAN')
    rowcount = 0
    for row in reader:

        rowcount += 1
        if int(row["DEMOCRAT"]) == 0:
            print(row["county_name"] + " " + row['county_fips'] + " " + row["state"] + " " + row["year"] + "democrat 0 at " + str(rowcount))
        if int(row["REPUBLICAN"]) == 0:
         print(row["county_name"] + " " + row["state"] + " " + row["year"] + "republican 0")
         if int(row["DEMOCRAT"]) > int (row["total_votes"] ) or  int(row["REPUBLICAN"]) > int (row["total_votes"] ):
             print(row["county_name"] + " " + row['county_fips'] + " " + row["state"] + " " + row["year"] + "vote mismatch " + str(rowcount))


    

