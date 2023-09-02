class Solution:
    def garbageCollection(self, garbage, travel):
        last_g_ct, last_p_ct, last_m_ct = 0, 0, 0
        last_g, last_p, last_m = -1, -1, -1

        prefix_travel = [travel[0]]
        for i in range(1, len(travel)):
            prefix_travel.append(prefix_travel[-1] + travel[i])

        for i, v in enumerate(garbage):
            if "G" in v:
                last_g = i
                last_g_ct += v.count("G")
            if "P" in v:
                last_p = i
                last_p_ct += v.count("P")
            if "M" in v:
                last_m = i
                last_m_ct += v.count("M")

        ans = last_g_ct + last_p_ct + last_m_ct

        if last_g > 0:
            ans += prefix_travel[last_g - 1]
        if last_p > 0:
            ans += prefix_travel[last_p - 1]
        if last_m > 0:
            ans += prefix_travel[last_m - 1]

        return ans