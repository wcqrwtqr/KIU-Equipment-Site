import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WTCDataBase.settings')

import django
import  pandas as pd
django.setup()

from FAR.models import FAR_DB

def update_dbs():
    df = pd.read_csv('/Users/mohammedalbatati/Anaconda Projects/Others/Django bootcamp/KIU-Equipment-Site/FAR_Master.csv', sep=',')
    products = []
    for i in range(len(df)):
        products.append(
            FAR_DB(
                asset_num=df.iloc[i][0]
                serial_num=df.iloc[i][1]
                description=df.iloc[i][2]
                BU=df.iloc[i][3]
                BL=df.iloc[i][4]
                asset_life=df.iloc[i][5]
                acquisition_date=df.iloc[i][6]
                acquisition_cost=df.iloc[i][7]
                tot_deb_value=df.iloc[i][8]
                nvb=df.iloc[i][9]
                temp_location=df.iloc[i][10]
                equ_type=df.iloc[i][11]
            )
        )
        FAR_DB.objects.bulk_create(products)


if __name__ = '__main__':
    print('start filling')
    update_dbs()
