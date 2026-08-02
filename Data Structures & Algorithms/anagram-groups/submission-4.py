class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Outer for loop
        check if it is in the seen dict. 
            if no:
                create a key, and push the first value into it "key":["key"]

            if yes:
                append the key. "key":["key", "key2"]
            
            for key in seen
            return [].append(seen[key])
        """
        seen = {}

        for i in range(len(strs)):
            sortea_str = "".join(sorted(strs[i]))
            if sortea_str in seen:
                seen[sortea_str].append(strs[i]) # Append is an inplace operation and it doesn't return anything.

            else:
                seen[sortea_str] = [strs[i]]
        return list(seen.values())

