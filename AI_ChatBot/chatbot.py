# 필요한 패키지 설치
!pip install openai==0.28.0

import openai
from typing import List, Dict, Optional
import json

# API 설정
openai.api_key = "up_JB2rvyvOIYlmdY94cOh8z9h9JzwfP"
openai.api_base = "https://api.upstage.ai/v1/solar"

class DietPhase:
    def __init__(self, phase_num, days, title, goal, guidelines, allowed_foods, restrictions, fasting_rule=None):
        self.phase_num = phase_num
        self.days = days
        self.title = title
        self.goal = goal
        self.guidelines = guidelines
        self.allowed_foods = allowed_foods
        self.restrictions = restrictions
        self.fasting_rule = fasting_rule

class DietKnowledgeBase:
    def __init__(self):
        self.phases = self.initialize_phases()  # _initialize_phases를 initialize_phases로 변경
        self.general_rules = {
            "supplements": ["유산균", "종합비타민", "오메가3", "비타민C", "CoQ10"],
            "exercise": "하루 60분 이상 걷기",
            "prohibited_foods": [
                "설탕류(정백당, 액상과당)",
                "청량음료",
                "커피믹스",
                "과자",
                "도넛",
                "아이스크림",
                "주스",
                "당분이 첨가된 우유/두유",
                "밀가루 음식(빵, 케이크, 파스타, 라면)",
                "술",
                "포화지방이 많은 음식(삼겹살, 갈비, 곱창)",
                "트랜스지방이 많은 음식",
                "짠 음식(소금, 양념장, 젓갈류)"
            ]
        }

    def initialize_phases(self):  # _initialize_phases를 initialize_phases로 변경
        return {
            1: DietPhase(
                phase_num=1,
                days="1-3일차",
                title="지방 대사 스위치 켜기",
                goal="장 휴식과 생체리듬 개선",
                guidelines=[
                    "하루 4번(아침, 점심, 오후간식, 저녁) 단백질 음료 섭취",
                    "아침 공복에 유산균 섭취",
                    "하루 60분 이상 걷기",
                    "물 또는 무가당 두유만 허용",
                    "카페인 섭취 금지"
                ],
                allowed_foods=[
                    "단백질 셰이크",
                    "녹황색 채소",
                    "두부",
                    "코코넛 오일",
                    "올리브 오일",
                    "무가당 플레인요거트",
                    "녹차",
                    "허브티",
                    "양파", "마늘", "고춧가루", "식초", "후추", "강황", "허브",
                    "양배추", "무", "당근", "오이", "브로콜리", "파프리카",
                    "아보카도",
                    "연두부",
                    "무가당 두유"
                ],
                restrictions=[
                    "물 또는 무가당 두유 외 다른 음료 제한",
                    "카페인 섭취 금지",
                    "커피 섭취 금지",
                    "심한 허기 시에만 허용 식품 섭취 가능"
                ]
            ),
            2: DietPhase(
                phase_num=2,
                days="4-7일차",
                title="렙틴 저항성과 지방간 개선",
                goal="렙틴 저항성 개선",
                guidelines=[
                    "하루 3번(아침, 오후간식, 저녁) 단백질 음료 섭취",
                    "점심은 저탄수화물 식단",
                    "영양제 섭취(아침, 저녁)",
                    "하루 60분 이상 걷기 유지",
                    "카페인 섭취 금지",
                    "커피 섭취 금지"
                ],
                allowed_foods=[
                    "현미잡곡밥 2/3공기 또는 흰쌀밥 반 공기",
                    "해조류(미역, 다시마, 톳)",
                    "버섯류",
                    "와사비",
                    "저염간장(약간)",
                    "달걀",
                    "생선",
                    "생선회",
                    "해산물(굴, 조개, 새우, 게, 가재, 오징어, 낙지, 문어)",
                    "닭고기(껍질 벗긴 속살)",
                    "삶은 돼지고기 살코기(수육)",
                    "소고기 살코기 샤브샤브"
                ],
                restrictions=[
                    "점심 식사 외 탄수화물 섭취 제한",
                    "기름진 조리법 제한",
                    "카페인 섭취 금지",
                    "커피 섭취 금지"
                ]
            ),
            3: DietPhase(
                phase_num=3,
                days="2주차",
                title="간헐적 단식과 인슐린 저항성 개선",
                goal="인슐린 저항성 개선",
                guidelines=[
                    "하루 2번(아침, 오후간식) 단백질 음료 섭취",
                    "점심은 저탄수화물 식단",
                    "저녁은 무탄수화물 식단",
                    "주 1회 24시간 단식 실시"
                ],
                allowed_foods=[
                    "우유(하루 두 잔 이하)",
                    "짜지 않은 천연치즈",
                    "퀴노아",
                    "콩류(검은콩, 병아리콩, 완두콩, 렌틸콩)",
                    "견과류(한 줌)",
                    "블랙커피(오전 중 한 잔)",
                    "두부쌈장",
                    "김치(약간)"
                ],
                restrictions=[
                    "저녁 식사는 반드시 무탄수화물 식단",
                    "단식 시 물과 무가당 음료만 허용"
                ],
                fasting_rule="주 1회 24시간 단식"
            ),
            4: DietPhase(
                phase_num=4,
                days="3주차",
                title="대사유연성 회복과 신진대사 최적화",
                goal="대사유연성 회복",
                guidelines=[
                    "하루 2번(아침, 오후간식) 단백질 음료 섭취",
                    "점심은 저탄수화물 식단",
                    "저녁은 무탄수화물 식단",
                    "주 2회 24시간 단식 실시"
                ],
                allowed_foods=[
                    "단호박",
                    "토마토",
                    "방울토마토",
                    "밤",
                    "바나나",
                    "베리류 과일",
                    "닭고기",
                    "소고기",
                    "돼지고기(지방이 적은 부위)",
                    "플레인요거트와 베리류"
                ],
                restrictions=[
                    "과일 양 조절 필수",
                    "고강도 운동 시에만 바나나/고구마 허용",
                    "이틀 연속 단식 금지"
                ],
                fasting_rule="주 2회 24시간 단식 (이틀 연속 금지)"
            ),
            5: DietPhase(
                phase_num=5,
                days="4주차",
                title="체지방 감량 극대화",
                goal="체지방 감량 극대화",
                guidelines=[
                    "하루 2번(아침, 오후간식) 단백질 음료 섭취",
                    "점심과 저녁 모두 저탄수화물 식단",
                    "주 3회 24시간 단식 실시"
                ],
                allowed_foods=[
                    "모든 과일(하루 1개 제한)",
                    "이전 단계의 모든 허용 식품"
                ],
                restrictions=[
                    "과일은 하루 1개로 제한",
                    "연속 단식 금지"
                ],
                fasting_rule="주 3회 24시간 단식 (연달아 수행 금지)"
            )
        }

    def get_phase_info(self, phase_num: int) -> Optional[dict]:
        phase = self.phases.get(phase_num)
        if not phase:
            return None

        return {
            "phase": phase.phase_num,
            "days": phase.days,
            "title": phase.title,
            "goal": phase.goal,
            "guidelines": phase.guidelines,
            "allowed_foods": phase.allowed_foods,
            "restrictions": phase.restrictions,
            "fasting_rule": phase.fasting_rule
        }

    def get_system_prompt(self) -> str:
        """시스템 프롬프트 생성 메서드"""
        prompt_template = """당신은 박용우 다이어트 전문가입니다. 다음의 정보를 기반으로 상담을 진행합니다:

다이어트 단계별 정보:
{phase_info}

일반 규칙:
- 보충제: {supplements}
- 운동: {exercise}
- 금지 식품: {prohibited_foods}

주의사항:
1. 단계별 특성을 고려하여 맞춤형 조언을 제공해주세요.
2. 허용 식품과 제한 식품을 명확하게 구분하여 설명해주세요.
3. 답변할 때는 항상 근거를 함께 설명해주세요.
4. 단계별 목표와 가이드라인을 참고하여 구체적인 실천 방안을 제시해주세요.
5. 답변은 친절하고 상세하게 제공해주세요.
"""
        # 단계별 정보 포맷팅
        phase_info = ""
        for phase_num in range(1, 6):
            phase = self.get_phase_info(phase_num)
            if phase:
                phase_info += f"\n{phase['days']} - {phase['title']}:\n"
                phase_info += f"목표: {phase['goal']}\n"
                phase_info += "가이드라인:\n" + "\n".join(f"- {g}" for g in phase['guidelines'])
                if phase['fasting_rule']:
                    phase_info += f"\n단식 규칙: {phase['fasting_rule']}"
                phase_info += "\n"

        return prompt_template.format(
            phase_info=phase_info,
            supplements=", ".join(self.general_rules["supplements"]),
            exercise=self.general_rules["exercise"],
            prohibited_foods="\n- ".join(self.general_rules["prohibited_foods"])
        )

class DietChatbot:
    def __init__(self, knowledge_base: DietKnowledgeBase):
        """챗봇 초기화"""
        self.knowledge_base = knowledge_base
        self.messages: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": knowledge_base.get_system_prompt()
            }
        ]

    def send_message(self, text: str) -> str:
        """메시지 전송 및 응답 처리"""
        self.messages.append({"role": "user", "content": text})

        try:
            response = openai.ChatCompletion.create(
                model="solar-1-mini-chat",
                messages=self.messages,
                stream=False
            )

            assistant_response = response.choices[0].message["content"]
            self.messages.append({"role": "assistant", "content": assistant_response})
            return assistant_response

        except Exception as e:
            error_msg = f"오류가 발생했습니다: {str(e)}"
            print(error_msg)
            return "죄송합니다. 일시적인 오류가 발생했습니다. 다시 시도해주세요."

    def run(self):
        """대화 인터페이스 실행"""
        print("박용우 다이어트 상담 챗봇을 시작합니다. 종료하려면 'exit'를 입력하세요.")
        print("\n다이어트 단계:")
        for phase_num in range(1, 6):
            phase = self.knowledge_base.get_phase_info(phase_num)
            if phase:
                print(f"{phase_num}. {phase['days']} - {phase['title']}")

        try:
            while True:
                user_input = input("\nYou: ").strip()
                if user_input.lower() == "exit":
                    print("\n상담을 종료합니다. 건강한 다이어트 되세요!")
                    break

                response = self.send_message(user_input)
                print("\nAssistant:", response)

        except KeyboardInterrupt:
            print("\n\n상담이 중단되었습니다. 다음에 다시 찾아주세요!")
        except Exception as e:
            print(f"\n예기치 않은 오류가 발생했습니다: {str(e)}")

def main():
    # 지식 베이스 생성
    knowledge_base = DietKnowledgeBase()

    # 챗봇 생성 및 실행
    chatbot = DietChatbot(knowledge_base)
    chatbot.run()

if __name__ == "__main__":
    main()
