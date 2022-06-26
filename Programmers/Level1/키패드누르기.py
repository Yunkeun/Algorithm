def get_distance(current_position, to_press_position):
    if current_position < 4 and to_press_position > 3:
        return abs(current_position - (to_press_position - 4)) + 1
    if current_position > 3 and to_press_position < 4:
        return abs((current_position - 4) - to_press_position) + 1
    return abs(current_position - to_press_position)

def solution(numbers, hand):
    # setting
    answer = []
    left_possible_numbers = [1, 4, 7, '*', 2, 5, 8, 0]
    right_possible_numbers = [3, 6, 9, '#', 2, 5, 8, 0]
    current_left_position = 3
    current_right_position = 3
    for number in numbers:
        if number in left_possible_numbers:
            position = left_possible_numbers.index(number)
        else:
            position = right_possible_numbers.index(number)
        if position > 3:
            left_distance = get_distance(current_left_position, position)
            right_distance = get_distance(current_right_position, position)
            if left_distance > right_distance:
                answer.append("R")
                current_right_position = position
            elif left_distance < right_distance:
                answer.append("L")
                current_left_position = position
            else:
                if hand == "right":
                    answer.append("R")
                    current_right_position = position
                else:
                    answer.append("L")
                    current_left_position = position
            continue
        if number in left_possible_numbers:
            answer.append("L")
            current_left_position = position
            continue
        if number in right_possible_numbers:
            answer.append("R")
            current_right_position = position
    return ''.join(answer)