class Solution:
    def isHappy(self, n: int) -> bool:
        num_to_str = str(n)
        results = set()
        
        while True :
            sum_square =0

            for  val in num_to_str:
                sum_square+= int(val)**2

            if (sum_square == 1) :
                return True

            if sum_square in results : 
                return False

            else : 
                results.add(sum_square)

            num_to_str = str(sum_square)



        
