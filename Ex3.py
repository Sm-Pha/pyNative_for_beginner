
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_size = len(sample_list)//3

for i in range(0, len(sample_list), chunk_size):
    list_chunked = sample_list[i: i + chunk_size]
    print(f"Chunk : {list_chunked}")

    list_chunked.reverse()
    print(f"After reversing it  {list_chunked}")
#     #step 3 (0-3)
#     #step 3 (3-6)
#     #step 3 (6-12)
