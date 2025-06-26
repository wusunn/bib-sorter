#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import argparse

def split_entries(text):
    # 用正向前瞻，在每个 "@xxx{..." 之前切分
    parts = re.split(r'(?=@\w+\s*{)', text)
    # 丢掉开头可能的空白
    return [p for p in parts if p.strip()]

def extract_year(entry):
    # 寻找 year = {xxxx} 或 "xxxx"
    m = re.search(r'year\s*=\s*[{"]\s*(\d{1,4})\s*[}"]', entry, re.IGNORECASE)
    if m:
        try:
            return int(m.group(1))
        except:
            pass
    return 0

def extract_title_initial(entry):
    # 寻找 title = {....} 或 "...."
    m = re.search(r'title\s*=\s*[{"]\s*([^}"]+)', entry, re.IGNORECASE)
    if m:
        title = m.group(1).strip()
        for ch in title:
            if ch.isalpha():
                return ch.upper()
    return ''

def sort_key(entry):
    return (extract_year(entry), extract_title_initial(entry))

def main():
    parser = argparse.ArgumentParser(
        description="按年份升序，年份相同时按 title 首字母升序 排序 .bib 文件条目")
    parser.add_argument("input", help="输入 .bib 文件，比如 refs.bib")
    parser.add_argument("output", help="输出 .bib 文件，比如 sorted_refs.bib")
    args = parser.parse_args()

    text = open(args.input, encoding='utf-8').read()
    entries = split_entries(text)
    # 排序
    entries_sorted = sorted(entries, key=sort_key)
    # 写回
    with open(args.output, 'w', encoding='utf-8') as fo:
        fo.write('\n\n'.join(e.strip() for e in entries_sorted))
        fo.write('\n')
    print(f"排序完成 → {args.output}")

if __name__ == "__main__":
    main()
