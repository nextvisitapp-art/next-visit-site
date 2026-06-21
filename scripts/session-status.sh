#!/usr/bin/env bash
# SessionStart status for the whole Next Visit product (4 repos = one product).
# Everything here is derived LIVE from git, so it is always current with zero
# manual upkeep: per-repo heads + the exact commits sitting on couples staging
# that are not yet promoted to main. The only thing git cannot know (env / app
# store / RevenueCat state) lives in couples staging:STATUS.md, printed last.
# Sibling repos are reached by rewriting the origin URL (same git host).
# Non-fatal: any failure just prints less, never blocks the session.
set +e
B=$(git remote get-url origin 2>/dev/null | sed 's#/[^/]*$##')
[ -z "$B" ] && exit 0
CU="$B/next-visit-couples"

echo "=== NEXT VISIT - one product, all repos (live) ==="
for r in couples go site dashboard; do
  o=$(git ls-remote --heads "$B/next-visit-$r" 2>/dev/null)
  m=$(printf '%s\n' "$o" | grep -E 'refs/heads/main$' | cut -c1-7)
  s=$(printf '%s\n' "$o" | grep -E 'refs/heads/staging$' | cut -c1-7)
  line="main:${m:--}"
  [ -n "$s" ] && line="$line  staging:$s"
  [ -n "$s" ] && [ "$s" != "$m" ] && line="$line  (staging ahead)"
  printf '%-9s %s\n' "$r" "$line"
done

# Pull couples main + staging into private refs so we can derive, live, exactly
# what is pending promotion, and read STATUS.md. (Couples sessions already have
# the objects; other repos download them once - couples is the product core.)
git fetch -q "$CU" 'refs/heads/main:refs/nv/couples-main' 'refs/heads/staging:refs/nv/couples-staging' 2>/dev/null

echo
echo "=== couples: pending promotion - staging commits not on main (live, auto) ==="
if git rev-parse --verify -q refs/nv/couples-staging >/dev/null; then
  git log --oneline --no-decorate refs/nv/couples-main..refs/nv/couples-staging 2>/dev/null | head -40
else
  echo "(unavailable)"
fi

echo
echo "=== product context - couples staging:STATUS.md (git can't auto-derive this) ==="
git show refs/nv/couples-staging:STATUS.md 2>/dev/null || echo "(STATUS.md unavailable)"
exit 0
