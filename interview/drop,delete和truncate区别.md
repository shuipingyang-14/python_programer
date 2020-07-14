* 用法
1. `drop`：`drop table` 表名

删除内容和定义，并释放空间

执行`drop`语句，将使此表的结构一起删除

2. `truncate` (清空表中的数据)：`truncate table` 表名

删除内容、释放空间但不删除定义(也就是保留表的数据结构)

与drop不同的是,只是清空表数据而已

`truncate`不能删除行数据，虽然只删除数据，但是比`delete`彻底，它只删除表数据

3. `delete`：`delete from` 表名 （`where` 列名 = 值）

与`truncate`类似，`delete`也只删除内容、释放空间但不删除定义

但是`delete`即可以对行数据进行删除，也可以对整表数据进行删除

* `delete`和`truncate`删除操作

1. `delete from` 语句执行删除过程是每次从表中删除一行，并且同时将该行的删除操作作为事务及在日志中保存一边进行回滚操作

2. `truncate table` 一次性从表中删除所有的数据并不把单独的删除操作记入日志保存，删除行不能恢复，删除过程中不会激活鱼与表有关的触发器，删除速度快

* 表和索引所占空间

1. 当表被`truncate`后，这个表和索引所占的空间会恢复到初始大小
2. `delete`操作不会减少表或者索引所占空间
3. `drop`语句将表所占用的空间全释放掉

* 执行速度：drop>truncate>delete

* 应用范围：
1. `truncate` 只能对`table`操作
2. `delete`可以是`table`和`view`操作

* `truncate` 和`delete`只删除数据， `drop`则删除整个表（结构和数据）

* `truncate`与不带`where`的`delete` ：只删除数据，而不删除表的结构（定义）

* `drop`语句将删除表的结构被依赖的约束（constrain),触发器（trigger)索引（index);依赖于该表的存储过程/函数将被保留，但其状态会变为：invalid

* `delete`语句为DML（data maintain Language),这个操作会被放到 rollback segment中,事务提交后才生效，如果有相应的 tigger,执行的时候将被触发

* `truncate`、`drop`是DLL（data define language),操作立即生效，原数据不放到 rollback segment中，不能回滚

* 在没有备份情况下，谨慎使用 `drop` 与 `truncate`，要删除部分数据行采用`delete`且注意结合`where`来约束影响范围，回滚段要足够大；要删除表用drop；若想保留表而将表中数据删除，如果和事务无关，用truncate即可实现；如果和事务有关，或老师想触发trigger,还是用delete

* `truncate table` 表名 速度快,而且效率高

`truncate table` 在功能上与不带 `where` 子句的 `delete` 语句相同：二者均删除表中的全部行，但 `truncate table` 比 `delete` 速度快，且使用的系统和事务日志资源少

`delete` 语句每次删除一行，并在事务日志中为所删除的每行记录一项

`truncate table` 通过释放存储表数据所用的数据页来删除数据，并且只在事务日志中记录页的释放

* `truncate table` 删除表中的所有行，但表结构及其列、约束、索引等保持不变

新行标识所用的计数值重置为该列的种子

如果想保留标识计数值，请改用 `delete`

如果要删除表定义及其数据，请使用 `drop table` 语句

* 对于有外键约束引用的表，不能使用 `truncate table`，而应使用不带 `where` 子句的 `delete` 语句

由于 `truncate table` 不记录在日志中，所以它不能激活触发器


一、`delete`

1、`delete`是DML，执行`delete`操作时，每次从表中删除一行，并且同时将该行的的删除操作记录在`redo`和`undo`表空间中以便进行回滚（rollback）和重做操作，但要注意表空间要足够大，需要手动提交（commit）操作才能生效，可以通过rollback撤消操作

2、`delete`可根据条件删除表中满足条件的数据，如果不指定`where`子句，那么删除表中所有记录

3、`delete`语句不影响表所占用的`extent`，高水线(high watermark)保持原位置不变

二、`truncate`

1、`truncate`是DDL，会隐式提交，所以，不能回滚，不会触发触发器

2、`truncate`会删除表中所有记录，并且将重新设置高水线和所有的索引，缺省情况下将空间释放到`minextents`个`extent`，除非使用`reuse storage`，不会记录日志，所以执行速度很快，但不能通过rollback撤消操作（如果一不小心把一个表truncate掉，也是可以恢复的，只是不能通过rollback来恢复）

3、对于外键（foreignkey ）约束引用的表，不能使用 `truncate table`，而应使用不带 `where` 子句的 `delete` 语句

4、`truncate table`不能用于参与了索引视图的表

三、`drop`

1、`drop`是DDL，会隐式提交，所以，不能回滚，不会触发触发器

2、`drop`语句删除表结构及所有数据，并将表所占用的空间全部释放

3、`drop`语句将删除表的结构所依赖的约束，触发器，索引，依赖于该表的存储过程/函数将保留,但是变为invalid状态