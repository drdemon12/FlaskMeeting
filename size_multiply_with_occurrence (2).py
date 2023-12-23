'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


def find_max(t,z):
    t_length = len(t)
    z_length = len(z)
    result = -1
    substrings = []

    for i in range(t_length):
        for j in range(i + 1, t_length + 1):
            substrings.append(t[i:j])

    for substring in substrings:
        count = 0
        start_index = 0
        while start_index < z_length:
            index = z.find(substring, start_index)
            if index != -1:
                count += 1
                start_index = index + 1
            else:
                break
        if count > 0:
            result = max(result, len(substring) * count)

    print(result)
    return result


if __name__ == '__main__':
    find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")