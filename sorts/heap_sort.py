# есть бинарное дерево
# есть пирамида подвид бинарного дерева -> heap, она же куча

# пирамида по максимуму: родитель всегда больше своих детей

# родитель индекс i имеет индекс (i-1) // 2
# по индексу получить детей: 2i + 1, 2i + 2


# как изменить элемент в куче? меняем значение, а дальше меняем его с максимальным из детей -> просеивание вниз

# import math

# def gen_padding(pad_len, min_pad):
#     return min_pad*pad_len

# def show_heap(heap):
#     n = len(heap)
#     num_layers = int(math.log2(n))
#     min_padding = '  '

#     for layer in range(num_layers):
#         print()

from copy import deepcopy

def get_left_child(i):
    return 2*i + 1

def get_right_child(i):
    return 2*i + 2

def get_parent(i):
    return (i - 1) // 2

def swap(i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]

example_heap = [15,9,14,7,8,7,13,4,6,7,5]
# print(example_heap)


def sift_down(heap, i):
    '''Если элемент уменьшился то просеиваем вниз'''
    size = len(heap)

    left_child_ind = get_left_child(i)
    right_child_ind = get_right_child(i)
    largest = i

    if (left_child_ind < size) and (heap[left_child_ind] > heap[largest]):
        largest = left_child_ind

    if (right_child_ind < size) and (heap[right_child_ind] > heap[largest]):
        largest = right_child_ind

    if largest != i:
        swap(i, largest, heap)
        sift_down(heap, largest)

    return

def sift_up(heap, i):
    '''Если элемент уменьшился то просеиваем вниз'''
    size = len(heap)

    parent_ind = get_parent(i)
    if i > 0 and heap[parent_ind] < heap[i]:
        swap(i, parent_ind, heap)
        sift_up(heap, parent_ind)

    return
    
def convert_to_heap(arr):
    '''
    идея: пирамида из одного элемента корректна
    добавим один элемент, и просеем его вниз
    '''
    arr_copy = deepcopy(arr)
    size = len(arr_copy)
    # те у кого нет детей являются листьями.
    # то есть те, у кого, 2*i + 1 > len(arr_copy)
    # т.е. i > (size - 1) / 2 являются листьями
    # пойдем получается от (size - 1) // 2 до нуля
    for i in reversed(range((size - 1) // 2 + 1)):
        sift_down(arr_copy, i)
    
    return arr_copy
    
def heap_sort(arr):
    '''
    идея:
    меняем верхний элемент с последним в пирамиде, отправляем верхний в конец отсортированного массива
    затем делаем sift down для того что оказалось сверху. Повторяем
    '''

# print(example_heap)
# example_heap[1] = 0
# sift_down(example_heap, 1)
# print(example_heap)

arr = [i for i in range(10)]
print(arr)

print(convert_to_heap(arr))


# def validate(heap, i):

#     n = len(heap)

#     left_ind = get_left_child(i)
#     right_ind = get_right_child(i)

#     if (left_ind < n) and (heap[left_ind] > heap[i]):
#         return False

#     if (right_ind < n) and (heap[right_ind] > heap[i]):
#         return False
    
#     left_correct = 
