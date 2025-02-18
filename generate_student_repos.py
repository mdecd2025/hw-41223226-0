import requests

def generate_html():
    # 下載2b.txt文件
    url = 'https://mde.tw/list/2b.txt'
    response = requests.get(url)
    data = response.text

    # 解析文件內容
    students = []
    lines = data.split('\n')
    for line in lines:
        if line.strip():
            student_id, github_username = line.split()
            repo_url = f'https://github.com/{github_username}/{student_id}'
            site_url = f'https://{github_username}.github.io/{student_id}'
            students.append((student_id, repo_url, site_url))

    # 生成HTML文件
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>學員倉儲列表</title>
</head>
<body>
    <h1>學員倉儲列表</h1>
    <ul>
    '''
    for student_id, repo_url, site_url in students:
        html_content += f'''
        <li>
            <h2>{student_id} (repo)</h2>
            <p>GitHub: <a href="{repo_url}">{repo_url}</a></p>
            <p>網站: <a href="{site_url}">{site_url}</a></p>
        </li>
        '''
    html_content += '''
    </ul>
</body>
</html>
    '''

    with open('students_repos.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == '__main__':
    generate_html()