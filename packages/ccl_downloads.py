import pandas as pd

# Temporary download option is given


def downloadScrapData(ccl_data):
    data = pd.DataFrame({'First Name': ccl_data['fname'], 'Last Name': ccl_data['lname'], 'Designation': ccl_data['designation'],
                         'Company Name': ccl_data['compName'], 'Location': ccl_data['location']})
    data.to_csv('Downloads/DataScrapped.csv', index=True,
                index_label='Sr. No.', encoding='utf-8')

    print("________________________________________________________________________________________________________")
    print(data)
    print("________________________________________________________________________________________________________")
    print('CSV is Downloaded ..!!!')
    ccl_data.clear()
    return data
