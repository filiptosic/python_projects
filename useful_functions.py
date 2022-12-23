
#takes in a list, and returns only unique elements from it
def unique(list):
    return list(set(list))
    
#takes in a list converts it to unique values. Returns dictionary of keys representing the unique elements, and values containing the count
def count_elements(arr):
    if type(arr) == list:
        unique_elements = list(set(arr))
        count_dict = {}
        for element in unique_elements:
            count_dict[element] = 0
        for element in arr:
            if element in unique_elements:
                count_dict[element] += 1
        return count_dict
    else:
        return f'Function argument must be list, not {type(arr)}'

#unpacks a nested list and counts the elements. Returns dictionary of keys representing the unique elements, and values containing the count
def count_elements_nested(arr):
    if type(arr) == list:
        count_dict = {}
        unnested = []
        for elements in arr:
            if type(elements) == list:
                for element in elements:
                    unnested.append(element)
            else:
                unnested.append(elements)
        unique_elements = list(set(unnested))
        for each in unique_elements:
            count_dict[each] = 0
        for element in unnested:
            if element in unique_elements:
                count_dict[element] += 1
        return count_dict
    else:
        error = type(arr)
        return f'Function argument must be list, not {error}'