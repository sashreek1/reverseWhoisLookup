from selenium import webdriver
inp = input('please enter the name of a person or company that you want to lookup : ')
print("\n\n")
driver = webdriver.Firefox()
driver.get("https://viewdns.info/reversewhois/?q="+inp)
driver.minimize_window()
i =1
try:
    while True:
        for j in range(1,4):
            element = driver.find_element_by_xpath("/html/body/font/table[2]/tbody/tr[3]/td/font/table/tbody/tr["+str(i)+"]/td["+str(j)+"]")
            print(element.text,end="\t\t")
        print("\n")
        print("="*70)
        print()
        i+=1
except:
    driver.close()
    driver.quit()