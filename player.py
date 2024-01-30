
import time

class Ai:
    def __init__(self, shape):
        self.shape = shape
        self.X = shape[0]
        self.Y = shape[1]

    def boundaries(self, i, j):
        return 0 <= i < self.X and 0 <= j < self.Y
    
    def possibleMoves(self, state):
        possible_moves = []
        occupied_edges = set()

        for line in state:
            if line is not None:
                occupied_edges.add(line)

        for i in range(self.X):
            for j in range(self.Y):
                if j + 1 < self.Y and ((i, j), (i, j + 1)) not in occupied_edges and ((i, j + 1), (i, j)) not in occupied_edges:
                    possible_moves.append(((i, j), (i, j + 1)))
                    occupied_edges.add(((i, j), (i, j + 1)))

                if i + 1 < self.X and ((i, j), (i + 1, j)) not in occupied_edges and ((i + 1, j), (i, j)) not in occupied_edges:
                    possible_moves.append(((i, j), (i + 1, j)))
                    occupied_edges.add(((i, j), (i + 1, j)))

        return possible_moves



    def is_square(self, x1, y1,x2, y2 ,state):
        if x1 == x2:
            #left and right
            if ((self.boundaries(x1-1 , y1) and self.boundaries(x1 , y1) and (((x1 - 1, y1),(x1,y1)) in state or ((x1,y1) , (x1 - 1, y1)) in state)) and ( self.boundaries(x1 - 1, y1 + 1) and self.boundaries(x1-1 , y1) and (((x1 - 1, y1 + 1) , (x1-1 , y1)) in state or ((x1-1 , y1) , (x1 - 1, y1 + 1)) in state)) and (self.boundaries(x1 - 1, y1 + 1) and self.boundaries(x2 , y2) and (((x1 - 1, y1 + 1) , (x2 , y2)) in state or ((x2 , y2) , (x1 - 1, y1 + 1) ) in state))):
                    return True
            elif ((self.boundaries(x1+1 , y1) and self.boundaries(x1 , y1) and (((x1 + 1, y1),(x1,y1)) in state or ((x1,y1) , (x1 + 1, y1)) in state)) and ( self.boundaries(x1 + 1, y1 + 1) and self.boundaries(x1 + 1 , y1) and (((x1 + 1, y1 + 1) , (x1 + 1 , y1)) in state or ((x1 + 1 , y1) , (x1 + 1, y1 + 1)) in state)) and (self.boundaries(x1 + 1, y1 + 1) and self.boundaries(x2 , y2) and (((x1 + 1, y1 + 1) , (x2 , y2)) in state or ((x2 , y2) , (x1 + 1, y1 + 1) ) in state))):
                    return True

        elif y1 == y2:
            #up and down
            if ((self.boundaries(x1 , y1 -1 ) and self.boundaries(x1 , y1) and (((x1, y1 - 1),(x1,y1)) in state or ((x1,y1) , (x1, y1 - 1)) in state)) and ( self.boundaries(x1 + 1, y1 - 1) and self.boundaries(x1 , y1 - 1) and (((x1 + 1, y1 - 1) , (x1 , y1 - 1)) in state or ((x1 , y1 - 1) , (x1 + 1, y1 - 1)) in state)) and (self.boundaries(x1 + 1, y1 - 1) and self.boundaries(x2 , y2) and (((x1 + 1, y1 - 1) , (x2 , y2)) in state or ((x2 , y2) , (x1 + 1, y1 - 1) ) in state))):
                return True
            elif ((self.boundaries(x1 , y1 + 1 ) and self.boundaries(x1 , y1) and (((x1, y1 + 1),(x1,y1)) in state or ((x1,y1) , (x1, y1 + 1)) in state)) and ( self.boundaries(x1 + 1, y1 + 1) and self.boundaries(x1 , y1 + 1) and (((x1 + 1, y1 + 1) , (x1 , y1 + 1)) in state or ((x1 , y1 + 1) , (x1 + 1, y1 + 1)) in state)) and (self.boundaries(x1 + 1, y1 + 1) and self.boundaries(x2 , y2) and (((x1 + 1, y1 + 1) , (x2 , y2)) in state or ((x2 , y2) , (x1 + 1, y1 + 1) ) in state))):
                return True
        return False

    def makes_three_lines(self , x1 , y1 , x2 , y2 , state):
        if x1 == x2 :
            if(self.boundaries(x1 , y1) and self.boundaries(x1+1 , y1) and (((x1,y1),(x1+1 , y1)) in state or ((x1+1 , y1) , (x1,y1)) in state)) and (self.boundaries(x1 + 1 , y1) and self.boundaries(x1 +1 , y1 + 1) and (((x1 + 1 , y1), (x1 +1 , y1 + 1)) or ( (x1 +1 , y1 + 1) , (x1 + 1 , y1)))):
                return True

            elif (self.boundaries(x1 , y1) and self.boundaries(x1 - 1 , y1) and (((x1,y1),(x1 - 1 , y1)) in state or ((x1 - 1 , y1) , (x1,y1)) in state)) and (self.boundaries(x1 - 1 , y1) and self.boundaries(x1 - 1, y1 + 1) and (((x1 - 1 , y1), (x1 - 1 , y1 + 1)) or ( (x1 - 1 , y1 + 1) , (x1 + 1 , y1)))):
                return True

            elif (self.boundaries(x2 , y2) and self.boundaries(x1 + 1 , y1 + 1) and (((x2 , y2) , (x1 + 1 , y1 + 1)) in state or ((x1 + 1 , y1 + 1) , (x2,y2)) in state)) and (self.boundaries(x1 + 1 , y1 + 1) and self.boundaries(x1 + 1, y1) and (((x1 + 1 , y1 + 1), (x1 + 1, y1) ) or ( (x1 + 1, y1) , (x1 + 1 , y1 + 1)))):
                return True

            elif (self.boundaries(x2, y2) and self.boundaries(x1 - 1, y1 + 1) and (((x2, y2), (x1 - 1, y1 + 1)) in state or ((x1 - 1, y1 + 1), (x2, y2)) in state)) and (self.boundaries(x1 - 1, y1 + 1) and self.boundaries(x1 - 1, y1) and (((x1 - 1, y1 + 1), (x1 - 1, y1)) or ((x1 - 1, y1), (x1 - 1, y1 + 1)))):

                return True

        if y1 == y2:
            if (self.boundaries(x2, y2) and self.boundaries(x1 + 1, y1 + 1) and (((x2, y2), (x1 + 1, y1 + 1)) in state or ((x1 + 1, y1 + 1), (x2, y2)) in state)) and (self.boundaries(x1 + 1, y1 + 1) and self.boundaries(x1, y1 + 1) and (((x1 + 1, y1 + 1), (x1, y1 + 1)) or ((x1, y1 + 1), (x1 + 1, y1 + 1)))):
                return True
            elif (self.boundaries(x2, y2) and self.boundaries(x1 + 1, y1 - 1) and (((x2, y2), (x1 + 1, y1 - 1)) in state or ((x1 + 1, y1 - 1), (x2, y2)) in state)) and (self.boundaries(x1 + 1, y1 - 1) and self.boundaries(x1, y1 - 1) and (((x1 + 1, y1 - 1), (x1, y1 - 1)) or ((x1, y1 - 1), (x1 + 1, y1 - 1)))):
                return True
            elif (self.boundaries(x1, y1) and self.boundaries(x1, y1 + 1) and (((x1, y1), (x1, y1 + 1)) in state or ((x1, y1 + 1), (x1, y1)) in state)) and (self.boundaries(x1, y1 + 1) and self.boundaries(x1 + 1, y1 + 1) and (((x1, y1 + 1), (x1 + 1, y1 + 1)) or ((x1 + 1, y1 + 1), (x1, y1 + 1)))):
                return True

            elif (self.boundaries(x1, y1) and self.boundaries(x1, y1 - 1) and (((x1, y1), (x1, y1 - 1)) in state or ((x1, y1 - 1), (x1, y1)) in state)) and (self.boundaries(x1, y1 - 1) and self.boundaries(x1 + 1, y1 - 1) and (((x1, y1 - 1), (x1 + 1, y1 - 1)) or ((x1 + 1, y1 - 1), (x1, y1 - 1)))):
                return True


        return False


    def heuristic(self, state, action):
        new_state = state + [action]

        given_boxes = 0
        for move in self.possibleMoves(new_state):
            if self.is_square(move[0][0], move[0][1], move[1][0], move[1][1], new_state):
                given_boxes += 1

        taken_boxes = 0
        for opponent_action in self.possibleMoves(new_state):
            opponent_state = new_state + [opponent_action]
            for move in self.possibleMoves(opponent_state):
                if self.is_square(move[0][0], move[0][1], move[1][0], move[1][1], opponent_state):
                    taken_boxes += 1

        score = given_boxes - taken_boxes

        return score






    def min_value(self, state, alpha, beta, depth):
        if depth == 0 or self.is_over(state):
            return self.heuristic(state, None)

        v = float('inf')

        for move in self.possibleMoves(state):
            v = min(v, self.max_value(state + [move], alpha, beta, depth))
            beta = min(beta, v)
            if beta <= alpha:
                break  
        return v

    def max_value(self, state, alpha, beta, depth):
        if depth == 0 or self.is_over(state):
            return self.heuristic(state, None)

        v = float('-inf')

        for move in self.possibleMoves(state):
            v = max(v, self.min_value(state + [move], alpha, beta, depth - 1))
            alpha = max(alpha, v)
            if beta <= alpha:
                break  
        return v

    def decide(self, state):
        valid_moves = self.possibleMoves(state)

        best_score = float('-inf')
        best_move = None
        

        max_dimension = max(self.X, self.Y)
        if max_dimension > 5 :
            depth = 1
        else :
            depth = 2

        
        start = time.time()

        for move in valid_moves:
            
            score = self.min_value(state + [move], float('-inf'), float('inf'), depth -1 )
            end = time.time()
            total_time = end - start

            if total_time > 2:
                break

            if score > best_score:
                best_score = score
                best_move = move

        return best_move





    def is_over(self , state):
        if self.possibleMoves(state) :
            return True
        return False








#x = Ai(shape=(3,3))
# mystates = [((0 ,0) , (0 , 1)) , ((1 , 0),(2,0)) , ((1,2),(2,2))]
# pm = x.possibleMoves(state=mystates)
# print(len(pm))
# for i in range (len(pm)) :
#     print(pm[i])
#
#
# print(mystates)
# # print(x.X)
# # print(x.Y)

# st = [((1,0),(2,0)) , ((1,0),(1,1)) , ((1,1),(2,1))]
# print(x.is_square(2 , 0 , 2 , 1 , st))




def main():
    x = Ai(shape=(10, 10))
    state1 = [((0, 0), (0, 1)), ((1, 0), (2, 0)), ((1, 2), (2, 2))]
    state2 = [((0 , 0),(1 , 0)) , ((0 , 0),(0 , 1)) , ((1 , 0),(1 , 1)) , ((0 , 1),(0 , 2)) , ((1,1),(1,2)) , ((0,2),(1,2))]
    state = [((0,0),(1,0)) , ((1,0),(2,0)) , ((2,0),(3,0)) , ((3,0),(4,0)) , ((4,0),(4,1)) , ((4,1),(3,1)) , ((3,1),(2,1)) , ((2,1),(1,1)) , ((1,1),(0,1)) , ((0,0),(0,1))] 
    #(1,0),(1,1) / (2,0) (2,1) / (3,0) (3,1) 
    start = time.time()
    best_move = x.decide(state)
    end = time.time()
    print(end-start)
    print(best_move)

if __name__ == "__main__":
    main()
