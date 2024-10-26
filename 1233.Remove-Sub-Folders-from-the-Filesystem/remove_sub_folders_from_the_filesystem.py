"""
LeetCode link to the problem: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

"""

#Optimised Time Complexity Solution
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        #Sort the list so that folders come before subfolders
        folder.sort()
        paths=[]
        for path in folder:
            #check if the paths in list are a subpath of the last added path to the result paths
            if paths and path.startswith(paths[-1]+"/"):
                continue
            paths.append(path)
        return paths



#Optmised Memory usage solution
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        #Sort the list so that folders come before subfolders
        folder.sort()
        i=0
        while(i<len(folder)):
            j=i+1
            while(j<len(folder)):
                #For each folder, if there is a subfolder in the list: remove it from the list
                if folder[j].startswith(folder[i]+"/"):
                    del folder[j]
                else:
                    j+=1
            i+=1
        return folder
