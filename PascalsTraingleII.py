class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[[1]]
        for i in range(rowIndex):
            if rowIndex==0:
                return res
            else:
                row=[]
                temp=[0]+res[-1]+[0]
                for j in range(len(res[-1])+1):
                    row.append(temp[j]+temp[j+1])
                res.append(row)
        return res[rowIndex]
                
