class Solution(object):
    def findWords(self, words):
        
        dictAlp = {'0':['q','w','e','r','t','y','u','i','o','p'],
                   '1':['a','s','d','f','g','h','j','k','l'],
                   '2':['z','x','c','v','b','n','m']}
        
        result = list()
        for e in words:
            sum_word = ''
            for it in e.lower():
                sum_word += [k for k,v in dictAlp.items() if it in v][0]
            if len(set(sum_word)) == 1:
                result.append(e)
                
        return result

if __name__ == "__main__":
    print(Solution().findWords(['Qsz','rqwer','dawerds', 'vcxvx', 'dsgfdh']))
