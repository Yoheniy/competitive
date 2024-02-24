class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split("/")
        for i in range(len(path)):
            if path[i]=="" or path[i]=='.':
                continue
            elif stack and path[i]=='..':
                stack.pop()
            elif path[i]=='..':
                continue
            else:
                stack.append(path[i])
        return "/"+'/'.join(stack)
                


        