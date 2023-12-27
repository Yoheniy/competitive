class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d={}
        for domain in cpdomains:
            domain_list=domain.split(" ")
            numberOfVisted=int(domain_list[0])
            subdomains=list((domain_list[1]).split("."))
            for subdomain in range(len(subdomains)):
                webdomain=".".join(subdomains[subdomain:])
                if webdomain not in d:
                    d[webdomain]=numberOfVisted
                else:
                    d[webdomain]+=numberOfVisted
        listOfKeys=list(d.keys())
        listOfValues=list(d.values())
        ans=[]
        for element in range(len(listOfKeys)):
            countPaired=str(listOfValues[element])
            countPaired+=" "
            countPaired+=str(listOfKeys[element])
            ans.append(countPaired)
        return ans
        





        