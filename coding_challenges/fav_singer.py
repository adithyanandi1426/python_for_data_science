from collections import defaultdict

def count_favorite_singers(num_songs, singers):
    singer_count = defaultdict(int)
    max_count = 0
    
    # Count occurrences of each singer
    for singer in singers:
        singer_count[singer] += 1
        max_count = max(max_count, singer_count[singer])
    
    # Count how many singers have the maximum count
    favorite_singers_count = sum(1 for count in singer_count.values() if count == max_count)
    
    return favorite_singers_count

# Read input
num_songs = int(input().strip())
singers = list(map(int, input().strip().split()))

# Calculate and print the result
result = count_favorite_singers(num_songs, singers)
print(result)
