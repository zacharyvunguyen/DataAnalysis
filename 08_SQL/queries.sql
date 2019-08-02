--List the following details of each employee: employee number, last name, first name, gender, and salary
select s.emp_no, last_name, first_name, gender, salary
from employees emp
         inner join salaries s on emp.emp_no = s.emp_no;

--List employees who were hired in 1986.
select *
from employees
where date_part('year', hire_date) = 1986;

--List the manager of each department with the following information:
--department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
select dept_no, emp_no, from_date, to_date
from dept_emp;
--List the department of each employee with the following information:
--employee number, last name, first name, and department name.
select de.emp_no, last_name, first_name, dept_name
from employees emp

         inner join dept_emp de on emp.emp_no = de.emp_no
         inner join departments d on de.dept_no = d.dept_no;

--List all employees whose first name is "Hercules" and last names begin with "B."
select *
from employees
where first_name = 'Hercules'
  and last_name like 'B%';

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
select de.emp_no, last_name, first_name, dept_name
from employees emp
         inner join dept_emp de on emp.emp_no = de.emp_no
         inner join departments d on de.dept_no = d.dept_no
where dept_name = 'Sales';

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
select de.emp_no, last_name, first_name, dept_name
from employees emp
         inner join dept_emp de on emp.emp_no = de.emp_no
         inner join departments d on de.dept_no = d.dept_no
where dept_name in( 'Sales', 'Development');
--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
select last_name, count(last_name)
from employees
group by last_name
order by  count(last_name) desc;

----BONUS----
--Salary by titles
select title, avg(salary)
from salaries sal inner join employees e on sal.emp_no = e.emp_no inner join titles t on e.emp_no = t.emp_no
group by title;



