def hello():
  print("Hello One and All!\n")
  day = input("What is Today's Day?")
  print("It is a Beautiful ", day)
  if(day.lower() == "monday"):
    print("il fait beau lundi")
  elif day.lower() == "tuesday":
    print("il fait beau mardi")
  elif day.lower() == "wednesday":
    print("il fait beau mercredi")
  elif day.lower() == "thursday":
    print("il fait beau jeudi")
  elif day.lower() == "friday":
    print("il fait beau vendredi")
  elif day.lower() == "saturday":
    print("il fait beau samedi")
  elif day.lower() == "sunday":
    print("il fait beau dimanche")
  else:
    print("bebe! ce n'est pas un jour de la semaine")

hello()
