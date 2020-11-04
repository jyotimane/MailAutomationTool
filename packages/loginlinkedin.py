import time


def LoginWithLinkedIn(request, driver):
    driver.get('https://www.linkedin.com/uas/login')

    username = "amey@exponential-x.com"
    password = "ameykulkarni"

    elementID = driver.find_element_by_xpath('//*[@id="username"]')
    elementID.send_keys(username)

    elementID = driver.find_element_by_xpath('//*[@id="password"]')
    elementID.send_keys(password)
    elementID.submit()
    time.sleep(6)
    request.session["username"] = username
