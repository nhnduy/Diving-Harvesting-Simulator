import random
#Create a function for the simulator app
def simulator_app():
  #Create a list of income, start year from 1, set manager's years = 0
  income_by_years = []
  repeat = True
  count_year = 1
  count_manager_years = 0
  minimum_total_profit = 0
  maximum_total_profit = 325000

  while repeat:
    print("** Year", count_year, "**")
    income = 0
    #Random the chance from 1% - 100%
    chance = random.randrange(1, 101)

    #Years of Lobsters will be 1, 5, 9, 13,..., these numbers mod 4 = 1
    if count_year % 4 == 1:
      print("Focus this year: Lobsters")
      #There are 3 levels of chances for Lobsters
      if 1 <= chance <= 10:
        income = 125000
      elif 11 <= chance <= 70:
        income = 50000
      elif 71 <= chance <= 100:
        income = -10000

    #Years of Bullwhip Kelp will be 2, 4, 6, 8..., these numbers mod 2 = 0
    if count_year % 2 == 0 and count_year > 0:
      print("Focus this year: Bullwhip Kelp")
      #There are 2 levels of chances for Bullwhip Kelp
      if 1 <= chance <= 60:
        income = 45000
      elif 61 <= chance <= 100:
        income = -10000

    #Years of Urchins will be 3, 7, 11, 15, 19,..., these numbers mod 4 = 3
    if count_year % 4 == 3:
      print("Focus this year: Urchins")
      #There are 2 levels of chances for Urchins
      if 1 <= chance <= 75:
        income = 30000
      elif 76 <= chance <= 100:
        income = -5000

    #Increase the year by 1 each loop
    count_year += 1
    #append income to the income list and sum it
    income_by_years.append(income)
    total_income_by_years = sum(income_by_years)
    print(f"This year's profit (or loss): ${income}")
    print(f"Total profit (or loss): ${total_income_by_years}")
    #If income > 0, we have profit that year, the manager's good year increases by 1
    if income > 0:
      count_manager_years += 1
    else:
      count_manager_years = 0

    #Check the cases
    if total_income_by_years < minimum_total_profit:
      print("The owner will close the fishing operation and look for a new business venture.")
      repeat = False
    if total_income_by_years >= maximum_total_profit:
      print("The total profit reaches at least $325,000 at year-end. The owner will happily retire.")
      repeat = False
    if count_manager_years == 5: #-->stop because the manager had 5 consecutive good years
      print("There are five consecutive years of positive profit. The manager will happily retire.")
      repeat = False
  return


app_status = True
#Call the function to run the simulator
simulator_app()
#Set the prompt to ask user to repeat
while app_status:
  prompt = input("Would you like to repeat (yes/no)? ")
  if prompt.lower().strip() == "yes":
    simulator_app()
  else:
    app_status = False
    print("End")