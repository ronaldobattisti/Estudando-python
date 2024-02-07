#import math

def read_file(file_name):
    with open(file_name, 'r') as file:
        text = file.read().split('\n')
    if '' in text:
        text.pop(text.index(''))
    text = [item.split(',') for item in text]
    #print(text)
    class_dict = {}
    for item in text:
        key = item[0]
        values = item[1:len(item)]
        values = [float(item) for item in values]
        class_dict.update({key: values})
    return(class_dict)

def check_file_infos(file_name):
    with open(file_name, 'r') as file:
        text = file.read().split('\n')
    if '' in text:
        text.pop(text.index(''))
    text = [item.split(',') for item in text]
    try:
        for item in text:
            values = item[1:len(item)]
            values = [float(item) for item in values]
    except ValueError as e:
        print(f'That\'s a unvalid value, ferify the .txt file: {e}')
        return False
    else:
        return True

def add_student(class_dict, student_name, grades):
    class_dict = class_dict.update({student_name: grades})
    print(class_dict)
    return dict_class, True

def avg_grade(dict_class):
    avg = {}
    for item in dict_class:
        avg.update({item: (sum(dict_class[item])/len(dict_class[item]))})
    return avg

def save_data(dict_class, file_name):
    text = ''
    with open(file_name, 'w') as file:
        for item in dict_class:
            text = (f"{text}{item},{','.join(str(grade) for grade in dict_class[item])}\n")
        file.write(text)
    return False
'''def show_class_data(file_name):
    read_file(file_name)'''

if __name__ == '__main__':
    file_name = "C:/Users/RONAL/Desktop/Exercicios programacao python do basico ao avancado/Chapter_13/Ex27/class_info.txt"
    inp = ''
    is_unsaved_change = False
    if check_file_infos(file_name):
        dict_class = read_file(file_name)
        while inp != 0:
            try:
                inp = int(input('Select a option:\n'
                                '1 - Show class data\n'
                                '2 - Insert student and grade\n'
                                '3 - Show students and average grade\n'
                                '4 - Show failed students\n'
                                '5 - Save data\n'
                                '6 - Quit program\n'))
            except ValueError as e:
                print(f'Value is not a integer: {e}')
            if inp == 1:
                for item in dict_class:
                    print(item, dict_class[item])
            elif inp == 2:
                student_name = str(input("Write the student name: "))
                grades = []
                try:
                    for item in range(1, 5):
                        grades.append(float(input(f'Insert the {item}º grade: ')))
                except ValueError as e:
                    print(f'Value should be a number, ex\'4.2\': {e}')
                dict_class, is_unsaved_change = add_student(dict_class, student_name, grades)
            elif inp == 3:
                average = avg_grade(dict_class)
                for item in average:
                    print(item, average[item])
            elif inp == 4:
                average = avg_grade(dict_class)
                for item in average:
                    if average[item] < 6:
                        print(item, average[item])
            elif inp == 5:
                is_unsaved_change = save_data(dict_class, file_name)
            elif inp == 6:
                if is_unsaved_change:
                    ans = input('There are unsaved changes, do you really want to quit without saving?(y/n)')
                    if ans == 'y':
                        break
                    elif ans == 'n':
                        0
                    else:
                        print('Invalid input')
                else:
                    break
            else:
                print('Input out of range, please select one of the options showed:\n')