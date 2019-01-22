import time
time.sleep(1)
print"				 THE FLIGHT AUTOMATER"
time.sleep(1)
print"                  WELCOME TO THE AUTOMATED FLIGHT PRICE CHECKER"
time.sleep(2)
print"                      PLEASE UPLOAD YOUR TRAVEL DETAILS"
time.sleep(1)
print"                        AND GET THE CHEAPEST FLIGHTS" 
time.sleep(2)
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#          TRAVEL DETAILS

origin=raw_input("Enter place of Origin: ")
destination=raw_input("Enter place of destination: ")
type=raw_input("Enter one way or round trip: ")
people=raw_input("Enter number of people flying: ")

#         ONE WAY

if type=="one way":
	time.sleep(1)
        departure=raw_input("Enter day of departure(dd/mm/yyyy): ")
        time.sleep(1)
        time_period=raw_input("Enter the time of day for departure(Morning,Afternoon,Evening,Night),if any, else type no: ")
        time.sleep(1)
        amazon=raw_input("Enter yes if you have amazon pay and no if not: ")
        time.sleep(1)

#				CLEARTRIP(ONE WAY)

#       CLEARTRIP FRONT PAGE	

	driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver.get("https://cleartrip.com")   #Loading the cleartrip website
        time.sleep(8)
        searchct1=driver.find_element_by_id("FromTag") #Origin of flight
	searchct1.click()
	time.sleep(1)
        searchct1.send_keys(origin)
        time.sleep(1)
        searchct2=driver.find_element_by_id("ToTag")  #Destination of flight
	searchct2.click()
	time.sleep(1)
        searchct2.send_keys(destination)
        searchct3=driver.find_element_by_id("DepartDate") #Departing of flight
	searchct3.click()
	time.sleep(1)
        searchct3.send_keys(departure)
        time.sleep(1)
        searchct4=driver.find_element_by_id("Adults")  #Number of person travelling
        searchct4.send_keys(people)
        time.sleep(1)
        driver.find_element_by_id("SearchBtn").click() #Searching for flight 
        driver.maximize_window()
        time.sleep(18)
	
	
#       CLEARTRIP FLIGHT DISPLAY PAGE

#	CHECKING FOR TIME OF FLIGHT IN THE DAY

	if time_period=="Night" or time_period=="night":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[1]/label").click()
                time.sleep(1)
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[5]/label").click()
        elif time_period=="Afternoon" or time_period=="afternoon":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[3]/label/span").click()
        elif time_period=="Morning" or time_period=="morning":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[2]/label").click()
        elif time_period=="Evening" or time_period=="evening":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[2]/label").click()
        time.sleep(1)

	driver.find_element_by_xpath("//*[@id='flightForm']/section[2]/div[4]/div/nav/ul/li[1]/table/tbody[2]/tr[2]/td[3]/button").click()  #Searching for flight fare
	time.sleep(1)

#	APPLYING COUPON
	
	driver.find_element_by_id("insurance_box").click()
        time.sleep(1)
	searchct5=driver.find_element_by_id("coupon")
        searchct5.send_keys("TRVLNOW")	#Applying coupon
        time.sleep(1)
        driver.find_element_by_id("check_saving").click()
        time.sleep(4)


#				GOIBIBO(ONE WAY)

	driver2=webdriver.Chrome(executable_path=r"./chromedriver")
        driver2.get("https://www.goibibo.com/")  #Loading the goibibo site
        driver2.maximize_window()

#	TRAVEL DETAILS 

	time.sleep(1)
        searchgo1=driver2.find_element_by_id("gosuggest_inputSrc")
        searchgo1.send_keys(origin) #Origin input
        time.sleep(1)
        searchgo2=driver2.find_element_by_id("gosuggest_inputDest")
        searchgo2.send_keys(destination) #Destination input
        time.sleep(1)

	
	driver2.find_element_by_xpath("//*[@id='searchWidgetCommon']/div/div[3]/div[1]/div[1]/div").click()
        month=int(departure[3]+departure[4])
        for i in range(month-1):
                driver2.find_element_by_css_selector("span.DayPicker-NavButton--next").click()
        time.sleep(1)
        s1="fare_2019"                          #Checking for date of departure
        s1+=departure[3]+departure[4]
        s1+=departure[0]+departure[1]
        driver2.find_element_by_id(s1).click()
        time.sleep(1)

	driver2.find_element_by_id("pax_label").click()
        for i in range(1,int(people)):
                driver2.find_element_by_id("adultPaxPlus").click() #Checking for no.of adults
        time.sleep(1)
        driver2.find_element_by_id("pax_close").click()
        time.sleep(1)
        driver2.find_element_by_id("gi_search_btn").click() #Searching for flights
        time.sleep(10)

	#LOADING FLIGHTS 

	s = driver2.find_elements_by_css_selector("i.icon-arrow-down.fl.downArrFilter")
        s=s[0]
        s.click()
        time.sleep(1)   #Checking for time of flight in the day 
        if time_period=="afternoon" or time_period=="Afternoon":
                driver2.find_element_by_id("onw_11-5").click()
        elif time_period=="morning" or time_period=="Morning":
                driver2.find_element_by_id("onw_before11").click()
        elif time_period=="evening" or time_period=="Evening":
                driver2.find_element_by_id("onw_5-9").click()
        elif time_period=="night" or time_period=="Night":
                driver2.find_element_by_id("onw_after9").click()

#	Searching for flights
	

	time.sleep(2)
        driver2.find_element_by_css_selector("input.fr").click()#Going to fare page
        time.sleep(3)

#	Applying Coupon
        
#       searchgo3=driver2.find_element_by_id("goPromo")
#       searchgo3.send_keys("WINTER")
#       time.sleep(1)
#       driver2.find_element_by_id("gi_search_promo").click()
#       time.sleep(1)
#       driver2.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[3]/div[1]").click()
	
#	Amazon Pay
	
	if amazon=="yes":
		print "You get an additional discount of upto Rupees 600 on GOIBIBO"

#				ROUND TRIP					

else:

#			       TRAVEL DETAILS	
	
	time.sleep(1)
        departure=raw_input("Enter day of departure(dd/mm/yyyy): ")
        time.sleep(1)
        arrival=raw_input("Enter day of arrival(dd/mm/yyyy): ")
        time.sleep(1)
        time_period1=raw_input("Enter the time of day for departure(Morning,Afternoon,Evening,Night),if any else no: ")
        time_period2=raw_input("Enter the time of day for arrival(Morning,Afternoon,Evening,Night),if any else no: ")
        amazon=raw_input("Enter yes if you have amazon pay and no if not: ")

#				CLEARTRIP	

#			 CLEARTRIP(ROUND TRIP)

	driver=webdriver.Chrome(executable_path=r"./chromedriver")
        driver.get("https://cleartrip.com") #Loading cleartrip 
        driver.find_element_by_id("RoundTrip").click()
        time.sleep(8)

#			LOADING DETAILS ON FRONT PAGE

	search1=driver.find_element_by_id("FromTag")
	search1.click()
	time.sleep(1)
        search1.send_keys(origin) #Origin 
        time.sleep(1)
        search2=driver.find_element_by_id("ToTag")
	search2.click()
	time.sleep(1)
        search2.send_keys(destination) #Destination
        time.sleep(1)
        search3=driver.find_element_by_id("DepartDate")
	search3.click()
	time.sleep(1)
        search3.send_keys(departure) #Depart date
        time.sleep(1)
        search4=driver.find_element_by_id("ReturnDate")
	search4.click()
	time.sleep(1)
        search4.send_keys(arrival)  #Arrival date
        time.sleep(1)
        search5=driver.find_element_by_id("Adults")
        search5.send_keys(people)  #Number of people
        time.sleep(1)
        driver.find_element_by_id("SearchBtn").click() #Searching for flights
        driver.maximize_window()
        time.sleep(25)

#			CHECKING FOR THE TIME OF FLIGHT IN THE DAY
	
	if time_period1=="Night" or time_period1=="night":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[1]/label").click()
                time.sleep(1)
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[5]/label").click()
        elif time_period1=="Afternoon" or time_period1=="afternoon":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[3]/label/span").click()
        elif time_period1=="Morning" or time_period1=="morning":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[2]/label").click()
        elif time_period1=="Evening" or time_period1=="evening":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[2]/label").click()
        time.sleep(1)


        if time_period2=="Night" or time_period2=="night":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[6]/div/nav/ul/li[1]/label").click()
                time.sleep(1)
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[6]/div/nav/ul/li[5]/label").click()
        elif time_period2=="Afternoon" or time_period2=="afternoon":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[6]/div/nav/ul/li[3]/label").click()
        elif time_period2=="Morning" or time_period2=="morning":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[5]/div/nav/ul/li[2]/label").click()
        elif time_period2=="Evening" or time_period2=="evening":
                driver.find_element_by_xpath("//*[@id='ResultContainer_1_1']/section[2]/section/aside[1]/div/div[1]/form/div/div[6]/div/nav/ul/li[4]/label").click()
	time.sleep(1)

	x=driver.find_elements_by_xpath("//*[@id='flightForm']/section[2]/div[3]/div[3]/button")
        x=x[-1]
        x.click()  #Checking for flight fare
        time.sleep(1)  

#	APPLYING COUPON

        driver.find_element_by_id("insurance_box").click()
        time.sleep(1)	
	search5=driver.find_element_by_id("coupon")
        search5.send_keys("TRVLNOW")  
        time.sleep(1)
        driver.find_element_by_id("check_saving").click()
	time.sleep(4)

#		         GOIBIBO(ROUND TRIP)

	driver2=webdriver.Chrome(executable_path=r"./chromedriver")
        driver2.get("https://www.goibibo.com/") #Loading Goibibo website
        driver2.maximize_window()
	time.sleep(1)

#			TRAVEL DETAILS

	driver2.find_element_by_id("gi_roundtrip_label").click()
        time.sleep(1)
        searchgo1=driver2.find_element_by_id("gosuggest_inputSrc")
        searchgo1.send_keys(origin)#Origin 
        time.sleep(1)
        searchgo2=driver2.find_element_by_id("gosuggest_inputDest")
        searchgo2.send_keys(destination)#Destination
        time.sleep(1)
	
#		       SELECTING TRAVEL DETAILS
	driver2.find_element_by_xpath("//*[@id='searchWidgetCommon']/div/div[3]/div[1]/div[1]/div").click()
        month=int(departure[3]+departure[4])
        for i in range(month-1):
                driver2.find_element_by_css_selector("span.DayPicker-NavButton--next").click()

	time.sleep(1)
        s1="fare_2019"
        s1+=departure[3]+departure[4]
        s1+=departure[0]+departure[1]
        driver2.find_element_by_id(s1).click()
        time.sleep(1)

        month1=int(arrival[3]+arrival[4])
        for i in range(month1-month):
                driver2.find_element_by_css_selector("span.DayPicker-NavButton--next").click()
        time.sleep(1)
        s2="fare_2019"
        s2+=arrival[3]+arrival[4]
        s2+=arrival[0]+arrival[1]
        driver2.find_element_by_id(s2).click()
        time.sleep(1)

	driver2.find_element_by_id("pax_label").click()
        for i in range(1,int(people)):# Selecting the number of people
                driver2.find_element_by_id("adultPaxPlus").click()
        time.sleep(1)
        driver2.find_element_by_id("pax_close").click()
        time.sleep(1)
        driver2.find_element_by_id("gi_search_btn").click() #Searching for flights
        time.sleep(10)


# 		ENTERING INTO THE FLIGHT DETAILS PAGE

	s = driver2.find_elements_by_css_selector("i.icon-arrow-down.fl.downArrFilter")
        s=s[0]
        s.click()
        time.sleep(1)

        if time_period1=="afternoon" or time_period1=="Afternoon":
                driver2.find_element_by_id("onw_11-5").click()
        elif time_period1=="morning" or time_period1=="Morning":
                driver2.find_element_by_id("onw_before11").click()
        elif time_period1=="evening" or time_period1=="Evening":
                driver2.find_element_by_id("onw_5-9").click()
        elif time_period1=="night" or time_period1=="Night":
                driver2.find_element_by_id("onw_after9").click()

        if time_period2=="afternoon" or time_period2=="Afternoon":
                driver2.find_element_by_id("ret_11-5").click()
        elif time_period2=="morning" or time_period2=="Morning":
                driver2.find_element_by_id("ret_before11").click()
        elif time_period2=="evening" or time_period2=="Evening":
                driver2.find_element_by_id("ret_5-9").click()
        elif time_period2=="night" or time_period2=="Night":
                driver2.find_element_by_id("ret_after9").click()

        time.sleep(3)
	
	driver2.find_element_by_css_selector("input.fr").click()#Going into the fare page
        time.sleep(2)

#	Applying Coupon

#       searchgo3=driver2.find_element_by_id("goPromo")
#       searchgo3.send_keys("WINTER")
#       time.sleep(1)
#       driver2.find_element_by_id("gi_search_promo").click()
#       time.sleep(1)
#       driver2.find_element_by_xpath("//*[@id='content']/div/div[2]/div/div[3]/div[2]/div/div/div[2]/button").click()

#	AMAZON PAY
	
	if amazon=="yes":
		print "You get an additional discount of upto Rupees 600 on GOIBIBO"	

time.sleep(50)
driver2.close()
driver.close()






				 
