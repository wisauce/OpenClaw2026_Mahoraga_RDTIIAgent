# Mermaid Syntax Pitfalls for RDTII Workflow Diagrams

Covers Mermaid syntax quirks discovered while generating RDTII workflow diagrams (`.mermaid` files for GitHub rendering).

## Critical: parentheses/arrows/ampersands in node labels

Mermaid **fails to parse** when the label text inside `[...]` contains `()`, `→`, or `&` — even escaped with `\n`.

**WRONG** (parser error):
```
nodeA[Score (0 to 1)]
nodeB[Pillar(s) & Indicator(s)]
nodeC[One measure → multiple indicators]
```

**RIGHT** (wrap the entire text in `["..."]`):
```
nodeA["Score (0 to 1)"]
nodeB["Pillar(s) & Indicator(s)"]
nodeC["One measure → multiple indicators"]
```

## Newlines in labels

Use `\n` for multi-line labels. Works inside both `[...]` and `["..."]`:

```
nodeA["First line\nSecond line"]
```

## Subgraph titles with special chars

Same rule applies — wrap in `["..."]`:

```
subgraph Phase["PHASE 6: MEASURE EXTRACTION"]
```

## Edge labels with `→` or other arrows

Use `|label|` syntax for edge labels. Arrows in the label text need quotes too:

```
A -->|"Yes → proceed"| B
A -->|"No → revise"| C
```

## Flow direction

- `flowchart TB` — top-to-bottom (best for pipelines)
- `flowchart LR` — left-to-right (best for parallel branching diagrams)

## Styling blocks

Apply at the bottom of the diagram:

```
style NodeID fill:#e3f2fd,stroke:#1565c0,color:#000
```

Keep `color:#000` (black text) for readability on GitHub's white background. The fill colors used in RDTII diagrams:

| Role | Fill | Stroke |
|------|------|--------|
| Input nodes | `#e1f5fe` | `#01579b` |
| Decision/conditional | `#fff9c4` (yellow) | `#f57f17` |
| Error/blocked paths | `#ffccbc` (red-orange) | `#bf360c` |
| Reviewer steps | `#e8f5e9` (green) | `#2e7d32` |
| Orchestrator | `#e3f2fd` (blue) | `#1565c0` |
| Subagent 1 | `#fce4ec` (pink) | `#c62828` |
| Subagent 2 | `#f3e5f5` (purple) | `#6a1b9a` |
| Subagent 3 | `#e8f5e9` (green) | `#2e7d32` |
| Subagent 4 | `#fff3e0` (orange) | `#e65100` |
| Merge phase | `#fff9c4` (yellow) | `#f57f17` |
| Verification gate | `#ffccbc` (red-orange) | `#bf360c` |

## Preview before committing

GitHub renders `.mermaid` files directly in the repo browser view. Always check the rendered preview after pushing — a parser error shows a red error box that looks unprofessional in a hackathon submission.

The 3 RDTII workflow diagrams are at `outputs/`:
- `rdtii-agent-workflow.mermaid` — 8-phase end-to-end
- `rdtii-parallel-research.mermaid` — 4-subagent parallel pattern
- `rdtii-autonomous-loop.mermaid` — agent loop + reviewer gate
