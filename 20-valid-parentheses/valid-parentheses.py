class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        

        for i in range (len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                if (st[-1]=='(' and s[i]==')') or (st[-1]=='{' and s[i]=='}') or (st[-1]=='[' and s[i]==']') :
                    st.pop()
                else:
                    return False
        return len(st)==0
         
        