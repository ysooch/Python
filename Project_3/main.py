######################################################

# Project: <Project 3 - Yeonsoo Chang>
# UIN: <673272656>
# repl.it URL: <https://replit.com/@CS111-Fall2021/Project-3-ychan57#main.py>

# For this project, I received help from the following members of CS111.
# TA : help with get_state_population
# Taehyung Kim, netID (I don't know his net ID): I received help with lab 13 "get_data" function and I used lab 13's code for project 3.

######################################################

"""import"""

import csv, json, requests # to open the data file
import matplotlib.pyplot as plt # for visualization
import operator # to sort the data to make descending bar graph
import os # to rename the answer text file



"""make def function"""

def get_data_from_file(fn, format=""):
  csv_data = []

  # get data from csv file
  if format == ".csv" or ".csv" in fn:
    file = open(fn)
    reader = csv.reader(file)
    for row in reader:
      csv_data.append(row)

    return (csv_data)

  # get data from json file
  elif format == ".json" or ".json" in fn:

    file = open(fn)
    text = file.read()
    data = json.loads(text)
    return (data)
    # print(json_data)


# get data from internet (I used the lab 13 code and I got helped from Taehyung Kim with the lab 13 code)
def get_data_from_internet(url, format="json"):

  if format == "":
    if (".csv" in url):
      format = "csv"
    else:
      format = "json"

  if format == "json":
    f = requests.get(url)
    data = f.json()
    return data

  if format == "csv":
    csv_data = []
    f = requests.get(url)
    reader = csv.reader(f)
    for row in reader:
      csv_data.append(row)
      return (csv_data)


# if the dct's second value; abbreviation; is same with the state code, get the full name of that state
def get_state_name(state_names, state_code):
  
  for dct in state_names:
    if dct["abbreviation"] == state_code:
      name = dct["name"]

  return name

# I got help from TA
# for the internet data, the dictionary value has dot(.) before the state name, so I remove that dot when I get the state name to get each state's population
def get_state_population(state_populations, state_name):

  for dct in state_populations:
    new_name = '.' + state_name
    if new_name in dct:
      population = int(dct[new_name])

  return population


# I also got this code from my lab 13
def get_index_for_column_label(header_row, column_row):
  for value in header_row:
    if value == column_row:
      return(header_row.index(value))


# I used the given code from the project 3 rubric file to make the answer file
def answer_header(question_number, question_labels):
  ''' returns the header string for each answer'''
  header = "\n"*2
  header += "="*60 + "\n"
  header += "Question " + str(question_number) + "\n"
  header += question_labels[question_number] + "\n"
  header += "="*60 + "\n"
  return header




"""main function"""

def main():

  # Retrieves data from files and internet only one time
  returns_data = get_data_from_file("tax_return_data_2018.csv")
  states = get_data_from_file("states_titlecase.json", "json")
  populations = get_data_from_internet("https://raw.githubusercontent.com/heymrhayes/class_files/main/state_populations_2018.txt")


  # For the answer file, I make the list of the questions
  question_labels = [
   "",
   "average taxable income per return across all groups",
   "average taxable income per return for each agi group",
   "average taxable income (per resident) per state",
   "average taxable income per return across all groups",
   "average taxable income per return for each agi group",
   "average dependents per return for each agi group",
   "percentage of returns with no taxable income per agi group",
   "average taxable income per resident",
   "percentage of returns for each agi_group",
   "percentage of taxable income for each agi_group"
 ]

  # For the answer file, I make the list of each agi group name
  gr_lst = ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6"]


  # For the question3, I made the list of the state code from the tax_return_data_2018.csv file.
  cd_lst = []
  for i in range(len(returns_data)-1):
    code = returns_data[i+1][1]
    cd_lst.append(code)
  num6 = 0
  real_cd_lst = []
  for num6 in range(51): # the total row of tax_return_data is 307 lines, so I divided it by 6 to get the number of state

    real_cd_lst.append(cd_lst[(6*num6)]) # Each state has 6 agi group, so I skipped it every 6 times to get one state code for one state


    


  f_answer = open("answers.txt", "w") # Open the answer file to write the answer



  "-------------------Q1-------------------"
  # average taxable income per return across all group

  f_answer.write(answer_header(1, question_labels))


  sum_A04800 = 0 # the taxable income amount column to use
  sum_N1 = 0 # the total returns count column

  for i in range(len(returns_data)-1):
    sum_N1 += int(returns_data[i+1][4]) # N1 data is in the column 5 (but in cs, column 4)
    sum_A04800 += int(returns_data[i+1][96]) # A04800 data is in the column 97 (but in cs, column 96)
    question1_ans = round((sum_A04800 / sum_N1)*1000)
  
  # print("Average taxable income per return across all group : $", question1_ans)

  f_answer.write("${:8.0f}".format(question1_ans)) # Use the answer format of project 3






  f_answer = open("answers.txt", "a")

  "-------------------Q2-------------------"
  # # average taxable income per return for each agi group

  f_answer.write(answer_header(2, question_labels))

  sum1_A04800 = 0
  sum1_N1 = 0
  sum2_A04800 = 0
  sum2_N1 = 0
  sum3_A04800 = 0
  sum3_N1 = 0
  sum4_A04800 = 0
  sum4_N1 = 0
  sum5_A04800 = 0
  sum5_N1 = 0
  sum6_A04800 = 0
  sum6_N1 = 0
  

  for i in range(len(returns_data)-1): # Make a loop to get the A04800 and N1 data from the tax_return_data_2018.csv file.

    question2_agi_group = int(returns_data[i+1][3]) # agi group number is in the column 4 (in the cs, column 3)

    if question2_agi_group == 1: # When the agi group number is 1

      # Add the data
      sum1_A04800 += int(returns_data[i+1][96])
      sum1_N1 += int(returns_data[i+1][4])
      # Calculate the average taxable income per return for group 1
      question2_1_ans = round((sum1_A04800 / sum1_N1)*1000)

    # Do the same way as agi group 1
    elif question2_agi_group == 2:
      sum2_A04800 += int(returns_data[i+1][96])
      sum2_N1 += int(returns_data[i+1][4])
      question2_2_ans = round((sum2_A04800 / sum2_N1)*1000)
    elif question2_agi_group == 3:
      sum3_A04800 += int(returns_data[i+1][96])
      sum3_N1 += int(returns_data[i+1][4])
      question2_3_ans = round((sum3_A04800 / sum3_N1)*1000)
    elif question2_agi_group == 4:
      sum4_A04800 += int(returns_data[i+1][96])
      sum4_N1 += int(returns_data[i+1][4])
      question2_4_ans = round((sum4_A04800 / sum4_N1)*1000)
    elif question2_agi_group == 5:
      sum5_A04800 += int(returns_data[i+1][96])
      sum5_N1 += int(returns_data[i+1][4])
      question2_5_ans = round((sum5_A04800 / sum5_N1)*1000)
    else:
      sum6_A04800 += int(returns_data[i+1][96])
      sum6_N1 += int(returns_data[i+1][4])
      question2_6_ans = round((sum6_A04800 / sum6_N1)*1000)
 
  f_answer.write("Group 1: ${:8.0f}".format(question2_1_ans) + "\n")
  f_answer.write("Group 2: ${:8.0f}".format(question2_2_ans) + "\n")
  f_answer.write("Group 3: ${:8.0f}".format(question2_3_ans) + "\n")
  f_answer.write("Group 4: ${:8.0f}".format(question2_4_ans) + "\n")
  f_answer.write("Group 5: ${:8.0f}".format(question2_5_ans) + "\n")
  f_answer.write("Group 6: ${:8.0f}".format(question2_6_ans))

    





  f_answer = open("answers.txt", "a")

  "-------------------Q3-------------------"
  # # average taxable income per state

  f_answer.write(answer_header(3, question_labels))

  q3lst1 = []

  for i in range(len(returns_data)-1):
    question3_A04800_data = int(returns_data[i+1][96])
    q3lst1.append(question3_A04800_data) # Make the list of A04800 data

  

  pp_lst = []
  st_lst = []
  for i in populations:
    a = list(i.keys()) # Get the key of the dictionary from internet data
    b = ''.join(a)
    st_lst.append(b[1:]) # Each key data has the dot(.), so I save the data after the dot
  
  for j in st_lst:
    st_name = j
    p = get_state_population(populations, st_name) # Use the get_state_population with the state_name which I got(st_lst)
    pp_lst.append(p) # Make the population list


  question3_ans_lst = []

  # Set the initial value
  x = 0
  y = 6
  a = 0
  income_data3 = 0

  while y < (len(returns_data)+1):
    income_data3 = q3lst1[x:y] # Each state has 6 agi group, so split the data every 6 times
    income_sum = 0
    for i in income_data3:
      income_sum += i
      question3_ans = round((income_sum / pp_lst[a])*1000) # Get the average taxable income per state
      
    # Repeat the calculation 51 times (because 306 / 6 = 51)
    x += 6
    y += 6
    a += 1

  
    question3_ans_lst.append(question3_ans) # Make the answer list
 
  for a in range(len(real_cd_lst)):
      f_answer.write("{} : ${:8.0f}".format(real_cd_lst[a], question3_ans_lst[a]) + "\n")


  

  
  
  f_answer = open("answers.txt", "a")
  
  "-------------------Q4-------------------"
  # What is the average taxable income per return across all groups?

  f_answer.write(answer_header(4, question_labels))

  print("Enter the code : ", end = "") # Make the input function with state code
  question = input()

  sum_N1 = 0
  sum_A04800 = 0

  # Same way as question 1
  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question: # Get the value of the state code which I entered
      sum_N1 += int(returns_data[i+1][4])
      sum_A04800 += int(returns_data[i+1][96])
      question4_ans = round((sum_A04800 / sum_N1)*1000)
  
  
  f_answer.write("${:8.0f}".format(question4_ans))




  f_answer = open("answers.txt", "a")

  "-------------------Q5-------------------"
  # What is the average taxable income per return for each agi group?
  

  f_answer.write(answer_header(5, question_labels))

  # Same way as question 2
  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question:
      for j in range(6):
        question5_N1_data = int(returns_data[i+j+1][4])
        question5_A04800_data = int(returns_data[i+j+1][96])
        question5_ans = round((question5_A04800_data / question5_N1_data) * 1000)
        
        f_answer.write(gr_lst[j])
        f_answer.write(": ${:8.0f}".format(question5_ans) + "\n")
      
      break
 

  f_answer = open("answers.txt", "a")


  "-------------------Q6-------------------"
  # What is the average dependents per return for each agi group?


  f_answer.write(answer_header(6, question_labels))

  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question:
      for j in range(6):
        question6_N1_data = int(returns_data[i+j+1][4])
        question6_NUMDEP_data = int(returns_data[i+j+1][13])
        question6_ans = round((question6_NUMDEP_data / question6_N1_data), 2)
        
        f_answer.write(gr_lst[j])
        f_answer.write(": {:8.2f}".format( question6_ans) + "\n")
        
      break
 



  f_answer = open("answers.txt", "a")


  "-------------------Q7-------------------"
  # What is the percentage of returns with no taxable income per agi group?


  f_answer.write(answer_header(7, question_labels))

  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question:
      for j in range(6):
        question7_N1_data = int(returns_data[i+j+1][4])
        question7_N04800_data = int(returns_data[i+j+1][95])
        question7_ans = round(((question7_N1_data - question7_N04800_data)/question7_N1_data)*100, 2)
       
        f_answer.write(gr_lst[j])
        f_answer.write(": {:8.2f}%".format( question7_ans ) + "\n")
 
      break





  f_answer = open("answers.txt", "a")


  "-------------------Q8-------------------"
  # What is the average taxable income per resident? 
  # A04800 / population


  f_answer.write(answer_header(8, question_labels))

  # Use get_state_name to run the get_state_population function
  stname = get_state_name(states, question)
  pp_st = get_state_population(populations, stname) # Get the resident data


  sum_A04800 = 0

  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question:
      sum_A04800 += int(returns_data[i+1][96])
      question8_ans = round((sum_A04800 / pp_st)*1000)
  
  f_answer.write("${:8.0f}".format(question8_ans) + "\n")

 
 
  f_answer = open("answers.txt", "a")


  "-------------------Q9-------------------"
  # What is the percentage of returns for each agi_group?  (as a percentage of total returns for that state)


  f_answer.write(answer_header(9, question_labels))

  sum_N1 = 0
  question9_ans_lst = []

  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question:
      sum_N1 += int(returns_data[i+1][4])

  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question:

      for j in range(6): # Loop the function 6 times because one state has 6 agi group
        question9_N1_data = int(returns_data[i+j+1][4])
        question9_ans = round((question9_N1_data / sum_N1)*100, 2)
  
        question9_ans_lst.append(question9_ans)

        f_answer.write(gr_lst[j])
        f_answer.write(": {:8.2f}%".format(question9_ans) + "\n")
        

      break
  





  f_answer = open("answers.txt", "a")


  
  "-------------------Q10-------------------"
  # What is the percentage of taxable income for each agi_group? (as a percentage of total taxable income for that state)

  # A04800 / sum of A04800 * 100


  f_answer.write(answer_header(10, question_labels))

  sum_A04800 = 0
  question10_ans_lst = []

  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question:
      sum_A04800 += int(returns_data[i+1][96])


  for i in range(len(returns_data)-1):
    if returns_data[i+1][1] == question:

      for j in range(6): # Loop the function 6 times because one state has 6 agi group
        question10_A04800_data = int(returns_data[i+j+1][96])
        question10_ans = round((question10_A04800_data / sum_A04800)*100, 2)
    
        question10_ans_lst.append(question10_ans)

        f_answer.write(gr_lst[j])
        f_answer.write(": {:8.2f}%".format(question10_ans) + "\n")
        

      break
  


  f_answer.close()

  os.rename('answers.txt',  "answers" + question + ".txt") # Rename the answer file name to fulfill the requirements of answer file rubric







  "-------------------Visualization-------------------"

  """for the state level data"""

  # First visualization - pie chart

  labels = 'Group1', 'Group2', 'Group3', 'Group4', 'Group5', 'Group6' 
  sizes = question9_ans_lst # percentage data

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, labels=labels,autopct='%1.1f%%',
          shadow=True, startangle=90)
  
  plt.title("The percentage of returns for each group", bbox={'facecolor':'0.8', 'pad':5}) # Make the pie chart title

  plt.savefig( "pie1_" + question + ".png") # Save the pie chart image
 

  # Second visualization - pie chart

  labels = 'Group1', 'Group2', 'Group3', 'Group4', 'Group5', 'Group6'
  sizes = question10_ans_lst

  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, labels=labels,autopct='%1.1f%%',
          shadow=True, startangle=90)

  plt.title("The percentage of taxable income for each group", bbox={'facecolor':'0.8', 'pad':5})
  
  plt.savefig( "pie2_" + question + ".png")

  

  """for the national level data"""

  plt.clf()
  

  x = st_lst # set the x axis as state name
  y = question3_ans_lst # set the y axis as question3 answers
  

  new_dict = dict(zip(x, y)) # Make the dictionary with x and y values
  sorted_d = sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True) # Sort the dictionary for making descending graph

  new_x_lst = []
  new_y_lst = []

  for i in range(len(sorted_d)): # Split the key and value from the dictionary and make the new list of x axis and y axis
    new_x_lst.append(sorted_d[i][0])
    new_y_lst.append(sorted_d[i][1])


  plt.bar(new_x_lst, new_y_lst) # Make the bar graph
  plt.title("The average taxable income (per resident) per state") # Make the title
  plt.savefig("bar1.png") # Save the image




main() # Run the main function




