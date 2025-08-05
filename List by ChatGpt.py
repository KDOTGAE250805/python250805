# 데이터 정의
my_list = [1, 2, 2, 3]
my_set = {1, 2, 2, 3}
my_dict = {'a': 1, 'b': 2}
my_tuple = (1, 2, 2, 3)

# 출력 비교
print("List :", my_list)   # [1, 2, 2, 3] - 중복 허용, 순서 있음
print("Set  :", my_set)    # {1, 2, 3} - 중복 제거, 순서 없음
print("Dict :", my_dict)   # {'a': 1, 'b': 2} - 키-값 구조, 순서 있음 (3.7 이상)
print("Tuple:", my_tuple)  # (1, 2, 2, 3) - 변경 불가능한 리스트 느낌

# 타입 확인
print("\n--- 타입 확인 ---")
print("List  type:", type(my_list))
print("Set   type:", type(my_set))
print("Dict  type:", type(my_dict))
print("Tuple type:", type(my_tuple))

# 주요 연산 비교
print("\n--- 주요 연산 예시 ---")

# List
my_list.append(4)
print("List append:", my_list)

# Set
my_set.add(4)
print("Set add    :", my_set)

# Dict
my_dict['c'] = 3
print("Dict add   :", my_dict)

# Tuple (불변 → 새로운 튜플로 만들어야 함)
my_tuple += (4,)
print("Tuple add  :", my_tuple)

# 멤버 확인
print("\n--- 포함 여부 확인 ---")
print("2 in list:", 2 in my_list)
print("2 in set :", 2 in my_set)
print("'a' in dict:", 'a' in my_dict)
print("2 in tuple:", 2 in my_tuple)
