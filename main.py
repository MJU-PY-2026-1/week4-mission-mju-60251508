# 파일이름 : main.py
# 작 성 자 : mju-3-31
# 도장깨기 맛집리스트

#비어있는 리스트 만들기
bucket_list = []
restaurant1 = input('맛집 리스트 입력: ')
bucket_list.append(restaurant1)

restaurant2 = input('맛집 리스트 입력: ')
bucket_list.append(restaurant2)

restaurant3 = input('맛집 리스트 입력: ')
bucket_list.append(restaurant3)

print(f'리스트 : {bucket_list}')

vip_restaurant = input('맛집 리스트 추가: ')
bucket_list.insert(0, vip_restaurant)

print(f'리스트 : {bucket_list}')


visited_restaurant = input('도장깨기 : ')
bucket_list.remove(visited_restaurant)

print(f'리스트 : {bucket_list}')


