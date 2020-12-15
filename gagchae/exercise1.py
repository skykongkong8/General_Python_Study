class Node:
    """노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.next = None
    """생성 시의 next 관계는 None으로 한다."""

"""Node 클래스 인스턴스 생성"""
head_node = Node(2)
node1 = Node(3)
tail_node =Node(5)

"""링크드 리스트 next 관계 형성"""
head_node.next = node1
node1.next = tail_node

"""연쇄적 출력"""
iterator = head_node
while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

class Linked_List:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head=None
        self.tail = None

    def __str__(self):
        """예쁘게 str으로 출력해주는 str메소드"""
        res_str = "|"
        iterator = self.head
        while iterator is not None:
            res_str += f"{iterator.data}|"
            iterator = iterator.next
        return res_str

    def append(self, data):
        """새로운 링크드 리스트를 형성할 때"""
        new_node = Node(data)
        """링크드 리스트가 비어있을 경우: 하나만 넣으므로 처음과 끝이 같을 것임"""
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            """링크드 리스트가 비어있지 않을 경우, 먼저 tailnode를 와 newnode를 이어준 후, tail node의 위치를 바꾸어준다"""
            self.tail.next = new_node
            self.tail = new_node
    
    def find_node_at(self, index):
        """접근하는 메소드"""
        iterator = self.head
        for i in range(index):
            iterator = iterator.next
        return iterator
    def find_node_with_data(self, data):
        """인덱스가 아닌 데이터로 접근하는 메소드"""
        iterator = self.head
        while iterator.data is not data:
            iterator = iterator.next
            if iterator is None:
                return None
        return iterator

    def insert_after(self, previous_node, data):
        new_node = Node(data)
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node



            
            



"""링크드 리스트의 연쇄적 출력하기"""
my_list = Linked_List()

my_list.append(2)
my_list.append(3)
my_list.append(5)

print(my_list)

next_should_be_numero_4 = my_list.find_node_at(1)
print(next_should_be_numero_4) #뭐야 그냥 data위치로 나오네? 뭐지

my_list.insert_after(next_should_be_numero_4,4)

print(my_list)