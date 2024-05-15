class Node:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None

class PolynomialLinkedList:
    def __init__(self):
        self.head = None

    def insert_term(self, coef, exp):
        new_node = Node(coef, exp)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def evaluate_addition(self):
        current = self.head
        result = {}
        while current is not None:
            if current.exp in result:
                result[current.exp] += current.coef
            else:
                result[current.exp] = current.coef
            current = current.next
        return result

    def evaluate_multiplication(self):
        current = self.head
        result = {}
        while current is not None:
            if current.exp in result:
                result[current.exp] *= current.coef
            else:
                result[current.exp] = current.coef
            current = current.next
        return result

# ساخت یک لیست لینکد لیست و افزودن توان‌ها و ضرایب
p = PolynomialLinkedList()
p.insert_term(2, 3)
p.insert_term(5, 2)
p.insert_term(1, 1)

# محاسبه جمع و ضرب
addition_result = p.evaluate_addition()
multiplication_result = p.evaluate_multiplication()

print("جمع چندجمله‌ای:")
print(addition_result)

print("\nضرب چندجمله‌ای:")
print(multiplication_result)