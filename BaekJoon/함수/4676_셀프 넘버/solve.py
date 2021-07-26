def get_generated_num(generated_num):
    for num in range(1, 10001):
        for each_num in str(num):
            num += int(each_num)
        generated_num.add(num)
    return generated_num

def get_self_num(generated_num):
    natural_num = set(range(1, 10001))
    self_num = sorted(natural_num - generated_num)
    for i in self_num:
        print(i)

set_num = set()
generated_num = get_generated_num(set_num)
get_self_num(generated_num)