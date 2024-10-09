def sort_student(traits):
    if 'bravery' in traits:
        return 'Gryffindor'
    elif 'intelligence' in traits:
        return 'Ravenclaw'
    elif 'loyalty' in traits:
        return 'Hufflepuff'
    elif 'cunning' in traits:
        return 'Slytherin'
    else:
        return 'Unknown'

student_traits = ['bravery', 'loyalty']
print(sort_student(student_traits))