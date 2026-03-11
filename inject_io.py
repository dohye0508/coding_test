import os
import re

# Dictionary mapping filenames (or keywords) to specific I/O examples
IO_EXAMPLES = {
    '0_1배낭': {
        'in': "4 7\n6 13\n4 8\n3 6\n5 12",
        'out': "14"
    },
    '무제한배낭': {
        'in': "4 7\n6 13\n4 8\n3 6\n5 12",
        'out': "14"
    },
    '개수제한배낭': {
        'in': "2 3\n2 7 1\n1 9 2",
        'out': "16"
    },
    'KMP': {
        'in': "ABC ABCDAB ABCDABCDABDE\nABCDABD",
        'out': "1\n16"
    },
    '다익스트라': {
        'in': "5 6\n1\n1 2 2\n1 3 3\n2 3 4\n2 4 5\n3 4 6\n5 1 1",
        'out': "0\n2\n3\n7\nINF"
    },
    '플로이드워셜': {
        'in': "5\n14\n1 2 2\n1 3 3\n1 4 1\n1 5 10\n2 4 2\n3 4 1\n3 5 1\n4 5 3\n3 5 10\n3 1 8\n1 4 2\n5 1 7\n3 4 2\n5 2 4",
        'out': "0 2 3 1 4\n12 0 15 2 5\n8 5 0 1 1\n10 7 13 0 3\n7 4 10 6 0"
    },
    '벨만포드': {
        'in': "3 4\n1 2 4\n1 3 3\n2 3 -1\n3 1 -2",
        'out': "4\n3"
    },
    'BFS': {
        'in': "4 5 1\n1 2\n1 3\n1 4\n2 4\n3 4",
        'out': "1 2 3 4"
    },
    'DFS': {
        'in': "4 5 1\n1 2\n1 3\n1 4\n2 4\n3 4",
        'out': "1 2 4 3"
    },
    '위상정렬': {
        'in': "3 2\n1 3\n2 3",
        'out': "1 2 3"
    },
    '격자탐색': {
        'in': "4 5\n10111\n10101\n10101\n11101",
        'out': "15"
    },
    '유니온파인드': {
        'in': "7 4\n0 1 3\n1 1 7\n0 7 6\n1 7 1",
        'out': "NO\nYES"
    },
    '세그먼트트리': {
        'in': "5 2 2\n1\n2\n3\n4\n5\n1 3 6\n2 2 5\n1 5 2\n2 3 5",
        'out': "17\n12"
    },
    '1차원배열': {
        'in': "5 3\n5 4 3 2 1\n1 3\n2 4\n5 5",
        'out': "12\n9\n1"
    },
    '2차원배열': {
        'in': "4 4\n1 2 3 4\n2 3 4 5\n3 4 5 6\n4 5 6 7\n2 2 3 4",
        'out': "27"
    },
    '투포인터': {
        'in': "5 5\n1 2 3 2 5",
        'out': "3"
    },
    'LCA': {
        'in': "15\n1 2\n1 3\n2 4\n3 7\n6 2\n3 8\n4 9\n2 5\n5 11\n7 13\n10 4\n11 15\n12 5\n14 7\n6\n6 11\n10 9\n2 6\n7 6\n8 13\n8 15",
        'out': "2\n4\n2\n1\n3\n1"
    },
    '이분탐색': {
        'in': "5\n4 1 5 2 3\n5\n1 3 7 9 5",
        'out': "1\n1\n0\n0\n1"
    },
    '에라토스테네스의체': {
        'in': "3 16",
        'out': "3\n5\n7\n11\n13"
    },
    '유클리드호제법': {
        'in': "24 18",
        'out': "6\n72"
    },
    'LIS': {
        'in': "6\n10 20 10 30 20 50",
        'out': "4"
    },
    'LCS': {
        'in': "ACAYKP\nCAPCAK",
        'out': "4"
    },
    'CCW': {
        'in': "1 1\n5 5\n7 3",
        'out': "-1"
    },
    '선분교차': {
        'in': "1 1 5 5\n1 5 5 1",
        'out': "1"
    },
    '다각형면적': {
        'in': "3\n0 0\n10 0\n0 10",
        'out': "50.0"
    },
    'N-Queen': {
        'in': "8",
        'out': "92"
    },
    '우선순위큐': {
        'in': "8\n1\n2\n0\n0\n3\n0\n4\n0",
        'out': "2\n1\n3\n4"
    },
    '타일링': {
        'in': "9",
        'out': "55"
    },
    '트리DP': {
        'in': "9\n1 3\n2 3\n4 3\n5 4\n6 4\n7 4\n8 7\n9 7\n1\n4\n3\n7",
        'out': "1\n5\n9\n3"
    },
    '트리_순회': {
        'in': "7\nA B C\nB D .\nC E F\nE . .\nF . G\nD . .\nG . .",
        'out': "ABDCEFG\nDBAECFG\nDBEGFCA"
    },
    '회의실배정': {
        'in': "11\n1 4\n3 5\n0 6\n5 7\n3 8\n5 9\n6 10\n8 11\n8 12\n2 13\n12 14",
        'out': "4"
    },
    '동전0': {
        'in': "10 4200\n1\n5\n10\n50\n100\n500\n1000\n5000\n10000\n50000",
        'out': "6"
    },
    '잃어버린괄호': {
        'in': "55-50+40",
        'out': "-35"
    },
    'RGB거리': {
        'in': "3\n26 40 83\n49 60 57\n13 89 99",
        'out': "96"
    },
    '편집거리': {
        'in': "abc\ndef",
        'out': "3"
    }  
}

def get_examples(filename):
    for key, val in IO_EXAMPLES.items():
        if key in filename:
            return val
    # Default specific example
    return {
        'in': "5 3\n1 2\n2 3\n3 4\n4 5",
        'out': "1\n2\n3 4 5"
    }

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(file_path)
    if filename in ['generate_data.py', 'inject_io.py']:
        return

    # Check for docstring
    match = re.match(r'^\s*([\'"]{3})([\s\S]*?)\1\s*', content)
    if not match:
        return

    doc_full = match.group(0)
    doc_inner = match.group(2)
    marker = match.group(1)

    # We want to replace everything from [입력 예시] down to the end of the docstring
    # and put our specific numbers there.
    
    # Strip existing [입력 예시] and [출력 예시] blocks, if any
    clean_doc = re.split(r'\[입력 예시\]|입력 예시:', doc_inner)[0].strip()
    
    examples = get_examples(filename)
    
    new_doc_inner = f"""{clean_doc}

[입력 예시]
{examples['in']}

[출력 예시]
{examples['out']}"""
    
    new_doc = f"{marker}\n{new_doc_inner}\n{marker}\n"
    new_content = code_str = content.replace(doc_full, new_doc, 1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    base_dir = '.'
    for root, dirs, files in os.walk(base_dir):
        if '.git' in root or '.gemini' in root:
            continue
        for file in files:
            if file.endswith('.py'):
                update_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
