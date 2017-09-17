from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from time import sleep

unfinished = 2


def car_selection(browser, car_type):
    sleep(2)
    close_survey(browser)
    sleep(2)
    exception = 0
    while exception < 20:
        try:
            browser.find_element_by_xpath("//*[contains(text(), '" + str(car_type) + "')]").click()
            print('found', car_type)
            break
        except NoSuchElementException:
            print('no', car_type)
            sleep(0.25)
            close_survey(browser)
            exception += 1
    else:
        print(car_type, 'not found')
        exception = 0
        while exception < 20:
            try:
                browser.find_element_by_xpath("//*[contains(text(), '" + str(car_type).title() + "')]").click()
                print('found', car_type.title())
            except NoSuchElementException:
                print('no', car_type.title())
                sleep(0.1)
                close_survey(browser)
                exception += 1
        else:
            print(car_type.title(), 'not found')
            less = 0
            length = len(car_type)
            print(length)
            new_length = 10
            while new_length > 3:
                car_type = car_type[0:length - less]
                less += 1
                sleep(0.25)
                try:
                    browser.find_element_by_xpath("//*[contains(text(), '" + str(car_type.title()) + "')]").click()
                    browser.find_element_by_xpath("//*[contains(text(), '" + str(car_type) + "')]").click()
                except NoSuchElementException:
                    print('no', car_type)
                    sleep(0.1)
                    close_survey(browser)
                new_length = len(car_type)
            else:
                print('---------------------------------------------------------------------'
                      '====================================================================='
                      '<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><'
                      'CLICK OPTION MANUALLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


def click_yes_or_no(browser, variable, yes_element_id, no_element_id):
    close_survey(browser)
    exception = 0
    variable = variable.strip().lower()
    if variable == 'y':
        while exception < 20:
            try:
                browser.find_element_by_id(yes_element_id).click()
                print(yes_element_id, 'clicked')
                return 'yes'
            except WebDriverException:
                exception += 1
                sleep(0.25)
                close_survey(browser)
        else:
            print(yes_element_id, 'not clicked')
    elif variable == 'n':
        while exception < 20:
            try:
                browser.find_element_by_id(no_element_id).click()
                print(no_element_id, 'clicked')
                return 'no'
            except WebDriverException:
                exception += 1
                sleep(0.25)
                close_survey(browser)
        else:
            print(no_element_id, 'not clicked')
    else:
        print(yes_element_id, 'or', no_element_id, 'is not y or n.')


def select_dropdown(browser, dropdown_id, index):
    close_survey(browser)
    check_cover = 0
    while check_cover < 20:
        try:
            s = Select(browser.find_element_by_id(dropdown_id))
            s.select_by_index(index)
            print(dropdown_id, 'selected')
            return 'selected'
        except WebDriverException:
            check_cover += 1
            sleep(0.25)
    else:
        print(dropdown_id, 'not found.')
        return 'not selected'


def input_text(browser, input_id, text):
    input_exception = 0
    while input_exception < 20:
        try:
            browser.find_element_by_id(input_id).clear()
            browser.find_element_by_id(input_id).send_keys(text)
            print(input_id, 'found')
            return 'typed'
        except WebDriverException:
            sleep(0.25)
            input_exception += 1
    else:
        print(input_id, 'not found.')
        return 'not typed'


def close_survey(browser):
    sleep(0.5)
    count = 0
    while count < 5:
        try:
            browser.find_element_by_xpath('//*[@id="fsrOverlay"]/div/div/div/a').click()
            print('survey closed')
        except NoSuchElementException:
            break
        except ElementNotVisibleException:
            sleep(0.1)
    sleep(0.5)


def click_next_button(browser):
    next_exception = 0
    while next_exception < 20:
        try:
            sleep(1)
            btn = browser.find_element_by_id('next')
            btn.click()
            print('clicked next button')
            next_exception += 1
        except WebDriverException:
            next_exception += 1
            print('btn webdriver exception')
            close_survey(browser)
            sleep(0.25)
        except ElementNotVisibleException:
            next_exception += 1
            print('btn not visible exception')
            close_survey(browser)
            sleep(0.25)
        try:
            sleep(2)
            btn.click()
        except StaleElementReferenceException:
            print('btn stale')
            return 'clicked'
        except WebDriverException:
            print('btn')
            return 'clicked'
        except UnboundLocalError:
            continue
    else:
        print('next button exception')


def profile_page(browser, driver_dict):
    first_name = driver_dict['firstName']
    middle_initial = driver_dict['middleInitial']
    last_name = driver_dict['lastName']
    street = driver_dict['street']
    city = driver_dict['city']
    DOBMonth = driver_dict['DOBMonth']
    DOBDay = driver_dict['DOBDay']
    DOBYear = driver_dict['DOBYear']
    apartmentNumber = driver_dict['aptNum']

    sleep(3)
    input_text(browser, 'NameAndAddressFormModel_FirstName_Value', first_name)
    input_text(browser, 'NameAndAddressFormModel_MiddleInitial_Value', middle_initial)
    input_text(browser, 'NameAndAddressFormModel_LastName_Value', last_name)
    input_text(browser, 'NameAndAddressFormModel_MailingAddress_Value', street)
    input_text(browser, 'NameAndAddressFormModel_ApartmentUnit_Value', apartmentNumber)
    input_text(browser, 'NameAndAddressFormModel_City_Value', city)
    input_text(browser, 'NameAndAddressFormModel_DateOfBirth_Month', DOBMonth)
    input_text(browser, 'NameAndAddressFormModel_DateOfBirth_Day', DOBDay)
    input_text(browser, 'NameAndAddressFormModel_DateOfBirth_Year', DOBYear)
    click_next_button(browser)
    print('profile entered')


def vehicle_page(browser, car_dict):
    car_year = car_dict['carYear']
    car_make = car_dict['carMake']
    car_model = car_dict['carModel']
    use = car_dict['use']
    miles_one_way = car_dict['milesOneWay']
    own_or_lease = car_dict['ownOrLease']

    sleep(5)
    try:
        browser.find_element_by_id('hvdDialogPopupButton').click()
    except NoSuchElementException:
        pass
    car_selection(browser, car_year)
    car_selection(browser, car_make)
    car_selection(browser, car_model)

    sleep(3)
    try:
        body_style = Select(browser.find_element_by_id('UnlistedVehicleFormModel_BodyStyle_Value'))
        trim_count = 0
        for trim in body_style.options:
            if trim_count != 0:
                trim_value = trim.get_attribute('value')
                print(str(trim_count) + '.', trim_value)
            trim_count += 1
        input_body_style = input('Input the number corresponding to the correct body style.')
        body_style.select_by_index(input_body_style)
    except NoSuchElementException:
        pass
    sleep(3)
    select_dropdown(browser, 'UnlistedVehicleFormModel_VehicleUse_Value', use)
    print('vehicle use selected')

    if use == 1:
        sleep(3)
        miles = browser.find_element_by_id('UnlistedVehicleFormModel_OneWayMiles_Value')
        miles.send_keys(miles_one_way)
        print('one way miles input')

    sleep(2)
    select_dropdown(browser, 'UnlistedVehicleFormModel_OwnOrLease_Value', own_or_lease)
    print('ownership selected')
    sleep(3)
    click_next_button(browser)

    sleep(2)
    if use == 4:
        print('business check')
        click_yes_or_no(browser, business_uses, 'VehicleBusinessUseFormModel_ExcludeBusinessUse_Value_Y',
                        'VehicleBusinessUseFormModel_ExcludeBusinessUse_Value_N')
        click_next_button(browser)


def other_driver(browser, driver_dict):
    first_name = driver_dict['firstName']
    middle_initial = driver_dict['middleInitial']
    last_name = driver_dict['lastName']
    gender = driver_dict['gender']
    DOBMonth = driver_dict['DOBMonth']
    DOBDay = driver_dict['DOBDay']
    DOBYear = driver_dict['DOBYear']
    martial_status = driver_dict['martialStatus']
    relationship_to_driver_one = driver_dict['relationshipToDriverOne']
    license_status = driver_dict['licenseStatus']
    age_licensed = driver_dict['ageLicensed']
    license_three_years = driver_dict['licenseBadThree']
    reinstate_month = driver_dict['licenseReinstatedMonth']
    reinstate_day = driver_dict['licenseReinstatedDay']
    reinstate_year = driver_dict['licenseReinstatedYear']
    license_outside_US = driver_dict['licenseOutsideUS']
    age_licensed_outside_US = driver_dict['ageLicenseOutUS']
    valid_eighteen_months = driver_dict['validEighteenMonths']
    damages_to_car = driver_dict['damagesToCar']
    DWI = driver_dict['DWI']
    tickets = driver_dict['tickets']
    driver_improvement_course = driver_dict['driverImprovementCourse']
    gender_exception = 0
    driver_course_exception = 0
    sleep(3)
    browser.find_element_by_id('add-unlisted-driver-button').click()

    sleep(2)
    input_text(browser, 'EditDriverDetailsFormModel_DriverDetail_FirstName_Value', first_name)

    sleep(2)
    input_text(browser, 'EditDriverDetailsFormModel_DriverDetail_MiddleInitial_Value', middle_initial)

    sleep(2)
    input_text(browser, 'EditDriverDetailsFormModel_DriverDetail_LastName_Value', last_name)

    sleep(2)
    if gender.strip().lower() == 'm':
        while gender_exception < 20:
            try:
                browser.find_element_by_id('EditPniDetailsFormModel_DriverDetail_Gender_Value_M').click()
                print('gender male')
                break
            except WebDriverException:
                sleep(0.25)
        else:
            print('male gender not found')
    elif gender.strip().lower() == 'f':
        while gender_exception < 20:
            try:
                browser.find_element_by_id('EditPniDetailsFormModel_DriverDetail_Gender_Value_F').click()
                print('gender female')
                break
            except WebDriverException:
                sleep(0.25)
        else:
            print('female gender not found')

    sleep(2)
    input_text(browser, 'EditDriverDetailsFormModel_DriverDetail_DateOfBirth_Month', DOBMonth)
    input_text(browser, 'EditDriverDetailsFormModel_DriverDetail_DateOfBirth_Day', DOBDay)
    input_text(browser, 'EditDriverDetailsFormModel_DriverDetail_DateOfBirth_Year', DOBYear)

    sleep(2)
    select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_MaritalStatus_Value', martial_status)

    sleep(2)
    select_dropdown(browser, 'EditDriverDetailsFormModel_DriverDetail_Relationship_Value', relationship_to_driver_one)

    sleep(2)
    select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_LicenseStatus_Value', license_status - 1)
    # There is no blank option

    sleep(3)
    input_text(browser, 'EditPniDetailsFormModel_DriverDetail_DriverAgeLicensed_Value', age_licensed)

    # Just in case
    click_yes_or_no(browser, license_three_years, 'EditPniDetailsFormModel_DriverDetail_DriverLicenseSuspended_Value_Y',
                    'EditPniDetailsFormModel_DriverDetail_DriverLicenseSuspended_Value_N')

    sleep(3)
    if click_yes_or_no(browser, license_three_years,
                       'EditPniDetailsFormModel_DriverDetail_DriverLicenseSuspended_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_DriverLicenseSuspended_Value_N') == 'yes':
        license_gone = 'y'
        input_text(browser, 'EditPniDetailsFormModel_DriverDetail_ReinstatementDate_Month', reinstate_month)
        input_text(browser, 'EditPniDetailsFormModel_DriverDetail_ReinstatementDate_Day', reinstate_day)
        input_text(browser, 'EditPniDetailsFormModel_DriverDetail_ReinstatementDate_Year', reinstate_year)

    sleep(2)
    if click_yes_or_no(browser, license_outside_US, 'EditPniDetailsFormModel_DriverDetail_DriverLicenseNonUS_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_DriverLicenseNonUS_Value_N') == 'yes':
        input_text(browser, 'EditPniDetailsFormModel_DriverDetail_DriverAgeLicensedNonUS_Value',
                   age_licensed_outside_US)
        try:
            print(license_gone, '\nThis is a test.')
            del license_gone
        except NameError:
            print('license not bad in past 3 years.')
            click_yes_or_no(browser, valid_eighteen_months,
                            'EditPniDetailsFormModel_DriverDetail_DriverLicense18Month_Value_Y',
                            'EditPniDetailsFormModel_DriverDetail_DriverLicense18Month_Value_N')

    sleep(2)
    if click_yes_or_no(browser, damages_to_car, 'EditPniDetailsFormModel_DriverDetail_HasAccidentsOrClaims_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_HasAccidentsOrClaims_Value_N') == 'yes':
        print('yes damages')
        select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_AccidentClaimList_0_DescribeAccidentClaim_Value',
                        unfinished)
        select_dropdown(browser,
                        'EditPniDetailsFormModel_DriverDetail_AccidentClaimList_0_AccidentClaimTimeframe_Value',
                        unfinished)
    sleep(2)
    if click_yes_or_no(browser, DWI, 'EditPniDetailsFormModel_DriverDetail_HasDwiViolations_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_HasDwiViolations_Value_N') == 'yes':
        print('yes driving like randy')
        input_text(browser, unfinished, 'EditPniDetailsFormModel_DriverDetail_DwiViolationList_0_ViolationDate_Month')
        input_text(browser, unfinished, 'EditPniDetailsFormModel_DriverDetail_DwiViolationList_0_ViolationDate_Day')
        input_text(browser, unfinished * 1013,
                   'EditPniDetailsFormModel_DriverDetail_DwiViolationList_0_ViolationDate_Year')

    sleep(2)
    if click_yes_or_no(browser, tickets, 'EditPniDetailsFormModel_DriverDetail_HasTicketsOrViolations_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_HasTicketsOrViolations_Value_N') == 'yes':
        print('yes tickets')
        select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_TicketViolationList_0_TicketOrViolation_Value',
                        unfinished)

    click_next_button(browser)

    sleep(2)
    while driver_course_exception < 10:
        try:
            browser.find_element_by_id('EditDriverAdditionalDetailsFormModel_SeniorDriver_Value_N')
            click_yes_or_no(browser, driver_improvement_course,
                            'EditDriverAdditionalDetailsFormModel_SeniorDriver_Value_Y',
                            'EditDriverAdditionalDetailsFormModel_SeniorDriver_Value_N')
            break
        except NoSuchElementException:
            driver_course_exception += 1
            pass


def final_detail_page(browser, driver_dict):
    education = driver_dict['education']
    work = driver_dict['work']
    # job = driver_dict['job']
    residence = driver_dict['residence']
    driver_improvement_course = driver_dict['driverImprovementCourse']
    gender = driver_dict['gender']
    martial_status = driver_dict['martialStatus']
    license_status = driver_dict['licenseStatus']
    age_licensed = driver_dict['ageLicensed']
    license_three_years = driver_dict['licenseBadThree']
    reinstate_month = driver_dict['licenseReinstatedMonth']
    reinstate_day = driver_dict['licenseReinstatedDay']
    reinstate_year = driver_dict['licenseReinstatedYear']
    license_outside_US = driver_dict['licenseOutsideUS']
    age_licensed_outside_US = driver_dict['ageLicenseOutUS']
    valid_eighteen_months = driver_dict['validEighteenMonths']
    damages_to_car = driver_dict['damagesToCar']
    if damages_to_car.lower().strip() == 'y':
        damage_cause = driver_dict['']
        damage_time = driver_dict['']
    DWI = driver_dict['DWI']
    if DWI.lower().strip() == 'y':
        DWI_Month = driver_dict['DWIMonth']
        DWI_Day = driver_dict['DWIDay']
        DWI_Year = driver_dict['DWIYear']
    tickets = driver_dict['tickets']

    gender_exception = 0
    driver_course_exception = 0
    license_status -= 1
    sleep(3)
    if gender.strip().lower() == 'm':
        while gender_exception < 20:
            try:
                browser.find_element_by_id('EditPniDetailsFormModel_DriverDetail_Gender_Value_M').click()
                print('gender male')
                break
            except WebDriverException:
                gender_exception += 1
                sleep(0.25)
        else:
            print('male gender not found')
    elif gender.strip().lower() == 'f':
        while gender_exception < 20:
            try:
                browser.find_element_by_id('EditPniDetailsFormModel_DriverDetail_Gender_Value_F').click()
                print('gender female')
                break
            except WebDriverException:
                gender_exception += 1
                sleep(0.25)
        else:
            print('female gender not found')

    sleep(2)
    select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_MaritalStatus_Value', martial_status)

    sleep(2)
    select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_HighestLevelOfEducation_Value', education)

    sleep(2)
    select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_EmploymentStatus_Value', work)

    # WIP
    if work == 1:
        sleep(1)
        input('Are you done with the input for work?\n'
              '----------------------------------------\n'
              '========================================\n'
              '<><><><><><><><><><><><><><><><><><><><>\n'
              '::::::::::::::::::::::::::::::::::::::::\n'
              '({[]})({[]})({[]})({[]})({[]})({[]})({[]})')

    sleep(2)
    select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_PrimaryResidence_Value', residence)

    sleep(2)
    select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_LicenseStatus_Value', license_status)
    # There is no blank option

    sleep(3)
    input_text(browser, 'EditPniDetailsFormModel_DriverDetail_DriverAgeLicensed_Value', age_licensed)

    # Just in case
    click_yes_or_no(browser, license_three_years, 'EditPniDetailsFormModel_DriverDetail_DriverLicenseSuspended_Value_Y',
                    'EditPniDetailsFormModel_DriverDetail_DriverLicenseSuspended_Value_N')

    sleep(3)
    if click_yes_or_no(browser, license_three_years,
                       'EditPniDetailsFormModel_DriverDetail_DriverLicenseSuspended_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_DriverLicenseSuspended_Value_N') == 'yes':
        license_gone = 'y'
        input_text(browser, 'EditPniDetailsFormModel_DriverDetail_ReinstatementDate_Month', reinstate_month)
        input_text(browser, 'EditPniDetailsFormModel_DriverDetail_ReinstatementDate_Day', reinstate_day)
        input_text(browser, 'EditPniDetailsFormModel_DriverDetail_ReinstatementDate_Year', reinstate_year)

    sleep(2)
    if click_yes_or_no(browser, license_outside_US, 'EditPniDetailsFormModel_DriverDetail_DriverLicenseNonUS_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_DriverLicenseNonUS_Value_N') == 'yes':
        input_text(browser, 'EditPniDetailsFormModel_DriverDetail_DriverAgeLicensedNonUS_Value',
                   age_licensed_outside_US)
        try:
            print(license_gone, '\nThis is a test.')
            del license_gone
        except NameError:
            print('license not bad in past 3 years.')
            click_yes_or_no(browser, valid_eighteen_months,
                            'EditPniDetailsFormModel_DriverDetail_DriverLicense18Month_Value_Y',
                            'EditPniDetailsFormModel_DriverDetail_DriverLicense18Month_Value_N')

    sleep(2)
    if click_yes_or_no(browser, damages_to_car, 'EditPniDetailsFormModel_DriverDetail_HasAccidentsOrClaims_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_HasAccidentsOrClaims_Value_N') == 'yes':
        print('yes damages')
        select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_AccidentClaimList_0_DescribeAccidentClaim_Value',
                        unfinished)
        select_dropdown(browser,
                        'EditPniDetailsFormModel_DriverDetail_AccidentClaimList_0_AccidentClaimTimeframe_Value',
                        unfinished)
    sleep(2)
    if click_yes_or_no(browser, DWI, 'EditPniDetailsFormModel_DriverDetail_HasDwiViolations_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_HasDwiViolations_Value_N') == 'yes':
        print('yes driving like randy')
        input_text(browser, DWI_Month, 'EditPniDetailsFormModel_DriverDetail_DwiViolationList_0_ViolationDate_Month')
        input_text(browser, DWI_Day, 'EditPniDetailsFormModel_DriverDetail_DwiViolationList_0_ViolationDate_Day')
        input_text(browser, DWI_Year, 'EditPniDetailsFormModel_DriverDetail_DwiViolationList_0_ViolationDate_Year')

    sleep(2)
    if click_yes_or_no(browser, tickets, 'EditPniDetailsFormModel_DriverDetail_HasTicketsOrViolations_Value_Y',
                       'EditPniDetailsFormModel_DriverDetail_HasTicketsOrViolations_Value_N') == 'yes':
        print('yes tickets')
        select_dropdown(browser, 'EditPniDetailsFormModel_DriverDetail_TicketViolationList_0_TicketOrViolation_Value',
                        23)

    sleep(2)
    while driver_course_exception < 10:
        try:
            browser.find_element_by_id('EditDriverAdditionalDetailsFormModel_SeniorDriver_Value_N')
            click_yes_or_no(browser, driver_improvement_course,
                            'EditDriverAdditionalDetailsFormModel_SeniorDriver_Value_Y',
                            'EditDriverAdditionalDetailsFormModel_SeniorDriver_Value_N')
            break
        except NoSuchElementException:
            driver_course_exception += 1
            pass
    click_next_button(browser)


def verify_page(browser, driver_dict):
    continued_three_years = driver_dict['continuedThreeYears']
    email = driver_dict['email']
    non_auto_progressive = driver_dict['nonAutoProgressive']
    bodily_injury_limits = driver_dict['bodilyInjuryLimits']
    sleep(5)
    try:
        browser.find_element_by_xpath("//*[contains(text(), 'Can you review & verify your personal information?')]")
        print('verifying page')
        click_next_button(browser)
    except NoSuchElementException:
        pass

    sleep(2)
    click_yes_or_no(browser, non_auto_progressive, 'FinalDetailsFormModel_OtherPolicies_Value_Y',
                    'FinalDetailsFormModel_OtherPolicies_Value_N')

    click_yes_or_no(browser, continued_three_years, 'FinalDetailsFormModel_ContinuousInsuranceThreeYears_Value_Y',
                    'FinalDetailsFormModel_ContinuousInsuranceThreeYears_Value_Y')

    sleep(2)
    select_dropdown(browser, 'FinalDetailsFormModel_BodilyInjuryLimits_Value', bodily_injury_limits)

    sleep(2)
    browser.find_element_by_id('FinalDetailsFormModel_PrimaryEmailAddress_Value').send_keys(email)
    print('email typed')


def change_price(browser, label_id, edit_id, variable):
    sleep(3)
    exception = 0
    while exception < 10:
        try:
            text = browser.find_element_by_id(label_id).get_attribute('textContent')
            break
        except NoSuchElementException:
            sleep(0.25)
            exception += 1
        except NoSuchAttributeException:
            print(':) :) :)')
    exception = 0
    print(text)
    print(variable)
    if text != variable:
        browser.find_element_by_id(edit_id).click()
        sleep(5)
        while exception < 10:
            try:
                browser.find_element_by_xpath("//*[contains(text(),'" + variable + "')]/preceding::input[1]").click()
                break
            except ElementNotVisibleException:
                sleep(0.25)
                exception += 1

        click_next_button(browser)


def edit_quote(browser, quote_dict):
    BI_PD = quote_dict['BI_PD']
    uninsuredMotoristBI = quote_dict['uninsuredMotoristBI']
    medical = quote_dict['medicalPayments']
    comprehensive = quote_dict['comprehensive']
    collision = quote_dict['collision']
    collDeductible_Waiver = quote_dict['collisionDeductibleWaiver']
    uninsuredMotoristPD = quote_dict['uninsuredMotoristPD']
    rental = quote_dict['rental']
    roadside = quote_dict['roadside']

    change_price(browser, 'BIPD0-lcl', 'BIPD0-button', BI_PD)
    change_price(browser, 'UMUIM1-lcl', 'UMUIM1-button', )
    change_price(browser, 'COMP0-lcl', 'COMP0-button', comprehensive)
    change_price(browser, 'COLL1-lcl', 'COLL1-button', collision)
    change_price(browser, 'CDW2-lcl', 'CDW2-button', collDeductible_Waiver)
    change_price(browser, 'UMPD3-lcl', 'UMPD3-button', uninsuredMotoristPD)
    change_price(browser, 'RENT4-lcl', 'RENT4-button', rental)
    change_price(browser, 'ROADSD5-lcl', 'ROADSD5-button', roadside)
