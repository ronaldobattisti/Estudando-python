"""
Decorators

What are decorators?
* Decorators are functions; in python functions are 1st class citzes
* Involve other functions and improve their behavior;
# Decorators are example of HOF
* Decorators have a own sintaxe, using @ (Sytatic sugar)


|------------------------------------------|
|            Function decorator            |
|------------------------------------------|

||----------------------------------------||
||----------------------------------------||
||--Decorated-Function(Visualy Improved)--||
||----------------------------------------||
||----------------------------------------||
"""

#1st exemple - non recommended sintaxe (wo sugar added)
def be_polite(function): #Generaly a function decorator gets a function as parameter
    def being():
        print("It was a plasure")
        function()  #using the decorator, we improve the fuction output. 
                    #If I execute only the "salutation" function, i'll have 
                    #a salutation, if I execute "be_polite(salutation)" 
                    #I will have the 1st print of "being" + salutation(as function) + 2nd print of "being"
        print("Have a great day!")
    return being

def salutation():
    print("Welcome!0")

#test 1
    
test = be_polite(salutation)
test()

print("----------------------------------------------")
#2nd exemple - decorators with sugar syntaxe

def be_polite_though(function):#>>>decoration function<<<
    def being_though():
        print("Nice to meet you")
        function()
        print("Have a nice day")
    return being_though

@be_polite_though#>>>decorator<<<
def presenting():
    print("My name is Ronaldo")

presenting()