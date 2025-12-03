test_input= "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
input = "199617-254904,7682367-7856444,17408-29412,963327-1033194,938910234-938964425,3207382-3304990,41-84,61624-105999,1767652-1918117,492-749,85-138,140-312,2134671254-2134761843,2-23,3173-5046,16114461-16235585,3333262094-3333392446,779370-814446,26-40,322284296-322362264,6841-12127,290497-323377,33360-53373,823429-900127,17753097-17904108,841813413-841862326,518858-577234,654979-674741,773-1229,2981707238-2981748769,383534-468118,587535-654644,1531-2363"

def main():
    invalid_ids_count = 0
    id_ranges = input.split(",")
    
    for id_range in id_ranges:
        first_id, last_id = id_range.split("-")
        
        for num in range(int(first_id), int(last_id) + 1):
            id_str = str(num)
            
            for length in range(1,  len(id_str) // 2 + 1):
                if len(id_str) % length == 0:
                    parts = [id_str[i:i+length] for i in range(0, len(id_str), length)]
                    if all(part == parts[0] for part in parts):
                        invalid_ids_count += num
                        break
                
    print(f"Total invalid IDs: {invalid_ids_count}")
                
if __name__ == "__main__":
    main()
