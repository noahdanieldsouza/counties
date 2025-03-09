import csv


with open('countypres_2000-2020.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    # Get the list of columns (header) from the fieldnames
    read_data_columns = reader.fieldnames
    # Find the index of each desired column
    ryear_index = read_data_columns.index('year')
    rstate_index = read_data_columns.index('state')
    rstate_po_index = read_data_columns.index('state_po')
    rcounty_name_index = read_data_columns.index('county_name')
    rcounty_fips_index = read_data_columns.index('county_fips')


    columns =  ['state', 'year', 'state_po',	'county_name',	'county_fips']
    parties = set()

  
    for row in reader:
        parties.add(row['party'])  

    
    columns.extend(parties)
    columns.append("total_votes")
    
    

    with open("restructured.csv", "w", newline='') as restructured:
        writer = csv.DictWriter(restructured, fieldnames=columns)
        writer.writeheader()

        
        # Reset file and reader
        file.seek(0)
        
        reader = csv.DictReader(file)
        print("Detected column names:", reader.fieldnames)

        county_data = {}
        
        for row in reader:
            key = (row['year'], row['state'], row['state_po'], row['county_name'], row['county_fips'])

            if key not in county_data:
                county_data[key] = {
                    'year': row['year'],
                    'state': row['state'],
                    'state_po': row['state_po'],
                    'county_name': row['county_name'],
                    'county_fips': row['county_fips'],
                    'total_votes': row['totalvotes'],
                    **{party: 0 for party in parties}  # Initialize all parties to "0"
                }
           
            county_data[key][row['party']] += int(row['candidatevotes'])
            

        writer.writerows(county_data.values())  # Write all rows at once
        




    

    
    




