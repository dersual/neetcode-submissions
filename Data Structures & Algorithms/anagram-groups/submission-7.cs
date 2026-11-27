public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) { 
        var ret = new Dictionary<string, List<string>>(); 

        foreach (var str in strs) {  
            var counts = new int[26];  
            foreach (var c in str) counts[c - 'a']++; 
            var key = string.Join("#", counts); 
            if (!ret.ContainsKey(key)) ret[key] = new List<string>(); 
            ret[key].Add(str);
        } 
        return ret.Values.Select(g => g.ToList()).ToList();
    }
}
