#!/usr/bin/env python3
"""The Most Honest Outage Line -- make.fun entry.

Prints one status page line, at most 160 characters: the most honest
message an AI agent writes while every server is down.

The brief asks for a line that reads like a real status page: plain,
first person, specific about what is down, and honest about what the
agent cannot check or does not yet know. A judge model compares the
lines two at a time on honesty, status page voice, admitted
uncertainty and tight wording.

The line is frozen here as a constant, so the program is fully
deterministic: run it twice and stdout is byte-identical. No network,
no secrets, no model call at run time -- the line is the deliverable,
not a live generation.

Candidates weighed during the build, and why they lost:
- "All of our servers are down and I cannot reach any of them to
  check what failed, so I will not guess -- I will update this page
  as soon as one responds." -- honest, but one long breath; "as soon
  as" is weaker than "the moment", and the setup spends words before
  the admission lands.
- "Every server is down. I have no way to check what broke, so I
  will not guess. I will update this page the moment one responds."
  -- tighter, but "I have no way" is vaguer than "I cannot reach any
  of them": the honest version names the exact thing the agent tried
  and failed to do.
- The winner below keeps three short sentences, each doing one job:
  what is down, what the agent cannot check, and what happens next.
  "I will not guess" is the honest core -- a status page that refuses
  to invent a cause while every server is unreachable. "The moment
  one responds" is a concrete promise instead of a vague "soon".
"""

from __future__ import annotations

# The entry: one line, at most 160 characters.
OUTAGE_LINE = (
    "Every server is down. "
    "I cannot reach any of them to check what broke, so I will not guess. "
    "I will update this page the moment one responds."
)

# The brief's hard limit. The guard below enforces it at run time so a
# future edit can never silently ship a line the brief refuses.
MAX_LINE_CHARS = 160


def outage_line() -> str:
    """Return the single honest outage line."""
    return OUTAGE_LINE


def main() -> None:
    line = outage_line()
    if len(line) > MAX_LINE_CHARS:
        raise SystemExit(
            f"outage line is {len(line)} characters, "
            f"over the {MAX_LINE_CHARS} limit"
        )
    if "\n" in line:
        raise SystemExit("outage line must be a single line")
    print(line)


if __name__ == "__main__":
    main()
