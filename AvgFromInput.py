#Amani Minaya
#Average From Input 
def main():
    total = 0.0
    count = 0
    random_numbers_file = open('numbers.txt','r')
#iterate for loop for all lines in 'file'
    for line in random_numbers_file:
            number = float(line)
            count += 1
            total += number
            print("I read in", count, " number(s) Current number is:", number, "Total is: ", total)
    average = total / count
    print("Average:", format(average,'.2f'))

main()
