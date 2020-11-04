import time
from bs4 import BeautifulSoup

name_info, loc_info, desg_info, namedemo_info, fname, lname, location, designation, compName = ([
] for i in range(9))


def ScrapData(request, driver):
    for i in range(3):
        SCROLL_PAUSE_TIME = 5

        # Get scroll height
        last_height = driver.execute_script(
            "return document.body.scrollHeight")

        for i in range(3):
            # Scroll down to bottom
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        driver.find_element_by_css_selector('[aria-label="Next"]').click()
        src = driver.page_source
        soup = BeautifulSoup(src, 'lxml')

    #     name = soup.find_all('span',{'name actor-name'})
        namedemo = soup.find_all('span', {'actor-name'})
        desg = soup.find_all(
            'p', {'subline-level-1 t-14 t-black t-normal search-result__truncate'})
        loc = soup.find_all(
            'p', {'subline-level-2 t-12 t-black--light t-normal search-result__truncate'})

        #print(len(namedemo), len(desg), len(loc))
        for i in range(len(namedemo)):
            namedemo_info.append(namedemo[i].get_text().strip())
            desg_info.append(desg[i].get_text().strip())
            loc_info.append(loc[i].get_text().strip())
        time.sleep(2)

    #     for i in namedemo:
    #         namedemo_info.append(i.get_text().strip())
    #     for i in desg:
    #         desg_info.append(i.get_text().strip())
    #     for i in loc:
    #         loc_info.append(i.get_text().strip())
    #     time.sleep(3)

    # for i in range(len(namedemo_info)):
    #     if namedemo_info[i] != 'LinkedIn Member':
    #         name.append(namedemo_info[i])
    #         location.append(loc_info[i])
    #         compDesg.append(desg_info[i])

    # for i in compDesg:
    for i in range(len(namedemo_info)):
        if namedemo_info[i] != 'LinkedIn Member':
            if " at " in desg_info[i]:
                temp = desg_info[i].split(" at ")
                designation.append(temp[0])
                compName.append(temp[1].strip())
    #             name.append(namedemo_info[i])
                fname.append(namedemo_info[i].split()[0])
                lname.append(namedemo_info[i].split()[-1])
                location.append(loc_info[i])
            elif "," in desg_info[i]:
                temp = desg_info[i].split(",")
                if "@" in temp[0]:
                    temp = temp[0].split("@")
                    designation.append(temp[0])
                    compName.append(temp[1].strip())
                    fname.append(namedemo_info[i].split()[0])
                    lname.append(namedemo_info[i].split()[-1])
                    location.append(loc_info[i])
                else:
                    designation.append(temp[0])
                    compName.append(temp[1].strip())
                    fname.append(namedemo_info[i].split()[0])
                    lname.append(namedemo_info[i].split()[-1])
                    location.append(loc_info[i])
            elif "@" in desg_info[i]:
                temp = desg_info[i].split("@")
                designation.append(temp[0])
                compName.append(temp[1].strip())
                fname.append(namedemo_info[i].split()[0])
                lname.append(namedemo_info[i].split()[-1])
                location.append(loc_info[i])
            elif "-" in desg_info[i]:
                temp = desg_info[i].split("-")
                designation.append(temp[0])
                compName.append(temp[1].strip())
                fname.append(namedemo_info[i].split()[0])
                lname.append(namedemo_info[i].split()[-1])
                location.append(loc_info[i])
            elif "=" in desg_info[i]:
                temp = desg_info[i].split("=")
                designation.append(temp[0])
                compName.append(temp[1].strip())
                fname.append(namedemo_info[i].split()[0])
                lname.append(namedemo_info[i].split()[-1])
                location.append(loc_info[i])
        #     if " and " in i:
        #         temp = i.split(" and ")
        #         designation.append(temp[0])
        #         compName.append(temp[1])
        #         continue
        #     if " or " in i:
        #         temp = i.split(" or")
        #         designation.append(temp[0])
        #         compName.append(temp[1])
        #         continue
            elif " of " in desg_info[i]:
                temp = desg_info[i].split(" of ")
                designation.append(temp[0])
                compName.append(temp[1].strip())
                fname.append(namedemo_info[i].split()[0])
                lname.append(namedemo_info[i].split()[-1])
                location.append(loc_info[i])
        #     else:
        #         designation.append(i)

    
    request.session['ccl_data'] = {'fname': fname, 'lname': lname, 'location': location,
                                   'designation': designation, 'compName': compName}
    # return request.session['ccl_data']
