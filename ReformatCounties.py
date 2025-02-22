import csv


with open('countypres_2000-2020.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)  
    column_data = [row['party'] for row in reader] 
    columns =  ['year',	'state', 'state_po',	'county_name',	'county_fips']
    year_index = columns.index('year')
    state_index = columns.index('state')
    state_po_index = columns.index('state_po')
    county_name_index = columns.index('county_name')
    county_fips_index = columns.index('county_fips')
    party_dict = {}
    count = columns.__len__ 
    for i in column_data:
        if not i in columns:
            columns.append(i)
            party_dict[f"{i}_index"] = count
            count = count + 1
    

    with open("restructured.csv", "w", newline = '') as restructured:
        writer = csv.writer(restructured,  quoting=csv.QUOTE_MINIMAL)
        writer.writerow(columns)
        read_data = reader[0]
        ryear_index =  read_data.index('year')
        rstate_index =  read_data.index('state')
        rstate_po_index =  read_data.index('state_po')
        rcounty_name_index =  read_data.index('county_name')
        rcounty_fips_index = read_data.index('county_fips')



            




            

       
        
          
        


    
       
        
   

        




    

    
    




