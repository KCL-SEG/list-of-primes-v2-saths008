def primes(number_of_primes):

    if number_of_primes > 0:
        list = []
        list.append(2)
        current_number = 3
        
        while len(list) < number_of_primes :

            i = 0

            for i in range(0, len(list)):
                  
                #if current number is a multiple of any number in the list, then increase current number by 1 and repeat process
                if(current_number % list[i] == 0):
                    print(f"i ---> {i}, and current_number ---> {current_number}")
                    i = 0
                    current_number+=1
                    break
        
                #if current number doesn't divide into the last element in the list, which means it has 
                #iterated through the rest of the numbers less than it, then add this number is a prime
                elif (not (current_number % list[i] == 0))  and (i == (len(list) -1)):
                    list.append(current_number)
                    current_number+=1


        return(list)


    else:
        raise ValueError(f"number_of_primes variable = {number_of_primes}. It must be >0.")


