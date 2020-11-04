import MailboxValidator
import csv
import pandas as pd


fstname = []
lstname = []
desig = []
compname = []
loc = []
valid_mail = []
domains = []


def multiple_validation_module(request):
    # MailboxValidator Api Key.
    mbv = MailboxValidator.SingleValidation('H3PW040UPFOLWZ79U312')

    # Read data in our generated lead.
    reader = csv.DictReader(open("D://Exponential-X//foremail_mail.csv"))

    for raw in reader:
        mails = []
        fname = (raw['First Name']).lower()
        lname = (raw['Last Name']).lower()
        domain = raw['Domain']

        fstname.append(fname)
        lstname.append(lname)
        desig.append(raw['Designation'])
        compname.append(raw['Company Name'])
        loc.append(raw['Location'])
        domains.append(domain)

        # Mail Combinations
        mails.append(fname+'@'+domain)
        mails.append(lname+fname+'@'+domain)

        flag = "True"
        tmp = []
        for mail in mails:
            # Validate generated mails and Domains.
            results = mbv.ValidateEmail(mail)
            if results is None:
                print("Error connecting to API.\n")
            elif results['error_code'] == '':
                print('email_address = ', results['email_address'])
                print('domain = ', results['domain'])
                print('is_domain = ', results['is_domain'])
                print('is_verified = ', results['is_verified'])
                print('is_server_down = ', results['is_server_down'] + "\n")

                if results['is_verified'] == "True":
                    #                 cur.execute("insert into email_table(FirstName,LastName,Designation,CompanyName,Location,Domain,ValidMails) values(%s,%s,%s,%s,%s,%s,%s)",(raw['First Name'],raw['Last Name'],raw['Designation'],raw['Company Name'],raw['Location'],raw['Domain'],mail))
                    tmp.append(mail)   # Append Only verified mails
                    flag = "False"
            else:
                print('error_code = ', results['error_code'])
                print('error_message = ', results['error_message'] + "\n")
    #         con.commit()

        if len(tmp) == 0:
            # If valid mail not found then append space
            valid_mail.append(" ")
        else:
            valid_mail.append(tmp)
    # con.close()
    print(valid_mail)
    print("\n")
    request.session['valid_mail'] = valid_mail
