print("Title of program: Post Exam bot")
print()
while True:
  description = input("Could you describe how you feel in a sentence?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "unmotivated":
      feelings_list.append("unmotivated")
      encouragement_list.append("to do something that makes you happy for the today, and try to plan ahead for tomorrow")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("that you are stronger than you think")
      counter += 1
    if each_word == "crazy":
      feelings_list.append("maniac")
      encouragement_list.append("to calm down calm down")
      counter += 1
    if each_word == "lazy":
      feelings_list.append("lazy")
      encouragement_list.append("to do something more productive")
      counter += 1
    if each_word == "nostalgic":
      feelings_list.append("nostalgic")
      encouragement_list.append("that you should write down what's on your mind")
      counter += 1
    if each_word == "sick":
      feelings_list.append("unwell")
      encouragement_list.append("to take a nap and drink some water")
      counter += 1
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("it's ok to feel this way. You've done your best today, be proud of yourself.")
      counter += 1


  if counter == 0:
    
      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember  "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
