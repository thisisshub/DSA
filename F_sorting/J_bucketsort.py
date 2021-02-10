def method1(ll: list) -> list:
    def insertion_sort(bucket):
        for i in range(1, len(bucket)):
            var = bucket[i]
            j = i - 1
            while j >= 0 and var < bucket[j]:
                bucket[j + 1] = bucket[j]
                j = j - 1
            bucket[j + 1] = var

    def bucket_sort(input_list):
        
        max_value = max(input_list)
        size = max_value / len(input_list)

        
        buckets_list = []
        for x in range(len(input_list)):
            buckets_list.append([])

        
        for i in range(len(input_list)):
            j = int(input_list[i] / size)
            if j != len(input_list):
                buckets_list[j].append(input_list[i])
            else:
                buckets_list[len(input_list) - 1].append(input_list[i])

        
        for z in range(len(input_list)):
            insertion_sort(buckets_list[z])

        
        final_output = []
        for x in range(len(input_list)):
            final_output = final_output + buckets_list[x]
        return final_output

    return bucket_sort(ll)


if __name__ == "__main__":
    
    l = [1, 3, 4, 7, 5, 9]
    from timeit import timeit
    print(timeit(lambda: method1(l), number=10000)) 
    
