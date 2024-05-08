#یونس خیالی صبری تمرین ساختمان داده
def get_item(self, index):
    if index >= self.num:
        raise IndexError("Index out of range")
    return self.Q[(self.first + index) % self.max_size]
