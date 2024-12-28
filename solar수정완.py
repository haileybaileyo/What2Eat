# 필요한 패키지 설치
!pip install openai==0.28.0

import openai

# API 키와 사용자 지정 Base URL 설정
openai.api_key = "up_JB2rvyvOIYlmdY94cOh8z9h9JzwfP"
openai.api_base = "https://api.upstage.ai/v1/solar"

# 초기 시스템 메시지와 사용자 메시지 설정
messages = [
    {
        "role": "system",
        "content": "당신은 스위치온 다이어트 전문가입니다. 다이어트 방법과 허용식품에 대해 조언해주세요."
    },
]

def send_message(text):
    """메시지를 보내고 응답을 받는 함수"""
    messages.append({"role": "user", "content": text})
    try:
        response = openai.ChatCompletion.create(
            model="solar-1-mini-chat",
            messages=messages,
            stream=False
        )
        
        # 응답에서 올바른 내용을 가져오기
        assistant_response = response.choices[0].message["content"]
        messages.append({"role": "assistant", "content": assistant_response})
        return assistant_response
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return "죄송합니다. 오류가 발생했습니다. 다시 시도해주세요."

def main():
    """메인 대화 루프"""
    print("스위치온 다이어트 챗봇을 시작합니다. 종료하려면 'exit'를 입력하세요.")
    try:
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() == "exit":
                print("\n대화를 종료합니다. 좋은 하루 되세요!")
                break
            
            response = send_message(user_input)
            print("\nAssistant:", response)
            
    except KeyboardInterrupt:
        print("\n\n대화가 중단되었습니다. 안녕히 가세요!")
    except Exception as e:
        print(f"\n예기치 않은 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
