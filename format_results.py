import sys

content = open('/home/manasa151/.config/Code/User/workspaceStorage/8ccb7e361a81e3058994882cccb16a1f/GitHub.copilot-chat/chat-session-resources/82e2e408-a44d-414e-9574-9e4a45d2a7cd/call_MHxhTmlUejVORUJST0RrOXBZWkg__vscode-1778894153081/content.txt').read()
lines = content.split('\n')
data_lines = [l for l in lines if l.count('|') == 3]

print(f"Total found matching criteria: {len(data_lines)}")
for i in range(0, min(len(data_lines), 400), 8):
    batch_num = 101 + (i // 8)
    if batch_num > 150: break
    batch_items = data_lines[i:i+8]
    print(f"\nBATCH {batch_num}:")
    for item in batch_items:
        parts = item.split('|')
        if len(parts) == 4:
            cls, slug, name, slen = parts
            print(f"  {cls}: {slug} ({name}, summary: {slen})")

for l in lines:
    if "---350 and 370 samples---" in l:
        print("\n" + l)
        idx = lines.index(l)
        print("\n".join(lines[idx+1:]))
