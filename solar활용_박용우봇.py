!pip install openai==1.2.0

import openai

# API 키와 사용자 지정 Base URL 설정
openai.api_key = "up_JB2rvyvOIYlmdY94cOh8z9h9JzwfP"
openai.api_base = "https://api.upstage.ai/v1/solar"

# 초기 시스템 메시지와 사용자 메시지 설정
messages = [
    {
        "role": "system",
        "content": "당신은 박용우 스위치온 다이어트 전문가입니다. 스위치온 다이어트 방법과 허용식품에 대해 조언해주세요."
    },
]

def send_message(text):
    messages.append({"role": "user", "content": text})
    response = openai.ChatCompletion.create(
        model="solar-1-mini-chat",
        messages=messages,
        stream=False
    )

    # 응답에서 올바른 내용을 가져오기
    assistant_response = response.choices[0].message["content"]
    messages.append({"role": "assistant", "content": assistant_response})
    return assistant_response

try:
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Conversation ended.")
            break
        response = send_message(user_input)
        print("Assistant:", response)
except KeyboardInterrupt:
    print("\nConversation ended by user.")
