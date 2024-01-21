'''
dunder name and dunder main
__name__
__main__

What are dunder methods -> create functions, attributes, properties, ect to not generate conflict with these ellements names in the program

#in C we have
int main(){
    return 0
}

#in java:
public static void main(String[] args){

}

#in python we don't have this, if we execute a module right in the command line, python atributer __name__ the value __main__, saying that is the mains module
'''

from model_function import sum_numbers

print(sum_numbers(2, 2))#A real python program shouldn'r print "ronaldo"

from model_function2 import sum_numbers#just execute the prints if the function was the main file

print(sum_numbers(2, 2))#A real python program shouldn'r print "ronaldo"