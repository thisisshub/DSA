# import math as mt
def ternary(l, r, key, arr):
    if (r >= l):
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if (arr[mid1] == key):
            return mid1

        if (arr[mid2] == key):
            return mid2

        if (key < arr[mid1]):

            return ternary(l, mid1 - 1, key, arr)

        elif (key > arr[mid2]):
            return ternary(mid2 + 1, r, key, arr)
        else:
            return ternary(mid1 + 1, mid2 - 1, key, arr)

    return "not present"

if __name__ == "__main__":
    print("Enter the elements of the array : ")
    arr= list(map(int,input().strip().split()))
    l, r= 0,len(arr)-1
    key = int(input("Enter the element to be found : "))
    ans = ternary(l, r, key, arr)
    print("Index of", key, "is", ans)
