WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
class SemanticNetsAgent:
    def __init__(self):
        pass

    def solve(self, initial_sheep, initial_wolves):

        #Add your code here! Your solve method should receive
        # the initial number of sheep and wolves as integers,
        #and return a list of 2-tuples that represent the moves 
        #required to get all sheep and wolves from the left
        #side of the river to the right .
        #If it is impossible to move the animals over according
        #to the rules of the problem, return an empty list of
        #moves.
        moves = []
        left_sheep = initial_sheep
        left_wolves = initial_wolves
        right_sheep = 0
        right_wolves = 0
        boat_on_left = True

        while left_sheep > 0 or left_wolves > 0:
            if boat_on_left:
                if left_sheep >= left_wolves or left_sheep == 0:
                    if left_sheep > 0:
                        left_sheep -= 1
                        right_sheep += 1
                    moves.append(('Sheep', 'right'))
                else:
                    if left_wolves > 0:
                        left_wolves -= 1
                        right_wolves += 1
                    moves.append(('Wolf', 'right'))
            else:
                if right_sheep > right_wolves or right_sheep == 0:
                    if right_sheep > 0:
                        right_sheep -= 1
                        left_sheep += 1
                    moves.append(('Sheep', 'left'))
                else:
                    if right_wolves > 0:
                        right_wolves -= 1
                        left_wolves += 1
                    moves.append(('Wolf', 'left'))
            boat_on_left = not boat_on_left

        return moves

