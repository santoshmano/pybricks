

class ResizableArray:

  def __init__(self, size=8):
    self.items = [0 for _ in range(size)]
    self.size = size

  def size():
      return self.size

  def set(index, item):
    if index <0 or index>size:
        those exception array out of bounds
    items[size] = item
    size++

  def append(int item):
    ensure_extra_capacity();
    items[size] = item
    size++

  def ensure_extra_capacity()
    if (size == items.length):
      new_array = [size *2]
      new_array = copy(self.items, )
      self.items = new_array
  
  def get(int index)
    if index <0 or index>size:
        those exception array out of bounds

    return self.items[index]