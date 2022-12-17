class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        print(6/-132)
        fir=0
        sec=0
        if len(tokens)==1:
            return int(tokens[0])
        for i in tokens:
            if (i.strip('-')).isnumeric():
                stack.append(int(i))
            else:
                fir=int(stack.pop())
                sec=int(stack.pop())
                print(i,"char")
                if ord(i)==43:
                    fir=fir+sec
                    stack.append(fir)
                    print(fir,"add")
                if ord(i)==45:
                    fir=sec-fir
                    stack.append(fir)
                    print(fir,"sub")
                if ord(i)==42:
                    fir=fir*sec
                    stack.append(fir)
                    print(fir,"MUL")
                if ord(i)==47:
                    print(sec,fir)
                    fir=sec/fir
                    stack.append(fir)
                    print(fir,"di")
                
        return int(fir)
                