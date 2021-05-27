# Initial
check =[]
number = 0

def number_reading(number):
    check =[]
    # Create a loop
    while True:
        num = input(" Enter a number: ")
        # Check if the input is numberic
        if num.isnumeric() == True:
            check.append(num)
        if num == "done":
            break  
        # If the input is neither a number or 'done'
        else:
            try:
                int(num)
            except:
                print ("Invalid input. A number, idiot!")
                continue
    print ("Done!")  
    check = [int(i) for i in check]
    print("Total:", sum(check), "Count:", len(check), "Average:", round((sum(check)/ len(check)), 3))
# Call the function    
number_reading(number)

    