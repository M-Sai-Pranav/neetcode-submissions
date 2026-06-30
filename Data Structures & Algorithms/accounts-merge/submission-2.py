class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        hashmap = dict()
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                name = accounts[i][0]
                email = accounts[i][j]
                parent[email] = email
                hashmap[email] = name 
        
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        def union(u, v):
            rootU = find(u)
            rootV = find(v)
            if rootU == rootV:
                return True 
            parent[rootV] = rootU
            return False
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])-1):
                email1 = accounts[i][j]
                email2 = accounts[i][j+1]
                union(email1, email2) 
        group = {}
        for email in parent:
                root = find(email)
                if root not in group:
                    group[root] = []
                group[root].append(email)
        res = []
        for i in group:
            name = [hashmap[i]]
            emails = sorted(group[i])
            res.append(name + emails)
        return res 




