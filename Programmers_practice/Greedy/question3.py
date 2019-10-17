"""
시간 복잡도에 대한 부연 설명 :

문자열 number 의 길이를 n 이라고 하면, 이 알고리즘의 실행 시간은 n 에 비례합니다. 즉, 이 알고리즘은 O(n) 의 시간 복잡도를 가집니다.

왜 O(n^2) 처럼 보일 수 있는데 O(n) 이라는 설명을 했냐면, 코드의 구조만 보면 for 순환문 안에 또다시 while 순환문이 들어 있고, 이 둘 다가 n 에 비례하는 실행 회수를 가지는 것처럼 여겨질 수 있기 때문입니다.

그런데, 각 자리의 수 (한 글자) 의 입장에서 생각해 보면 (결국 이 알고리즘의 실행 시간이 무엇에 비례하는지는 while 순환문 안의 몸체가 얼마나 여러 번 실행되느냐에 달려 있습니다)

collected 라는 리스트에서 빠지는 회수가 많아야 한 번입니다. (적으면 0 번이구요.) 따라서 이 몸체는 기껏 해야 n 번 실행됩니다. 따라서 알고리즘의 복잡도는 n 에 비례합니다.

보충 설명은 위에 적힌 예를 통해서 하는 것이 적절할 듯하네요. number = "1239451234592" 이고 k = 11 인 경우, 처음부터 해서 "123" 까지는 한 번씩 collected 에 들어갔다가

(append()) 곧 바로 다음 for 순환문 반복에서 빠져나옵 (pop()) 니다. 한편, 그 다음의 "9" 는 한 번 들어가고 끝까지 나오지 않습니다. 그 다음의 "4" 도 앞선 "123" 과 마찬가지로 행동하지만,

또 그 다음의 "5" 는 마지막에서 두 번째인 "9" 를 만나기 전까지는 쌓여 있습니다. 마지막에서 두 번째 "9" 를 만나는 시점에서의 collected 의 상태는 ["9", "5", "5"] 입니다.

이 "9" 를 만났을 때 while 순환문의 몸체에 들어 있는 collected.pop() 이 두 번 실행하면서 두 개의 "5" 들을 제거합니다.

지금까지 pop() 은 (도합) 몇 번이나 일어났습니까? 이 회수가 문자열 number 의 길이인 n 보다 클 수 있나요?

요약하면, while 순환문의 몸체는 이중 순환문 안에 들어 있지만, 총 실행 회수는 주어진 문자열의 길이를 넘을 수 없습니다.

"""

def solution(number, k):
    # 숫자를 모아서 큰 수를 만드는데 이용할 리스트 정의
    collected = []

    # 숫자의 순서, 그리고 각 인덱스에 해당하는 숫자 모두가 필요하므로 number 문자열을
    # enumerate 함수를 이용하여 인덱스와 원소 동시에 접근하게끔 반복문을 구성한다
    for i, num in enumerate(number):
        # 꺼내온 숫자(num)가 collected에 있는 숫자보다 클때 아래의 반복문을 실행하여
        # 작은 숫자들을 모조리 k번 이하 만큼 pop한다
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        # 문자 제거가 다 끝나고 나머지 문자열을 이어 붙이고 반복문 모두 종료
        if k == 0:
            collected += list(number[i:])
            break
        # while 조건에 걸리지 않으면 숫자를 계속 쌓아 나아가는 부분
        collected.append(num)

    # 모든 숫자 문자열에 대한 탐색 및 k 값 이하만큼 제거를 하고도 k가 남았다면
    # 나머지 k를 소모하여 뒤에서부터 숫자를 제거한다(앞자리 있는 수가 크게끔 되어 있으므로)
    # 뒷자리 부터 하나씩 제거해 나가면 큰 수를 유지할 수 있다.
    collected = collected[:-k] if k > 0 else collected
    answer = ''.join(collected)

    return answer

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
