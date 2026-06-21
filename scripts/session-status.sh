#!/usr/bin/env bash
# Printed at SessionStart in every Next Visit repo so a session sees the whole
# product (all 4 repos) at once: live git heads for each repo + the shared
# narrative (couples staging:STATUS.md, the single source of truth). All repos
# live behind the same git host, so we reach siblings by rewriting the origin
# URL. Non-fatal: any failure just prints less, never blocks the session.
set +e
B=$(git remote get-url origin 2>/dev/null | sed 's#/[^/]*$##')
[ -z "$B" ] && exit 0

echo "=== NEXT VISIT - one product, all repos (live) ==="
for r in couples go site dashboard; do
  o=$(git ls-remote --heads "$B/next-visit-$r" 2>/dev/null)
  m=$(printf '%s\n' "$o" | grep -E 'refs/heads/main$' | cut -c1-7)
  s=$(printf '%s\n' "$o" | grep -E 'refs/heads/staging$' | cut -c1-7)
  line="main:${m:--}"
  [ -n "$s" ] && line="$line  staging:$s"
  [ -n "$s" ] && [ "$s" != "$m" ] && line="$line  (staging ahead -> work pending promotion)"
  printf '%-9s %s\n' "$r" "$line"
done

echo
echo "=== product status (couples staging:STATUS.md - single source of truth) ==="
git fetch -q "$B/next-visit-couples" staging 2>/dev/null \
  && git show FETCH_HEAD:STATUS.md 2>/dev/null \
  || echo "(STATUS.md unavailable - check couples staging)"
exit 0
