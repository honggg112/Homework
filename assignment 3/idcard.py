number = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
code_map = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
def verify_id_card(id_card):
    total_sum = sum(int(id_card[i]) * number[i] for i in range(17))
    return "YES" if code_map[total_sum % 11] == id_card[-1].upper() else "NO"

n= int(input())
for _ in range(n):
    print(verify_id_card(input().strip()))
