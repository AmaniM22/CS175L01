#Amani Minaya
#Average From Input file with exception handling
def loop (random_number_file):    
    for line in random_numbers_file:
            number = float(line)
            count += 1
            total += number
            print("I read in", count, " number(s) Current number is:", number, "Total is: ", total)
            random_number_file.close()
            return total, count
        
def avg (total,count):
    average = total / count
    return average

def printing(average):
    try:
        print("Average:", format(average,'.2f'))
        except IOError:
            print('An error occurred trying to read the file.')
        except ValueError:
            print('Non-numeric data found in the file')
        except:
            print('An error has occurred')

def main():
    total = 0.0
    count = 0
    random_numbers_file = open('numbers.txt','r')
    number=loop('number.txt', total, count)   
    average=avg(total,count)
    printing(average)

main()
