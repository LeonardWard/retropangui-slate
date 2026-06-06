#!/usr/bin/env python3
import os
import requests
import argparse

def download_console_images(force=False):
    repo_owner = "prefect421"
    repo_name  = "es-theme-lcars-p42"
    base_url   = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/"
    save_dir   = "/home/pangui/scripts/retropangui-slate/_assets/consoles/"

    os.makedirs(save_dir, exist_ok=True)

    headers = {}
    github_token = os.getenv("GITHUB_TOKEN")
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        print(f"레포 목록 가져오기 실패: {response.status_code}")
        return

    folders = [
        item for item in response.json()
        if item["type"] == "dir"
        and not item["name"].startswith(("_", "."))
    ]

    success_count = skip_count = fail_count = 0

    for folder in folders:
        name     = folder["name"]
        raw_url  = f"https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/{name}/_inc/console.png"
        save_path = os.path.join(save_dir, f"{name}-console.png")

        if not force and os.path.exists(save_path):
            print(f"  SKIP  {name}")
            skip_count += 1
            continue

        r = requests.get(raw_url)
        if r.status_code == 200:
            with open(save_path, "wb") as f:
                f.write(r.content)
            print(f"  OK    {name}")
            success_count += 1
        else:
            print(f"  MISS  {name} ({r.status_code})")
            fail_count += 1

    print(f"\n완료 — 다운로드: {success_count}  스킵: {skip_count}  없음: {fail_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="레포에서 콘솔 이미지 일괄 다운로드")
    parser.add_argument("--force", action="store_true", help="기존 파일도 덮어씀")
    args = parser.parse_args()
    download_console_images(args.force)
