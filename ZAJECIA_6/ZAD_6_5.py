import random

# create nested list
def nested_list(depth = 5, max_elements = 3,  max_value = 5):
    if 'nest_list' not in locals():
        nest_list = []
    if depth == 0: # stop nesting
        return random.randint(0,max_value)
    for _ in range(random.randint(1,max_elements)):
        nest_list.append(nested_list(depth-1,max_elements, max_value))
    return nest_list

def nested_sum(nested_list: list):
    sum = 0
    for element in nested_list:
        if isinstance(element, int):
            sum += element
        else:
            sum += nested_sum(element)
    return sum


def main():
    example = nested_list(3,2,5)
    print(example)
    print(nested_sum(example))



if __name__ == "__main__":
    main()