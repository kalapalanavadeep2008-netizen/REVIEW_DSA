class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth=0
        for customers in accounts:
            tot=0
            for money in customers:
                tot+=money
                if tot>max_wealth:
                    max_wealth=tot
        return max_wealth