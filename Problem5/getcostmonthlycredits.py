import boto3 
import sys
import xlwt
from xlwt import Workbook

client = boto3.client('ce', region_name='us-east-1') #any specific region
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
  
#startdate and enddate
def get_credits(startdate, enddate):
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': startdate,
            'End': enddate
        },
        Granularity='MONTHLY',
        Metrics=[
            'AmortizedCost',
        ]
    )
    return response


if __name__ == '__main__':
    try:
        lastmonthprice = sys.argv[0]
        startdate = sys.argv[1]
        enddate = sys.argv[2]
    except ValueError:
        print('Enter Last Month Usage')
        print('Enter Start Date from which you want to check the credits in dd-mm-yyyy')
        print('Enter End Date from which you want to check the credits in dd-mm-yyyy')
    
    usedmonthcredits = get_credits(startdate, enddate)
    usagecurrentmonth = usedmonthcredits['price'] - lastmonthprice
    print('Usage for the mentioned Date:' + usagecurrentmonth)
    sheet1.write(startdate, enddate, lastmonthusage, usagecurrentmonth)