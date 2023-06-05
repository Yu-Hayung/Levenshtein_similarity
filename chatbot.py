import numpy as np
import pandas as pd
import Levenshtein


questions = []
answers = []

# CSV 파일 경로를 지정하세요.
filepath = 'ChatbotData.csv'

data = pd.read_csv(filepath)
questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
answers = data['A'].tolist()  # 답변열만 뽑아 파이썬 리스트로 저장

def find_best_answer(input_sentence):
    min_distance = float('inf')
    best_match_index = -1

    for i, question in enumerate(questions):
        distance = Levenshtein.distance(input_sentence, question)
        if distance < min_distance:
            min_distance = distance
            best_match_index = i

    return answers[best_match_index]





# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = find_best_answer(input_sentence)
    print('Chatbot:', response)
    
