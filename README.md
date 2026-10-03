# Islamic Lyric Audit Skill

An evidence-based Sunni Islamic evaluation framework and CLI toolkit for AI agents (Antigravity, Cursor, Windsurf, Claude, Codex) to audit song lyrics, transcripts, and media speech across 8 theological, moral, and speech-discipline dimensions.

---

## 📁 Repository Structure

```text
islamic-lyric-audit/
├── LICENSE                           # Permissive MIT License
├── README.md                         # Project documentation and quickstart
├── SKILL.md                          # Core agent specification & /al slash command trigger
├── references/
│   ├── scoring_rubric.md             # Pre-frozen 8-dimensional scoring matrix (0 to 5)
│   └── jurisprudence_evidence.md     # Classical Sunni sources (Qur'an, Bukhari, Muslim, Ibn al-Qayyim)
└── scripts/
    └── audit_cli.py                  # Portable Python CLI for stats & interactive HTML report generation
```

---

## 🚀 How to Install and Use in Any AI Agent

### Method 1: Project-Level Auto-Discovery (Recommended for Workspaces)
To make this skill automatically available to AI agents in your project repository (e.g. Antigravity, Cursor, Windsurf, Cline), clone or copy this repository into your workspace's `.agents/skills/` directory:

```bash
# Inside your project root:
mkdir -p .agents/skills
git clone https://github.com/bobbyscript/islamic-lyric-audit.git .agents/skills/islamic-lyric-audit
```
* **Auto-Discovery:** Any modern coding assistant scanning `.agents/skills/` will automatically discover and register the skill and its `/al` slash command.

### Method 2: Global Machine-Wide Installation (Antigravity)
To make the skill globally available across all projects on your machine:

```bash
git clone https://github.com/bobbyscript/islamic-lyric-audit.git ~/.gemini/config/skills/islamic-lyric-audit
```

---

## 💬 Invoking the Skill

Whenever an agent has this skill loaded, simply type:
```text
/al <Song Title - Artist>
```

#### Examples:
* `/al Bohemian Rhapsody - Queen`
* `/al Bruno Mars - It Will Rain`
* `/al Bernadya - Satu Bulan`
* `/al top 10 songs globally`

---

## ⚖️ The 8 Evaluated Dimensions (0 to 5 Scale)

| Code | Dimension | Core Focus |
| :---: | :--- | :--- |
| **A** | **Theological Severity** | Ascription of divine attributes, omnipotence, or trivializing eschatology (*Tawḥīd* vs. *Shirk* / Blasphemy). |
| **B** | **Major / Minor Sins** | Reference to *Kabāʾir* (Zinā, Khamr, murder, theft, slander) vs. *Ṣaghāʾir*. |
| **C** | **Taqwā & Pious Discipline** | Deviation from *Waraʿ* (scrupulous caution) and spiritual vigilance. |
| **D** | **Glorification of Sin** | Celebration and publicizing of transgression (*Mujāharah*) vs. neutral narration. |
| **E** | **Faḥsh & Lewdness** | Obscenity, sexual vulgarity, voyeurism, and bodily exhibition (*Tabarruj*). |
| **F** | **Laghw & Idle Speech** | Vain, spiritually void, or time-wasting speech diverting from Allah’s remembrance. |
| **G** | **Violence & Revenge** | Aggression, murder threats, assault, arson, and oppression (*Ẓulm*). |
| **H** | **Pride & Materialism** | Arrogance (*Kibr*), luxury flexing (*Fakhr*), and conspicuous consumerism. |

---

## 🛡️ Mandatory Methodological Guardrails
1. **Strict Prohibition of Takfīr (*Lā Takfīr*):** Sins and statements are judged, never the human artist's creed or ultimate salvation (Ṣaḥīḥ al-Bukhārī 6104).
2. **Utterance vs. Intent:** Distinguishes poetic hyperbole from literal belief, while identifying spiritually dangerous expressions.
3. **No Arithmetic Dilution:** Theological violations are never averaged out or masked by low profanity scores.
4. **Pre-Frozen Rubric:** The 8-dimensional criteria are frozen before auditing to prevent subjective bias.

---

## 🛠️ CLI Helper (`audit_cli.py`)

The bundled script provides data validation, frequency calculations, and HTML report generation. It accepts arrays of songs, wrapped objects (`{"songs": [...]}`), or single song objects:

```bash
# Calculate statistical frequency percentages from an audit JSON file:
python3 scripts/audit_cli.py stats --input audit_results.json

# Generate a responsive, self-contained HTML dashboard with Tailwind styling:
python3 scripts/audit_cli.py generate-html \
  --input audit_results.json \
  --output report.html \
  --title "Islamic Lyric Audit Report" \
  --subtitle "Audited under Orthodox Sunni Jurisprudence"
```

---

## 📜 License

Distributed under the [MIT License](LICENSE). Open-source for the benefit of the Ummah and AI research.
