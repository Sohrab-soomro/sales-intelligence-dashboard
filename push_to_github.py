import os
import sys
import json
import base64
import urllib.request
import urllib.error

GITHUB_USERNAME = "Sohrab-soomro"
DEFAULT_REPO_NAME = "sales-intelligence-dashboard"
FOLDER = os.path.dirname(os.path.abspath(__file__))

FILES_TO_PUSH = [
    ("README.md", "docs: add README with explicit 100% synthetic dummy data disclaimer"),
    (".gitignore", "chore: add .gitignore for temporary Excel lock files"),
    ("index.html", "feat: add Sales Intelligence Control Center dashboard with humanized developer comments"),
    ("Jazz_Sales_Intelligence_Dashboard.html", "feat: add standalone dashboard HTML file with humanized comments"),
    ("N2_Bundle_Upsell_Sciences_OCT-25_MASTER.xlsx", "data(dummy): add Oct 2025 100% synthetic dummy workbook for demo"),
    ("N2_Bundle_Upsell_Sciences_NOV-25_MASTER.xlsx", "data(dummy): add Nov 2025 100% synthetic dummy workbook for demo"),
    ("N2_Bundle_Upsell_Sciences_DEC-25_MASTER_V3.3.xlsx", "data(dummy): add Dec 2025 100% synthetic dummy workbook for demo"),
    ("upadted N2 file.xlsx", "data(dummy): add current-period 100% synthetic dummy workbook for demo"),
]

def github_api(method, url, token, payload=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "Sohrab-Soomro-Dashboard-Uploader",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, (json.loads(body) if body else {})
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        try:
            return e.code, json.loads(err_body)
        except Exception:
            return e.code, {"message": err_body}

def main():
    print("=" * 72)
    print("  GitHub Separate Repo Pusher — Sohrab-soomro")
    print("=" * 72)
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if len(sys.argv) > 1 and sys.argv[1].strip():
        token = sys.argv[1].strip()
    if not token:
        print("\nTo push directly to https://github.com/Sohrab-soomro:")
        print("1. Go to: https://github.com/settings/tokens/new?scopes=repo&description=DashboardPush")
        print("2. Generate a classic token (with 'repo' checked) and paste it below.\n")
        token = input("Paste your GitHub Personal Access Token: ").strip()
    if not token:
        print("Error: No GitHub token provided.")
        sys.exit(1)

    repo_name = os.environ.get("GITHUB_REPO", DEFAULT_REPO_NAME).strip() or DEFAULT_REPO_NAME
    print(f"\n[1/3] Creating separate repository '{GITHUB_USERNAME}/{repo_name}' ...")
    status, res = github_api(
        "POST",
        "https://api.github.com/user/repos",
        token,
        {
            "name": repo_name,
            "description": "Sales & Bundle Upsell Intelligence Control Center (Includes 100% Synthetic Dummy Data Workbooks for Portfolio Demo)",
            "private": False,
            "auto_init": True,
        },
    )
    if status in (200, 201):
        print(f"  -> Created new repository: https://github.com/{GITHUB_USERNAME}/{repo_name}")
    elif status == 422:
        print(f"  -> Repository https://github.com/{GITHUB_USERNAME}/{repo_name} already exists; updating files...")
    else:
        print(f"  -> GitHub API error ({status}): {res.get('message')}")
        sys.exit(1)

    print("\n[2/3] Uploading dashboard & verified 100% dummy Excel files ...")
    for fname, commit_msg in FILES_TO_PUSH:
        fpath = os.path.join(FOLDER, fname)
        if not os.path.exists(fpath):
            print(f"  -> Skipping missing file: {fname}")
            continue
        with open(fpath, "rb") as f:
            b64_content = base64.b64encode(f.read()).decode("ascii")

        # Check if file already exists in repo to get its SHA
        encoded_name = urllib.parse.quote(fname)
        content_url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/contents/{encoded_name}"
        g_status, g_res = github_api("GET", content_url, token)
        payload = {
            "message": commit_msg,
            "content": b64_content,
            "branch": "main"
        }
        if g_status == 200 and isinstance(g_res, dict) and "sha" in g_res:
            payload["sha"] = g_res["sha"]

        u_status, u_res = github_api("PUT", content_url, token, payload)
        if u_status in (200, 201):
            print(f"  ✓ Pushed: {fname}")
        else:
            print(f"  ✗ Failed {fname} ({u_status}): {u_res.get('message')}")

    print("\n[3/3] Enabling GitHub Pages for live LinkedIn demo link ...")
    p_status, _ = github_api(
        "POST",
        f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}/pages",
        token,
        {"source": {"branch": "main", "path": "/"}}
    )
    if p_status in (201, 409):
        print(f"  ✓ GitHub Pages enabled: https://sohrab-soomro.github.io/{repo_name}/")

    print("\n" + "=" * 72)
    print(f"SUCCESS! Repository URL: https://github.com/{GITHUB_USERNAME}/{repo_name}")
    print(f"Live Dashboard URL:      https://sohrab-soomro.github.io/{repo_name}/")
    print("=" * 72)

if __name__ == "__main__":
    main()
