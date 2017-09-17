from time import strftime
from selenium import webdriver
from Other.test4 import *

ZIP = '90292'

d_one = {'firstName': 'Xue ', 'middleInitial': '', 'lastName': 'Liu',
         'street': '4750 Lincoln Boulevard ', 'aptNum': '286', 'city': 'Marina del Rey',
         'DOBMonth': '06', 'DOBDay': '06', 'DOBYear': '1989',
         'gender': 'f', 'martialStatus': 1,
         # 1:Single
         # 2:Married
         # 3:Separated
         # 4:Widowed
         # 5:Divorced

         'education': 7,
         # 1:No high school diploma or GED
         # 2:High school diploma or GED
         # 3:Vocational/trade school/military training
         # 4:Completed some college
         # 5:Currently in college
         # 6:College degree
         # 7:Graduate work or graduate degree

         'work': 1,
         # 1:Employed
         # 2:Homemaker
         # 3:Not working/Disabled/Other
         # 4:Retired
         # 5:Student

         'job': '',

         'residence': 1,
         # 1:Own home
         # 2:Own condominium
         # 3:Own manufactured/mobile home
         # 4:Rent
         # 5:Other

         'licenseStatus': 1,
         # 1:Valid
         # 2:Permit
         # 3:Suspended
         # 4:Permanently Revoked
         # 5:Expired
         # 6:Not licensed
         # 7:Commercial/Business
         # 8:Foreign driver's license

         'ageLicensed': '18', 'licenseOutsideUS': 'n', 'licenseBadThree': 'n',
         'ageLicenseOutUS': '0',
         'validEighteenMonths' : 'y',
         'licenseReinstatedMonth': '0',
         'licenseReinstatedDay': '0',
         'licenseReinstatedYear': '0',
         'damagesToCar': 'n',
         'typeOfDamage': 0,
         # 1:Collision with another vehicle
         # 2:Hit Object/Property
         # 3:Swerved/Lost control
         # 4:Hit an animal
         # 5:Victim of hit and run
         # 6:Acts of Nature/Weather related
         # 7:Object fell on vehicle(not weather related)
         # 8:Theft/Vandalism/Fire
         # 9:Windshield/Glass only
         # 10:Damage from pothole
         # 11:Hit pedestrian

         'howLongAgoDamage': 0,
         # 1:Within the last year
         # 2:1-3 years
         # 3:More than 3 years

         'DWI': 'n',
         'DWIMonth': '0', 'DWIDay': '0', 'DWIYear': '0',
         'tickets': 'n',
         'driverImprovementCourse': 'n',
         # Only matters if born before 1962
         'autoInsuranceToday': 'y',
         # 'currentAutoInsurance': ,
         # 1:Less than 1 year
         # 2:1 to 3 years
         # 3:More than 3 years
         'bodilyInjuryLimits': 4,
         # 1:$15,000/$30,000 (State Min) or less
         # 2:$25,000/$50,000
         # 3:$50,000/$100,000
         # 4:$100,000/$300,000 or higher
         'nonAutoProgressive': 'n',
         'continuedThreeYears': 'y',  # Have you had auto insurance for 3 years consecutively?
         'email': 'luckypython1@gmail.com',
         # 'householdHealthInsurance': '',
         # 'residentNumber':
         }

c_one = {'carYear': '2012',
         'carMake': 'Toyota',
         'carModel': 'Camry',
         'trackingDevice': 'n',
         'milesOneWay': '12',
         'ownOrLease': 2,
         # 1:Finance
         # 2:Own
         # 3:Lease

         'use': 1,
         # 1:Personal(to/from work, school, errands)
         # 2:Personal(including rideshare: Uber, Lyft) This means you have to get commercial insurance
         # 3:Pleasure(recreational driving only)
         # 4:Business(business errands, sales calls)
         # 5:Farming(agriculture, ranching)
         }

quote_one = {'BI_PD': '$250k/$500k/$100k',
             # $15k/$30k/$5k
             # $15k/$30k/$10k
             # $25k/$50k/$10k
             # $25k/$50k/$25k
             # $50k/$100k/$25k
             # $50k/$100k/$50k
             # $100k/$300k/$50k
             # $100k/$300k/$100k
             # $250k/$500k/$100k
             # $100k CSL
             # $300k CSL
             # $500k CSL

             'uninsuredMotoristBI': '$250k/$500k',
             # No coverage
             # $15k/$30k
             # $25k/$50k
             # $50k/$100k
             # $100k/$300k

             'medicalPayments': 'No Coverage',
             # No coverage
             # $1k per person
             # $2k per person
             # $5k per person
             # $10k per person

             'comprehensive': 'No Coverage',
             # No coverage
             # $100 deductible
             # $250 deductible
             # $500 deductible
             # $1,000 deductible
             # $2,500 deductible

             'collision': 'No Coverage',
             # No coverage
             # $100 deductible
             # $250 deductible
             # $500 deductible
             # $1,000 deductible
             # $2,500 deductible

             'collisionDeductibleWaiver': 'No Coverage',
             # No coverage
             # Whatever the collision deductible is

             'uninsuredMotoristPD': 'No Coverage',

             'rental': 'n',
             # No coverage
             # $30 per day ($900 maximum)
             # $40 per day ($1,200 maximum)

             'roadside': 'n'
             # No coverage
             # Coverage selected
             }

bundle_product = 'a'

auto_exception = 0
skip_bundle_exception = 0

b = webdriver.Chrome()
b.set_window_size(1000, 750)
b.set_window_position(0, 0)
b.get('https://www.progressive.com')
print('page')
while auto_exception < 20:
    try:
        b.find_element_by_xpath('//*[@id="primary"]/div/ul[1]/li[2]').click()
        print('clicked auto option')
        break
    except NoSuchElementException:
        sleep(0.25)
        print('auto_exception one')
        close_survey(b)
        auto_exception += 1
    except ElementNotVisibleException:
        sleep(0.25)
        print('auto exception 2')
        close_survey(b)
        auto_exception += 1
else:
    print('no auto option found')
input_text(b, 'zipCode_ueno', ZIP)
sleep(3)
b.find_element_by_id('qsButton_ueno').click()

print('zip code entered')

profile_page(b, d_one)

vehicle_page(b, c_one)

click_next_button(b)
print('finished vehicle page')

close_survey(b)

final_detail_page(b, d_one)

close_survey(b)
click_next_button(b)

close_survey(b)
print('driver page finished')

close_survey(b)

verify_page(b, d_one)

click_next_button(b)

if bundle_product.lower().strip() == 'a':
    b.find_element_by_id('no-thanks-link').click()
    skip_bundle_exception = 11
elif bundle_product.lower().strip() == 'h':
    b.find_element_by_id('product-button-0').click()
    click_next_button(b)
elif bundle_product.lower().strip() == 'r':
    b.find_element_by_id('product-button-1').click()
    click_next_button(b)
elif bundle_product.lower().strip() == 'c':
    b.find_element_by_id('no-thanks-link').click()
else:
    print('bundle product variable is not h, a, r, or c.')

while skip_bundle_exception < 20:
    try:
        b.find_element_by_xpath("//*[contains(text(), 'Skip this, see Auto rate now')]").click()
        break
    except NoSuchElementException:
        sleep(0.25)
        skip_bundle_exception += 1

edit_quote(b, quote_one)
