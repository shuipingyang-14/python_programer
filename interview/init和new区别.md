* ��ͬ��
���߾���python������������еĺ�����__new__�Ƚ����ã�__init__ʹ�õĽ϶�

* ��ͬ��
1. __init__�ǵ�ʵ�����󴴽���ɺ󱻵��õģ����ö������Ե�һЩ��ʼֵ��ͨ�����ڳ�ʼ��һ����ʵ����ʱ����һ��ʵ������
2. __new__ʫ��ʵ������֮ǰ���ã���Ϊ���������Ǵ���ʵ��Ȼ�󷵻�ʵ��������һ����̬����
3. __new__�ֱ����ã�__init__�󱻵��ã�__new__�ķ���ֵ��ʵ���������ݸ�__init__�����ĵ�һ��������Ȼ��__init__�����ʵ�����ò���

```python
class Book(object):
    def __new__(cls, title):
        print('this is __new__')
        return super(Book, cls).__new__(cls)

    def __init__(self, title):
        print('this is __init__')
        super(Book, self).__init__()
        self.title = title

b = Book('this python book...')
print(b.title)


# �����
# this is __new__
# this is __init__
# this python book... 
```

* �ر�˵��
1. �̳�object����ʽ�����__new__
2. __new__������һ������cls������ǰ�࣬�˲���ʵ����ʱ��python�������Զ�ʶ��
3. __new__����Ҫ�з���ֵ������ʵ����������ʵ��������return���ࣨͨ��super(��ǰ����, cls)��__new__������ʵ��������ֱ����object��__new__������ʵ��
4. __init__��һ������self��__new__���ص�ʵ����__init__��__new__�Ļ����Ͽ������һЩ������ʼ���Ķ�����__init__����Ҫ����ֵ
5. ���__new__�������ǵ�ǰ���ʵ�������Զ�����__init__������ͨ��return���������õ�__new__�����ĵ�һ������cls��֤�ǵ�ǰ��ʵ����������������������ʵ�ʴ������صľ����������ʵ������ʵ������õ�ǰ���__init__������Ҳ��������������__init__����
6. �ڶ�������ʱû�����¶���__new__()ʱ��pythonĬ�ϵ��ø����ֱ�Ӹ����__new__()��������������ʵ�����������ĸ���Ҳû����д__new__()������һֱ���˹���׷�ݵ�object��__new__()��������Ϊobject��������ʽ��Ļ���
7. ���������д��__new__()��������������ѡ������һ����������ʽ�ࣨ��������ʽ�ֻ࣬����ʽ��ض���__new__()��������ʽ����object�������������û��__new__()����)��__new__()��������ʵ����������ʽ�������ǰ����ͺ���ֻ࣬Ҫ�����ɵݹ���ѭ��
8. ���������__init__�����ù����__new__һ�£��������͸����__init__����������ã������������__init__�����м���Ը���__init__�����ĵ���
9. ����ʹ��__init__��������Ҫȥ�Զ���__new__��������Ϊ�������ڼ̳�����ʱ�����Ի��Ǻܲ�һ����
10. ������������̣�__new__��������ǰ�ڵ�ԭ���Ϲ��򻷽ڣ�__init__������������ԭ���ϵĻ����ϣ��ӹ�����ʼ����Ʒ����

* __init__����
```python
class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
```
* __new__����
__new__������__init__�Ĳ���һ����__init__����ʵ����������ã�__new__�Ǵ�����ʵ���ķ���
```python
class Person(object):
    def __new__(cls, name, age):
        print('this is __new__')
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print('this is the __init__')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' %(self.name, self.age)

if __name__ == '__main__':
    p = Person('zhangsan', 18)
    print(p)
    
# ���
# this is __new__
# this is the __init__
# <Person: zhangsan(18)>

# ִ���߼���
"""
1. p = Person(name, age)
2. ����ִ��ʹ��name��age������ִ��Person���__new__���������__new__�����᷵��Person���һ��ʵ����ͨ���������ʹ�� super(Persion, cls).__new__(cls) �����ķ�ʽ��
3. Ȼ���������ʵ�����������__init__��������һ������__new__������ʵ��Ҳ���� __init__����ĵ� self
"""
```

* __init__��__new__��Ҫ������
1. __init__ͨ�����ڳ�ʼ��һ����ʵ�������Ƴ�ʼ���Ĺ��̣��������һЩ���ԣ���һЩ�����������������ʵ����������ɺ���ʵ������ķ���
2. __new__ͨ�����ڿ�������һ����ʵ�����̣����༶��ķ���

* __new__���ã�
__new__�ǵ��̳�һЩ���ɱ��classʱ(����int,str,tuple)���ṩһ���Զ�����ʵ�������̵�;����ʵ���Զ����metaclass
```python
class PositiveInterger(int):
    def __new__(cls, value):
        return super(PositiveInterger, cls).__new__(cls, abs(value))
        
i = PositiveInterger(-3)
print(i)
```