#!/usr/bin/env python3
"""Читает журнал ModSecurity и показывает, какие правила сработали.

Использование: python3 waflog.py [сколько_последних_записей]
"""
import json
import sys
from pathlib import Path
from urllib.parse import unquote

LOG = Path(__file__).parent / "logs" / "audit.log"
count = int(sys.argv[1]) if len(sys.argv) > 1 else 5

lines = LOG.read_text(errors="ignore").splitlines()
shown = 0
for line in reversed(lines):
    try:
        t = json.loads(line)["transaction"]
    except (ValueError, KeyError):
        continue
    msgs = t.get("messages") or []
    if not msgs:
        continue
    print(f"[{t['time_stamp']}] {t['client_ip']}  "
          f"HTTP {t['response']['http_code']}  {unquote(t['request']['uri'])[:80]}")
    for m in msgs:
        d = m["details"]
        print(f"   правило {d['ruleId']:>6} | {d.get('severity', '-'):>1} | {m['message'][:75]}")
    print()
    shown += 1
    if shown >= count:
        break

if not shown:
    print("Срабатываний WAF в журнале нет.")
