import os
import re

ENRICH_DATA = {
    '0_1배낭문제.py': "0/1 배낭 문제 (0-1 Knapsack)\n\n[작동 원리]\n배낭의 용량이 정해져 있을 때, 담을 수 있는 물건들의 가치 합을 최대로 만드는 조합을 찾는 동적 계획법 알고리즘입니다.\n가장 일반적인 점화식은 `DP[i][w] = max(DP[i-1][w], DP[i-1][w-weight[i]] + value[i])` 입니다.\n즉, i번째 물건을 넣지 않았을 때의 가치와, i번째 물건을 넣었을 때의 가치 중 더 큰 값을 선택하며 표를 채워나갑니다.\n1차원 배열로 최적화할 경우, 중복 선택을 막기 위해 반드시 뒤에서부터 역방향으로 채워나가야 합니다.\n\n[시간 복잡도]\nO(N * K) (N: 물품의 수, K: 배낭의 용량)",
    '개수제한배낭문제.py': "개수 제한 배낭 문제 (Bounded Knapsack)\n\n[작동 원리]\n각 물건의 개수가 제한되어 있는 배낭 문제입니다.\n일반적인 DP로 풀면 O(N * K * C)가 되어 느리지만, 개수 C를 1, 2, 4, 8... 과 같이 2의 거듭제곱 단위로 분할하여 물건을 묶는 '이진화 기법(Binary Grouping)'을 사용하면 0/1 배낭 문제로 치환하여 매우 빠르게 풀 수 있습니다.\n\n[시간 복잡도]\nO(N * K * log C)",
    '무제한배낭문제.py': "무제한 배낭 문제 (Unbounded Knapsack)\n\n[작동 원리]\n물건의 개수 제한이 무한대인 배낭 문제입니다.\n0/1 배낭과 점화식은 동일하지만, 물건을 중복해서 사용할 수 있으므로 1차원 DP 배열을 업데이트할 때 용량을 정방향(앞에서부터 뒤로)으로 채워나갑니다.\n\n[시간 복잡도]\nO(N * K)",
    '최장증가부분수열.py': "최장 증가 부분 수열 (LIS, Longest Increasing Subsequence)\n\n[작동 원리]\n수열의 원소들 중 순서를 유지하면서 크기가 점점 커지는 부분 수열의 최대 길이를 구하는 알고리즘입니다.\nO(N^2) DP 방식과 이분 탐색을 활용한 O(N log N) 방식이 있습니다.\n해당 코드는 이분 탐색(bisect)을 활용하여, 현재 값이 이분 탐색의 어느 위치에 들어갈지 찾아서 치환하거나 배열 끝에 추가하는 방식으로 시간을 대폭 줄입니다.\n\n[시간 복잡도]\nO(N log N)",
    '가장긴바이토닉부분수열.py': "가장 긴 바이토닉 부분 수열 (Longest Bitonic Subsequence)\n\n[작동 원리]\n수열이 증가하다가 감소하는 형태로 이루어진 부분 수열 중 가장 긴 길이를 구하는 문제입니다.\n앞에서부터 LIS(최장 증가)를 구하고, 뒤에서부터 LIS(최장 감소)를 구한 뒤, 특정 기준점(i)에서 두 값을 더한 후 1을 뺀 값 중 최댓값을 찾습니다.\n\n[시간 복잡도]\nO(N log N)",
    '다익스트라.py': "다익스트라 알고리즘 (Dijkstra's Algorithm)\n\n[작동 원리]\n하나의 시작 정점으로부터 다른 모든 정점까지의 가장 짧은 경로를 구하는 최단 경로 알고리즘입니다.\n음의 간선이 없을 때만 사용 가능합니다.\n우선순위 큐(Min Heap)를 사용하여 현재 방문한 정점들 중 가장 비용이 적은 정점을 꺼내고, 그 정점을 거쳐서 가는 경로가 기존 경로보다 더 짧다면 비용 배열을 갱신하는 그리디(Greedy) 방식입니다.\n\n[시간 복잡도]\nO(E log V) (E: 간선의 수, V: 정점의 수)",
    '플로이드워셜.py': "플로이드 워셜 알고리즘 (Floyd-Warshall Algorithm)\n\n[작동 원리]\n동적 계획법을 이용하여 '모든 정점에서 모든 정점으로'의 최단 경로를 구하는 알고리즘입니다.\n3중 for문을 돌며, `정점 i에서 정점 j로 가는 거리`와 `정점 i에서 정점 k를 거쳐 정점 j로 가는 거리`를 비교하여 최적화합니다.\n노드 개수가 적을 때(일반적으로 V <= 500) 유용하며, 음의 가중치를 가진 간선이 있어도 사용할 수 있으나 음의 사이클이 없어야 합니다.\n\n[시간 복잡도]\nO(V^3)",
    '벨만포드.py': "벨만 포드 알고리즘 (Bellman-Ford Algorithm)\n\n[작동 원리]\n단일 출발점 최단 경로 알고리즘으로, 다익스트라와 달리 '음수 가중치'를 가진 간선이 있을 때도 사용할 수 있습니다.\n모든 간선을 N-1번(V-1번) 확인하며 최단 거리를 갱신합니다.\n만약 N번째(V번째) 확인에서 또 거리가 갱신된다면, 그래프 내에 무한히 비용이 줄어드는 '음수 사이클'이 존재함을 판단할 수 있습니다.\n\n[시간 복잡도]\nO(V * E)",
    'KMP_문자열매칭.py': "KMP 문자열 매칭 알고리즘\n\n[작동 원리]\n긴 본문 문자열 속에서 특정 패턴 문자열을 빠르게 찾는 알고리즘입니다.\n불일치가 발생했을 때 처음부터 다시 비교를 시작하는 단순 O(N*M)의 비효율을 막기 위해, 접두사와 접미사의 일치 길이를 저장한 LPS(Longest Prefix Suffix) 배열을 미리 전처리합니다.\n본문과 패턴을 비교하다 틀릴 경우, 패턴 내에서 중복되는 부분을 건너뛰고 비교를 이어나갑니다.\n\n[시간 복잡도]\nO(N + M) (N: 본문 길이, M: 패턴 길이)",
    '1차원_누적합.py': "1차원 누적 합 (Prefix Sum)\n\n[작동 원리]\n배열에 있는 특정 구간 [L, R]의 합을 연속해서 구해야 할 때 사용합니다.\n매번 O(N)으로 구간을 합산하지 않고, 미리 처음부터 현재 인덱스까지의 합을 저장하는 `prefix_sum` 배열을 한 번의 스캔(O(N))으로 만듭니다.\n이후 특정 구간 [L, R]의 합은 `prefix_sum[R] - prefix_sum[L-1]` 연산을 통해 단 O(1)만에 빠르게 구할 수 있습니다.\n\n[시간 복잡도]\n전처리 O(N), 쿼리당 O(1)",
    '2차원_누적합.py': "2차원 누적 합 (2D Prefix Sum)\n\n[작동 원리]\n2차원 배열에서 특정 직사각형 영역의 합을 연속해서 구할 때 사용합니다.\n1차원 누적합의 개념을 확장하여 `DP[i][j] = 원본[i][j] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]` 공식을 사용해 전처리합니다.\n이후 특정 구간 (x1, y1)부터 (x2, y2)까지의 합은 `DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1]` 공식을 통해 O(1) 시간만에 구할 수 있습니다. 중복해서 뺀 영역을 다시 더해주는 것이 핵심입니다.\n\n[시간 복잡도]\n전처리 O(N^2), 쿼리당 O(1)",
    '세그먼트트리.py': "세그먼트 트리 (Segment Tree)\n\n[작동 원리]\n어떤 배열에서 '특정 구간의 데이터 합/최솟값/최댓값' 등을 구하는 쿼리가 매우 잦고, 동시에 '배열의 특정 요소 값이 변경'되는 업데이트 쿼리 또한 잦을 때 사용하는 고급 자료구조입니다.\n루트 노드가 전체 구간을 담당하고 자식 노드들이 반씩 구간을 나누어 가지는 이진 트리 형태입니다.\n단순 배열로 하면 합을 구하는 데 O(N), 요소를 바꾸는 데 O(1)이 걸리지만, 세그먼트 트리를 사용하면 합치기와 변경 모두 빠르게 수행할 수 있습니다.\n\n[시간 복잡도]\n트리 초기화 O(N), 쿼리당 O(log N), 업데이트 O(log N)",
    '유니온파인드.py': "분리 집합 / 유니온 파인드 (Disjoint Set / Union-Find)\n\n[작동 원리]\n서로 중복되지 않는 부분 집합들을 표현할 때 사용하는 자료구조로, 노드들이 같은 집합에 속해 있는지를 확인하거나 두 집합을 하나로 합치는 연산을 수행합니다.\n- `Find`: 해당 노드의 최상위 부모(루트) 노드를 찾으며 이 과정에서 경로 압축(Path Compression)을 통해 트리의 높이를 평평하게 만듭니다.\n- `Union`: 두 노드의 트리를 하나로 연결하며, 랭크나 크기 최적화를 통해 작은 트리를 큰 트리에 붙입니다.\n\n[시간 복잡도]\n실질적으로 O(1) (엄밀히는 아커만 함수의 역함수 알파(N))",
    '유클리드호제법.py': "유클리드 호제법 (Euclidean Algorithm)\n\n[작동 원리]\n두 정수의 최대공약수(GCD)를 로그 시간 내에 빠르게 구하는 고전적인 수학 알고리즘입니다.\n`A`를 `B`로 나눈 나머지를 `R`이라고 할 때, `A`와 `B`의 최대공약수는 `B`와 `R`의 최대공약수와 동일하다는 원리를 이용합니다.\n재귀나 반복문을 통해 나머지가 0이 될 때까지 `A = B`, `B = R`로 값을 넘겨주면서 몫을 계산합니다.\n최소공배수(LCM)는 두 수의 곱을 이 GCD로 나누어 구합니다.\n\n[시간 복잡도]\nO(log(min(A, B)))",
    '에라토스테네스의체.py': "에라토스테네스의 체 (Sieve of Eratosthenes)\n\n[작동 원리]\n대량의 숫자 범위 내에서 소수(Prime Number)를 한꺼번에 구하고자 할 때 사용하는 고속 알고리즘입니다.\n마치 체로 치듯이 합성수를 걸러낸다는 의미가 있습니다.\n2부터 시작해 특정 수의 배수들을 전부 지우는 방식으로 진행되며, 어떤 수 N까지 소수를 판별할 때는 N의 제곱근까지만 판별해도 충분하다는 수학적 정리를 이용하여 최적화합니다.\n\n[시간 복잡도]\nO(N log(log N))",
    '편집거리.py': "편집 거리 알고리즘 / 레벤슈타인 거리 (Levenshtein Distance)\n\n[작동 원리]\n두 문자열이 얼마나 유사한지를 수치화하기 위해, 한 문자열을 다른 문자열로 변환하는 데 필요한 최소한의 삽입, 삭제, 교체 연산 횟수를 구하는 2차원 DP 알고리즘입니다.\n두 문자가 같다면 수정할 필요가 없으므로 대각선 위 값(비용 추가 없음)을 그대로 가져오며, 문자가 다르다면 삽입(왼쪽+1), 삭제(위쪽+1), 교체(대각선+1) 중 가장 작은 비용을 선택해 DP 배열을 갱신합니다.\n\n[시간 복잡도]\nO(N * M) (N, M은 각각 두 문자열의 길이)"
}

def process():
    for root, _, files in os.walk('.'):
        for file in files:
            if not file.endswith('.py') or file in ['generate_data.py', 'inject_io.py', 'enrich_docs.py']:
                continue
            
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            match = re.match(r'^\s*([\'\x22]{3})([\s\S]*?)\1', content)
            if not match:
                continue

            marker = match.group(1)
            doc_inner = match.group(2)
            
            # Extract [입력 예시] blocks
            io_parts = re.split(r'(\[입력 예시\]|입력 예시:)', doc_inner)
            
            # We want to replace the top description with ENRICH_DATA if it exists
            # Otherwise, keep the old one but clean it up.
            desc_part = io_parts[0].strip()
            
            if file in ENRICH_DATA:
                new_desc = ENRICH_DATA[file]
            else:
                # Fallback, just keep existing but make sure it looks neat
                new_desc = desc_part
            
            io_block = ""
            if len(io_parts) > 1:
                # Add [입력 예시] and what follows
                io_block = "\n\n" + "".join(io_parts[1:]).strip()
            
            new_docstring = f"{marker}\n{new_desc}{io_block}\n{marker}"
            new_content = content.replace(match.group(0), new_docstring, 1)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

if __name__ == "__main__":
    process()
