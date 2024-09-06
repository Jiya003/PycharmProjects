def merge_the_tools(string, k):
    # your code goes here
    s=string
    l=[]
    len_l=0
    for i in s:
        len_l=len_l+1
        if i not in l:
            l.append(i)
        if len_l==k:
            print(''.join(l))
            len_l=0
            l=[]



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)