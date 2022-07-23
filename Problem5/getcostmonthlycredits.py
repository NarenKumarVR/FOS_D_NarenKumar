import boto3 
import sys
import xlwt
from xlwt import Workbook

client = boto3.client('ce', region_name='us-east-1') #any specific region
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

client = boto3.client(
    's3',
    aws_access_key_id = 'AKIA46SFIWN5AMWMDQVB', #add access key id
    aws_secret_access_key = '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', # add access key
    region_name = 'ap-south-1'
)
    
resource = boto3.resource(
    's3',
    aws_access_key_id = 'AKIA46SFIWN5AMWMDQVB',
    aws_secret_access_key = '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',
    region_name = 'ap-south-1'
)
  
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