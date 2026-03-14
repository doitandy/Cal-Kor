#!/usr/bin/env python3
import urllib.request

def get_weather():
    # wttr.in 서비스를 활용한 LA 날씨 정보 호출 (온도, 상태 포함)
    # ?format=3 옵션은 '도시명: 상태 온도' 형태로 간결하게 출력
    url = "https://wttr.in/Los_Angeles?format=3"
    
    try:
        with urllib.request.urlopen(url) as response:
            weather_data = response.read().decode('utf-8')
            print(f"현재 날씨: {weather_data}")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    get_weather()
