class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)     
        occurence=[0]*(n+1) #citation occurnce frequency
        
        for i in citations:
            occurence[min(n,i)]+=1
        print (occurence)
        #occurence we have citation as index
        #
        cumulative_paper=0
        for h_index in range(n,-1,-1):
            
            cumulative_paper+=occurence[h_index]
            print(h_index,'-----',occurence[h_index])
            if cumulative_paper>=h_index:
                return h_index




        
