from SeventhWeek import first_greedy_until1
from SeventhWeek import second_implementation_UDLR
from SeventhWeek import third_DFSNBFS_frozenJuice

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # #7week_1st
    # N = 25
    # K = 3
    # print(first_greedy_until1.solution(N,K))

    #7week_2nd
    # N = 5
    # plans = "R R R U D D"
    # print(second_implementation_UDLR.solution(N,plans))

    #7week_3rd
    N = 15
    M = 14
    field = [
        [0,0,0,0,0,1,1,1,1,0,0,0,0,0],
        [1,1,1,1,1,1,0,1,1,1,1,1,1,0],
        [1,1,0,1,1,1,0,1,1,0,1,1,1,0],
        [1,1,0,1,1,1,0,1,1,0,0,0,0,0],
        [1,1,0,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,1,1,1,1,1,1,1,1,1,0,0],
        [1,1,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0,0,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,0,1,1,1,1,1,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,1,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,0,0,1,1],
        [1,1,1,0,0,0,1,1,1,1,1,1,1,1],
        [1,1,1,0,0,0,1,1,1,1,1,1,1,1]
    ]
    print(third_DFSNBFS_frozenJuice.solution(N,M,field))





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
