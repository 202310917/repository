import os
import struct

def input_scores():
    print('[점수 입력]')
    scores = []
    while True:
        score = int(input(f"#{len(scores) + 1}? "))
        if score < 0:
            break
        scores.append(score)
    return scores
def get_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def show_scores(scores):
    print('[점수 출력]')
    scores_str = ""
    for score in scores:
        scores_str += str(score) + " "
    print("개인점수:", scores_str.rstrip())

def save_scores(scores):
    with open("score.bin", "wb") as file:
        for score in scores:
            file.write(struct.pack('i', score))

def load_scores():
    with open("score.bin", "rb") as file:
        scores = []
        while True:
            data = file.read(4)
            if not data:
                break
            score = struct.unpack('i', data)[0]
            scores.append(score)
        show_scores(scores)


if os.path.exists("score.bin"):
    load_scores()
else :
    scores = input_scores()
    show_scores(scores)
    average = get_average(scores)
    print(f"평균: {average:.1f}")
    save_scores(scores)


