!!! info "操作环境"
    Ubuntu 24.04

## Mysql 数据库安装
### WSL中安装
```bash
sudo apt install mysql-server
```

### 以root用户登录并修改root用户密码
执行以下语句，强制以root用户登录
```bash
sudo mysql -u root 
```
修改密码:
```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_password';
```

## 基本操作
### 创建数据库
```sql
CREATE DATABASE db_name;
```
### 查询当前所有数据库的名称
```sql
SHOW DATABASES;
```

### 创建数据表
```sql
CREATE TABLE table_name (name TYPE CONSTRAINTS,...);
```

```sql title="创建样例"
create table instructor(
    ID char(5),
    name varchar(20) not null,
    dept_name varchar(20),
    salary numeric(8,2),
    primary key(ID),
    foreign key(dept_name) references department
    on delete cascade | set null | restrict | set default
    on update cascade | set null | restrict | set default,
);
```

### 插入数据
```sql
INSERT INTO table_name (name, age) VALUES ('John', 30);
```

### 查询数据

```sql title="查询样例"
select '437' as FOO 
/* Results is a table with one column and a single row with value '437'*/
select 'A' from instructor
/*Result is a table with one column and N rows(number of tuples in the instructors table), each row with value 'A'*/
select ID,name, salary/12 from instructor
/* would return a relation that is the same as the instructor relation, except thaht the value of the attribute salary is divided by 12.*/
select distinct dept_name from instructor
/* find the department name of all insturctors, and remove duplicates*/
select all dept_name from intructor
/* The keyword all specifies that duplicates should not be removed */
```

```sql
SELECT * FROM table_name WHERE ... AND ...;
```

### 删除字段

```sql
ALTER TABLE table_name DROP COLUMN column_name;
```

### 建立索引

```sql
CREATE INDEX index_name ON table_name (column_name);
```

### 删除索引

```sql
DROP INDEX index_name ON table_name;
```

### 建立视图

```sql
CREATE VIEW view_name AS SELECT column_name FROM table_name WHERE ...;
```

### 删除视图
```sql
DROP VIEW view_name;
```

### 删除数据
```sql
DELETE FROM table_name WHERE ...;
```

## 进阶操作

### 条件更新

```sql
update instructor
	set salary = case
		when salary <= 100000 then salary * 1.05
		else salary * 1.03
		end
```

```sql
update student S
set tot_cred = (select sum(credits)
				from takes, course
				where takes.course_id = course.course_id and S.ID = takes.ID and takes.grade <> 'F' and takes.grade is not null)
```

### 标量子查询
- 返回单个查询结果

```sql
select dept_name,
	(select count(*)
	from instructor 
	where department.dept_name = instructor.dept_name)
	as num_instructors
from department;
```

### With 字句

```sql
with max_budget(value) as
	(select max(budget)
	from department)
select department.name
from department, max_budget
where department.budget = max_budget.value
```

- Complex example

```sql
with dept_total (dept_name, value) as
	(select dept_name, sum(salary)
	from instructor
	group by dept_name),
dept_total_avg(value) as
	(select avg(value)
	from dept_total)
select dept_name
from dept_total, dept_total_avg
where dept_total.value > dept_total_avg.value;
```

### From子查询

```sql
select dept_name, avg_salary
from(select dept_name, avg(salary) as avg_salary
	from instructors
	group by dept_name)
where avg_salary > 42000;

select dept_name, avg_salary
from (select dept_name, avg(salary)
	from instructor
	group by dept_name)
	as dept_avg(dept_name, avg_salary)
where avg_salary > 42000;
```


### 集合运算

```sql
(select course_id from section where sem='Fall' and year = 2017) union (select course_id from section where sem='Spring' and year = 2018)
/* Find courses that ran in Fall 2017 or in Spring 2017*/

(select course_id from section where sem ='Fall' and year = 2017) intersect (select course_id from section where sem='Spring' and year =2018)
/*Find courses that ran in Fall 2017 and in Spring 2018*/

(select course_id from section where sem = 'Fall' and year = 2017) except (select course_id from section where sem='Spring' and year = 2018)
/* Find courses that ran in Fall 2017 but not in Spring 2018*/
union (all)

select distinct course_id from section where semester = 'Fall' and year = 2017 and course_id in\not in(select course_id from section where semester= 'Spring' and year = 2018);

select name from instructor  where salary > some/all (select salary from instructor where dept_name = 'Biology')

exits 判断集合是否有值
unique 判断集合的值是否有重复
```

### 字符串匹配运算

- percent (%). The % character matches any substring.
- underscore (_). The _ character matches any character. 

```sql
select name from instructor where name like '%dar%'
/* Find the names of all instructors whoes name includes the substring 'dar' */
like '100 \%' escape '\'
/*Match the string '100%'*/

'Intro%' /* matches any string beginning with 'Intro' */
'___' /*matches any string of exactly three characters.*/
'___%' /* matches any string of at least three characters*/
```

### 重命名
```sql
select distinct T.name from instructor as T, instructor as S where T.salary > S.salary and S.dept_name = 'Comp. Sci.'
```

### 分类COUNT
```sql
SELECT department, COUNT(*) AS num_employees FROM employees GROUP BY department;
```

### 跨表查询
```sql
SELECT title FROM book t1 WHERE EXISTS ( SELECT * FROM borrow t2 WHERE t1.bno = t2.bno);
```
### 排序
```sql
SELECT * FROM table_name ORDER BY column_name ASC/DESC;
```

### 添加约束
添加主键
```sql
ALTER TABLE table_name ADD CONSTRAINT constraint_name PRIMARY KEY (column_name);
```

添加外键(级联删除和级联更新)

```sql
ALTER TABLE table_name ADD CONSTRAINT constraint_name FOREIGN KEY (column_name) REFERENCES referenced_table_name(referenced_column_name) ON DELETE CASCADE ON UPDATE CASCADE;
```

自连接

```sql
create table person(
	ID ...,
	name ...,
	mother ...,
	father ...,
	primary key ID,
	foreign key father reference person,
	foreign key mother reference person
)
```

添加内容约束
```sql
ALTER TABLE table_name ADD CONSTRAINT constraint_name CHECK (column_name > 0);
```
### 添加触发器
定义结束符,用于命令行的程序书写
```sql
DELIMITER $$
```

定义触发器
```sql
CREATE TRIGGER trigger_name BEFORE INSERT ON table_name 
    FOR EACH ROW 
BEGIN
    DECLARE var_name TYPE;
    IF condition THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'message';
    END IF;
END$$
```

恢复分号结束符
```sql
DELIMITER ;
```

- Example:
```sql
create trigger credits_earned after update of takes on (grade)
referencing new row as nrow 
referencing old row as orow 
for each row
when nrow.grade <> 'F' and nrow.grade is not null
	and (orow.grade = 'F' or orow.grade is null)
begin atomic
	update student
	set tot_cred= tot_cred + 
		(select credits
		from course
		where course.course_id = nrow.course_id)
	where student.id = nrow.id
end;
```

## 检查
创建条件检查
```sql
create assertion <assertion-name> check (<predicate>);
```

## 权限控制
### 创建用户
```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';
```
### 给予权限
```sql
revode <privilege list> on <relation or view> from <user list>
```
- All privileges that depend on the privilege being revoked are also revoked.

```sql
grant <privilege list>
on <relation or view> to <user list>

create role <name>
grant <role> to users
```

### 撤销权限
```sql
REVOKE ALL PRIVILEGES ON db_name.* FROM 'username'@'host';
```

## 聚合函数
- avg\min\max\sum\count
- group by
```sql
select dept_name, avg(salary) as avg_salary from instructor group by dept_name having avg(salary) > 42000;
/*predicates in the having clause are applied after the formation of groups whereas predicates in the where clause are applied before forming groups*/
```

## 高级SQL
### Embedded SQL

SQL的语句能够直接被编译，可以直接在代码中书写SQL语句

```C
EXEC-SQL connect to server user user-name using password;

:credit_amount // 可以辨别主机变量
EXEC SQL BEGIN DECLARE SECTION;
int credit_amount;
EXEC SQL END DECLARE SECTION;

EXEC SQL
	declare c cursor for
	select ID, name
	from student
	where tot_cred > :
END_EXEC

EXEC SQL open c;
EXEC SQL fetch c into :si, :sn END_EXEC;

EXEC SQL
	declare c cursor for
		select *
		from instructor
		where dept_name = 'Music'
		for update
// 遍历元组使用fetch
	update instructor
	set salary = salary + 1000
	where current of c

EXEC SQL <embedded SQL statement>;
```

### Dynamic SQL
能够连接到数据库，然后可以在运行期间提交SQL语句，与数据库交互.

#### ODBC(Open Database Connectivity)
- C\C++\C# and Visual Basic

#### JDBC(Java Database Connectivity)
- 获取返回字段

`rs.getString("dept_name") or rs.getString(1)`

- 处理空字段

`if (rs.wasNull())`

- 预准备语句
	- 可以载入不同参数
	- 防止SQL注入攻击
	- 使用`setString`
```sql
PreparedStatement pstmt = conn.prepareStatement("select * from dept where dept_no = ?");
```

- 事务管理
```sql
conn.setAutoCommit(false);
conn.commit();
conn.rollback();
```

### SQL函数
例子：

```sql
// 值返回
create function dept_count (dept_name varchar(20))
	return integer
	begin
	declare d_count integer;
		select count(*) into d_count
		from instructor
		where instructor.dept_name = dept_name
	return d_count;
end

// 表返回

create function instructor_of(dept_name char(20))
	returns table (
		ID varchar(5),
		name varchar(20),
		dept_name varchar(20),
		salary numeric(8,2))
	return table
		(select ID, name, dept_name, salary
		from instructor
		where instructor.dept_name = instructor_of.dept_name)


select * 
from table (instructor_of('Music'))
```

### SQL过程

```sql
create procedure dept_count_proc (in dept_name varchar(20),
	out d_count integer)
	begin
		select count(*) into d_count
		from instructor
		where instructor.dept_name = dept_count_proc.dept_name
	end
```

### Language Constructs

```sql
while boolean expression do
	sequence of statements;
end while

repeat
	sequence of statements;
until boolean expression
end repeat

declare n integer default 0;
for r as
	select budget from department
	where dept_name = 'Music'
do
	set n = n + r.budget
end for

if boolean expression
	then statement or compound statement
elseif boolean expression
	then statement or compound statement
else statement or compound statement
end if
```

