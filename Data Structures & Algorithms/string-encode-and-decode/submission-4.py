class Solution:

    def encode(self, strs: List[str]) -> str:
        print(len(strs),strs)
        if len(strs)==1 and strs==['']:
            return 'none'
        if len(strs)>=1:
            return ",#,".join(strs)
        if len(strs)==0:
            return "null"
         

    def decode(self, s: str) -> List[str]:
        if s=='null':
            return []
        return s.split(',#,') if s!='none' else [""]
