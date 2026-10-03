# Islamic Lyric Audit Skill (`.agents/skills/islamic-lyric-audit`)

This repository includes the **`islamic-lyric-audit`** skill under `.agents/skills/islamic-lyric-audit/`. Any AI coding assistant or agent opening this repository (Antigravity, Cursor, Windsurf, Cline, Codex) will automatically discover and load this skill.

---

## 📁 Repository Structure

```text
.agents/
└── skills/
    └── islamic-lyric-audit/
        ├── SKILL.md                          # Core instructions, Sunni guardrails, workflow
        ├── references/
        │   ├── scoring_rubric.md             # 8-dimensional scoring rules (0 to 5)
        │   └── jurisprudence_evidence.md     # Classical Sunni sources (Qur'an, Bukhari, Muslim)
        └── scripts/
            └── audit_cli.py                  # CLI utility for stats and HTML report generation
```

---

## 🚀 How Any Agent Uses This Skill

### 1. Slash Command / Prompt Trigger
Whenever prompted with:
* `/al [Song Title - Artist]`
* *"Audit these lyrics under Islamic framework"*
* *"Evaluate this song's theological content"*

The agent automatically activates the pre-frozen 8-dimensional scoring matrix (`0` to `5`):
1. **Dimension A:** Theological Severity (*Tawḥīd* / *Shirk* / Eschatology)
2. **Dimension B:** Major & Minor Sins (*Kabāʾir* vs. *Ṣaghāʾir*)
3. **Dimension C:** Taqwā & Pious Discipline (*Waraʿ*)
4. **Dimension D:** Glorification of Sin (*Mujāharah*)
5. **Dimension E:** Faḥsh & Sexual Lewdness
6. **Dimension F:** Laghw & Idle Speech
7. **Dimension G:** Violence, Injustice & Revenge
8. **Dimension H:** Pride, Arrogance & Materialism

---

## ⚖️ Mandatory Guardrails Enforced
* **No Takfīr (*Lā Takfīr*):** Sins and statements are judged, never the human artist's creed or salvation (Ṣaḥīḥ al-Bukhārī 6104).
* **Utterance vs. Intent:** Distinguishes poetic hyperbole from literal belief, while identifying spiritually dangerous expressions.
* **No Arithmetic Dilution:** Theological violations are never averaged out or masked by low profanity scores.
