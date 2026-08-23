 

def max_sub_string(arr):

    sor_list = []
    best_list =[]
    max_count = 0

    for char in arr:
        while char in sor_list:
            sor_list.pop(0)
        sor_list.append(char)

        if len(sor_list) > max_count:
            max_count = len(sor_list)
            best_list = sor_list.copy()
    print("The best substring:","".join(best_list))
    return max_count


if __name__ == "__main__":
    st = "addbcewfswsss"
    x = max_sub_string(st)
    print(x)
    