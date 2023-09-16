class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        source = set()
        destination = set()

        for s, d in paths:
            source.add(s)
            destination.add(d)

        for d in destination:
            if d not in source:
                return d
            
        return None