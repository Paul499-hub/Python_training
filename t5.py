
board = [[".",".","4", ".",".",".", "6","3","."],
         [".",".",".", ".",".",".", ".",".","."],
         ["5",".",".", ".",".",".", ".","9","."],

         [".",".",".", "5","6",".", ".",".","."],
         ["4",".","3", ".",".",".", ".",".","1"],
         [".",".",".", "7",".",".", ".",".","."],

         [".",".",".", "5",".",".", ".",".","."],
         [".",".",".", ".",".",".", ".",".","."],
         [".",".",".", ".",".",".", ".",".","."]]

def isValidSudoku(board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def scan(startX, startY, scan_orentation='l'):

            # SCAN 3x3  
            #print(f'[SCAN MODE {scan_orentation}]')
            for i in range(startY, startY+9): # DOWN
                s=set()
                for k in range(startX,startX+9): #LEFT
                    current_member = board[i][k] if scan_orentation=='l' else board[k][i] #<--- DECIDE IF SCAN DOWN OR LEFT
                    if current_member not in {'0','1','2','3','4','5','6','7','8','9','.'}: # NUMBER 1-9 CONTITION CHECK
                        #print('NUMBER 1-9 CONTITION CHECK FAILED')
                        return False
                    #print(f'[BIG SCAN {scan_orentation}] board member ik ----> {current_member}')

                    # CHECK IF EXISTS IN SET
                    if (current_member not in s or current_member=='.'):
                        s.add(current_member)
                    else:
                        #print(f'-------- ERROR, REPEAT MEMBER FOUND : {current_member}')
                        return False
            return True
        

        def scan_small(startX, startY, scan_orentation='l'):

            # SCAN 3x3  
            total_set=set()
            #print(f'[SCAN MODE {scan_orentation}]')
            for i in range(startY, startY+3): # DOWN
                for k in range(startX,startX+3): #LEFT
                    current_member = board[i][k] if scan_orentation=='l' else board[k][i] #<--- DECIDE IF SCAN DOWN OR LEFT
                    if current_member not in {'0','1','2','3','4','5','6','7','8','9','.'}: # NUMBER 1-9 CONTITION CHECK
                        #print(f'NUMBER 1-9 CONTITION CHECK FAILED, cn:{current_member}')
                        return False
                    #print(f'[SMALL SCAN] board member ik ----> {current_member}')
                    # CHECK IF EXISTS IN SET
                    if (current_member not in total_set or current_member=='.') :
                        total_set.add(current_member)
                    else:
                        #print(f'-------- ERROR, REPEAT MEMBER FOUND : {current_member}')
                        return False
            return True
        

        if not scan(0,0,'l'): return False

        if not scan(0,0,'d'): return False
        
        maxDownIdx=len(board) - 3  # IDX MUST BE LESS THAN THIS
        maxLeftIdx= len(board[0]) - 3  # IDX MUST BE LESS THAN THIS

        startX=0
        startY=0

        while startY<=maxDownIdx:
            startX=0
            while startX<=maxLeftIdx:
                
                if not scan_small(startX,startY,'l'):
                    print(f' SMALL SCAN FAILED ')
                    return False 

                startX+=3 #<=== MOVE LEFT
            startY+=3 #<=== MOVE DOWN
        return True


print(isValidSudoku(board))

    


    