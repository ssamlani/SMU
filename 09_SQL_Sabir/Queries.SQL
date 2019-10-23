
--1.    List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT  e.emp_no ,
        e.last_name ,
        e.first_name ,
        e.gender ,
        s.salary
FROM    employees e
        LEFT JOIN salaries s ON e.emp_no = s.emp_no
ORDER BY e.last_name ASC;

--2.    List employees who were hired in 1986.

SELECT  emp_no ,
        first_name ,
        last_name ,
        gender ,
        hire_date
FROM    employees
WHERE   
        EXTRACT (YEAR FROM hire_date) = 1986
ORDER BY
        last_name ASC;


--3.    List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.   

SELECT  d.dept_no AS "Department No." ,
        d.dept_name AS "Department Name" ,
        e.emp_no AS "Employee No." ,
        e.last_name AS "Last Name" ,
        e.first_name AS "First Name" ,
        dm.from_date AS "Start Date" ,
        dm.to_date AS "End Date"
FROM    public.dept_manager dm
        INNER JOIN public.departments d ON dm.dept_no = d.dept_no
        INNER JOIN public.employees e ON e.emp_no = dm.emp_no;


--4.    List the department of each employee with the following information: employee number, last name, first name, and department name.


SELECT 
    e.emp_no ,
    e.first_name,
    e.last_name,
    d.dept_name

FROM 
public.employees e
left join public.dept_emp de  on e.emp_no = de.emp_no
left join public.departments d on d.dept_no = de.dept_no
order by last_name asc ;

--5.    List all employees whose first name is "Hercules" and last names begin with "B."


SELECT  e.emp_no ,
        first_name ,
        last_name
FROM    employees e
WHERE   e.last_name LIKE 'B%'
        AND e.first_name = 'Hercules';

--6.    List all employees in the Sales department, including their employee number, last name, first name, and department name.

 SELECT 
        e.emp_no ,
        first_name,
        last_name
FROM     employees e
left join public.dept_emp de on de.emp_no = e.emp_no
left join public.departments d on d.dept_no =de.dept_no
where d.dept_name LIKE 'Sales';


--7.    List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

SELECT 
    e.emp_no ,
    first_name,
    last_name,
    dept_name
FROM 
employees e
join public.dept_emp de on de.emp_no = e.emp_no
 join public.departments d on d.dept_no =de.dept_no
where d.dept_name in ('Sales','Development');

--8.    In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.


SELECT  e.last_name ,
        COUNT(e.emp_no) AS Lastname_count
FROM    employees e
GROUP BY last_name
ORDER BY Lastname_count DESC












