#!/usr/bin/env python3
"""
Instagram Follower Tracker
- 사용자 목록에서 프로필 정보를 가져와 HTML 파일 생성
- 프로필 사진을 로컬 assets 폴더에 다운로드
- GitHub Pages 배포용
"""

import instaloader
import requests
import time
import os
from datetime import datetime
from pathlib import Path


def load_users(filepath: str = "users.txt") -> list[str]:
    """users.txt에서 사용자 목록을 읽어옵니다."""
    users = []
    
    if not os.path.exists(filepath):
        print(f"⚠️ {filepath} 파일이 없습니다. 샘플 파일을 생성해주세요.")
        return users
    
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # 빈 줄과 주석(#으로 시작) 무시
            if line and not line.startswith("#"):
                # @로 시작하면 제거
                username = line.lstrip("@")
                users.append(username)
    
    return users


def download_image(url: str, save_path: str) -> bool:
    """이미지를 다운로드하여 로컬에 저장합니다."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        with open(save_path, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"  └─ 이미지 다운로드 실패: {e}")
        return False


def create_default_image(assets_dir: str):
    """기본 프로필 이미지(SVG)를 생성합니다."""
    default_path = os.path.join(assets_dir, "default.svg")
    
    if os.path.exists(default_path):
        return
    
    # 심플한 기본 프로필 SVG 생성
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <circle cx="50" cy="50" r="50" fill="#e0e0e0"/>
  <circle cx="50" cy="38" r="18" fill="#bdbdbd"/>
  <ellipse cx="50" cy="85" rx="30" ry="25" fill="#bdbdbd"/>
</svg>'''
    
    print("📥 기본 이미지 생성 중...")
    with open(default_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("  └─ 완료!")


def generate_html(users_data: list[dict], total_count: int) -> str:
    """HTML 컨텐츠를 생성합니다."""
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>팔로우 필요 목록</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 40px 20px;
        }}
        
        .container {{
            max-width: 600px;
            margin: 0 auto;
        }}
        
        header {{
            text-align: center;
            margin-bottom: 30px;
            color: white;
        }}
        
        header h1 {{
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 8px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }}
        
        header p {{
            font-size: 0.9rem;
            opacity: 0.9;
        }}
        
        .stats {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 15px;
        }}
        
        .stat-item {{
            background: rgba(255,255,255,0.2);
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 0.85rem;
            backdrop-filter: blur(10px);
        }}
        
        .user-list {{
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        
        .user-card {{
            display: flex;
            align-items: center;
            background: white;
            padding: 16px;
            border-radius: 16px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }}
        
        .user-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }}
        
        .user-card.failed {{
            background: #f8f8f8;
            opacity: 0.8;
        }}
        
        .user-card img {{
            width: 56px;
            height: 56px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #eee;
            flex-shrink: 0;
        }}
        
        .info {{
            flex-grow: 1;
            margin-left: 14px;
            min-width: 0;
        }}
        
        .username {{
            font-weight: 600;
            font-size: 1rem;
            color: #262626;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        
        .private-tag {{
            font-size: 0.7rem;
            color: #ff6b6b;
            font-weight: 600;
        }}
        
        .public-tag {{
            font-size: 0.7rem;
            color: #51cf66;
            font-weight: 600;
        }}
        
        .failed-tag {{
            font-size: 0.7rem;
            color: #aaa;
        }}
        
        .fullname {{
            font-size: 0.85rem;
            color: #8e8e8e;
            margin-top: 2px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        
        .btn {{
            text-decoration: none;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 0.85rem;
            flex-shrink: 0;
            transition: opacity 0.2s ease, transform 0.2s ease;
        }}
        
        .btn:hover {{
            opacity: 0.9;
            transform: scale(1.02);
        }}
        
        .btn.disabled {{
            background: #ccc;
        }}
        
        footer {{
            text-align: center;
            margin-top: 30px;
            color: rgba(255,255,255,0.7);
            font-size: 0.8rem;
        }}
        
        @media (max-width: 480px) {{
            .user-card {{
                padding: 12px;
            }}
            
            .user-card img {{
                width: 48px;
                height: 48px;
            }}
            
            .btn {{
                padding: 8px 14px;
                font-size: 0.8rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 팔로우 필요 목록</h1>
            <p>마지막 업데이트: {now}</p>
            <div class="stats">
                <div class="stat-item">총 {total_count}명</div>
            </div>
        </header>
        
        <div class="user-list">
"""
    
    for user in users_data:
        if user["success"]:
            privacy_tag = '<span class="private-tag">🔒 비공개</span>' if user["is_private"] else '<span class="public-tag">🌏 공개</span>'
            html += f"""
            <div class="user-card">
                <img src="assets/{user['username']}.jpg" onerror="this.src='assets/default.svg'" alt="{user['username']}">
                <div class="info">
                    <div class="username">{user['username']} {privacy_tag}</div>
                    <div class="fullname">{user['full_name'] or '-'}</div>
                </div>
                <a href="https://www.instagram.com/{user['username']}/" target="_blank" rel="noopener" class="btn">팔로우</a>
            </div>
"""
        else:
            html += f"""
            <div class="user-card failed">
                <img src="assets/default.svg" alt="{user['username']}">
                <div class="info">
                    <div class="username">{user['username']} <span class="failed-tag">⚠️ 조회 실패</span></div>
                    <div class="fullname">정보를 가져올 수 없습니다</div>
                </div>
                <a href="https://www.instagram.com/{user['username']}/" target="_blank" rel="noopener" class="btn disabled">확인</a>
            </div>
"""
    
    html += """
        </div>
        
        <footer>
            <p>Powered by Instagram Follower Tracker</p>
        </footer>
    </div>
</body>
</html>
"""
    
    return html


def main():
    print("=" * 50)
    print("🔍 Instagram Follower Tracker")
    print("=" * 50)
    
    # assets 폴더 생성
    assets_dir = "assets"
    Path(assets_dir).mkdir(exist_ok=True)
    
    # 기본 이미지 준비
    create_default_image(assets_dir)
    
    # 사용자 목록 로드
    target_list = load_users("users.txt")
    
    if not target_list:
        print("❌ 확인할 사용자가 없습니다. users.txt 파일을 확인해주세요.")
        return
    
    print(f"\n📋 총 {len(target_list)}명의 사용자를 확인합니다.\n")
    
    # Instaloader 인스턴스 생성 (로그인 없이)
    L = instaloader.Instaloader()
    
    users_data = []
    
    for i, username in enumerate(target_list, 1):
        print(f"[{i}/{len(target_list)}] {username} 처리 중...")
        
        user_info = {
            "username": username,
            "success": False,
            "full_name": "",
            "is_private": False,
        }
        
        try:
            # 프로필 정보 가져오기
            profile = instaloader.Profile.from_username(L.context, username)
            
            user_info["success"] = True
            user_info["full_name"] = profile.full_name
            user_info["is_private"] = profile.is_private
            
            # 프로필 사진 다운로드 (이미 존재하면 스킵)
            img_path = os.path.join(assets_dir, f"{username}.jpg")
            if os.path.exists(img_path):
                print(f"  └─ ✅ 성공 (이미지 이미 존재)")
            elif download_image(profile.profile_pic_url, img_path):
                print(f"  └─ ✅ 성공 (이미지 저장됨)")
            else:
                print(f"  └─ ✅ 성공 (이미지 저장 실패, 기본 이미지 사용)")
            
        except Exception as e:
            print(f"  └─ ❌ 실패: {str(e)[:50]}")
        
        users_data.append(user_info)
        
        # Rate limit 방지를 위한 딜레이 (마지막 요청 후에는 불필요)
        if i < len(target_list):
            time.sleep(3)
    
    # HTML 생성
    print("\n📝 HTML 파일 생성 중...")
    html_content = generate_html(users_data, len(target_list))
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # 결과 요약
    success_count = sum(1 for u in users_data if u["success"])
    fail_count = len(users_data) - success_count
    
    print("\n" + "=" * 50)
    print("✨ 완료!")
    print(f"   - 성공: {success_count}명")
    print(f"   - 실패: {fail_count}명")
    print(f"   - 결과 파일: index.html")
    print(f"   - 이미지 폴더: {assets_dir}/")
    print("=" * 50)


if __name__ == "__main__":
    main()

