import os
import json

def generate():
    base_dir = '.'
    data = []
    
    # 순회하며 폴더와 파이썬 파일 정보 수집
    for root, dirs, files in os.walk(base_dir):
        # 숨김 폴더(.git 등) 제외
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        rel_dir = os.path.relpath(root, base_dir)
        if rel_dir == '.':
            continue
            
        folder_data = {
            'folderName': rel_dir.replace('\\', '/'),
            'files': []
        }
        
        for file in files:
            if file.endswith('.py') and file != 'generate_data.py':
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    folder_data['files'].append({
                        'fileName': file,
                        'content': content
                    })
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    
        if folder_data['files']:
            # 파일 이름 순으로 정렬
            folder_data['files'].sort(key=lambda x: x['fileName'])
            data.append(folder_data)
            
    # 폴더 이름 순으로 정렬
    data.sort(key=lambda x: x['folderName'])
    
    # 자바스크립트 변수 형태로 저장
    js_content = 'const codeData = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';'
    
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print("성공적으로 data.js가 생성되었습니다! 이제 index.html을 브라우저에서 열어보세요.")

if __name__ == '__main__':
    generate()
