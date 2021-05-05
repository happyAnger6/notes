class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        e_hash = {}
        for employee in employees:
            e_hash[employee.id] = employee

        def dfs_value(id):
            nonlocal e_hash
            employee = e_hash[id]

            val = employee.importance
            for subordinate in employee.subordinates:
                sub_employee = e_hash[subordinate]
                val += dfs_value(sub_employee.id)
            return val

        return dfs(id)