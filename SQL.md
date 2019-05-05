- Nth maximum 
```WITH CTE AS
(
    SELECT EmpID, EmpName, EmpSalary,
           RN = ROW_NUMBER() OVER (ORDER BY EmpSalary DESC)
    FROM dbo.Salary
)
SELECT EmpID, EmpName, EmpSalary
FROM CTE
WHERE RN = @NthRow
```