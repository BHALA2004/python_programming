try:
    file = open('exam.txt','r')
except ZeroDivisionError:
    print("Divide By Zero")
except FileNotFoundError:
    print("No File is Present")
finally:
    print("Good")
