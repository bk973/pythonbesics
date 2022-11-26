# A set is an unordered collection that cannot contain duplicates...
# Creating sets

my_list = [ 1, 1, 2, 3, 4, 5, 6]
my_set = set(my_list)
print(my_set) #removes extra 1

digit_set = { 0, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(digit_set)

#checking for membership on a set
#function that checks for membership

def check_membership():
    member = input('Input an integer to check for membership... \n')
    return int(member) in digit_set # checks for membership

print(check_membership())