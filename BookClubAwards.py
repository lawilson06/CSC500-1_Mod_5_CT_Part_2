ERROR_MSG1 = 'Enter a valid value. 🖍'
ERROR_MSG2 = 'Exceeded the maximum number of attempts. Setting value to 0.💥'

# try-except statements are used to catch invalid user entries (any other data type but integer will trigger error)
# user has three maximum attempts for a valid entry before the value is set to zero
# absolute values are taken instead of negative values if entered by the user

class BookClubAwards:
    def __init__(self):
        self.__base_value = 5
        self.__base_multiplier = 3
        self.__counter = 1
        self.__multiplier = 0
        self.__reward_points = 0
        self.__reward_points_arr = []
        self.__books_purchased = 0
        self.__reward_generator()

    def __add_rewards_record(self):
        self.__reward_points = self.__base_value * self.__multiplier
        self.__reward_points_arr.append(self.__reward_points)

# Points array is created for the first eight books

    def __reward_generator(self):
        for i in range(9):
            if i % 2 == 0 and i >= 4:
                self.__multiplier = self.__base_multiplier * self.__counter
                self.__add_rewards_record()
                self.__counter *= 2
            elif i % 2 == 0 and i != 0:
                self.__multiplier = 1
                self.__add_rewards_record()
            else:
                self.__add_rewards_record()

# Awards are looked up from the array and returned after user enters number of books

    def reward_return(self):
        counter = 0
        points_return = 0
        while counter < 3:
            try:
                self.__books_purchased = abs(int(input("Please enter the number of books purchased: ")))
                break
            except (ValueError,OverflowError):
                print(ERROR_MSG1)
            counter += 1
        if counter >= 3:
            print(ERROR_MSG2)
        else:
            points_return =  self.__reward_points_arr[self.__books_purchased] \
                if self.__books_purchased < 9 else self.__reward_points_arr[-1]
        return points_return