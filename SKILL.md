---
name: islamic-lyric-audit
description: Systematically audit and assess song lyrics, spoken media, and popular cultural speech under an orthodox Sunni Islamic framework. Triggered whenever the user invokes the '/al' command, says '/al [song]', asks to 'audit lyrics', or evaluates songs against Islamic principles. Evaluates content across 8 dimensions (Theology/Tawḥīd, Major/Minor Sins, Taqwā/Discipline, Glorification, Faḥsh/Lewdness, Laghw/Idle Speech, Violence/Injustice, and Pride/Materialism) on a pre-frozen 0-5 scale. Enforces strict methodological guardrails (no takfīr, utterance-only assessment, figurative vs. literal distinction). Generates markdown reports and interactive HTML dashboards with statistical graphs.
---

# Islamic Lyric Audit Skill

This skill provides a systematic, academically rigorous, and spiritually grounded framework for evaluating song lyrics, transcripts, and media speech through orthodox Sunni Islamic scholarship.

## Core Islamic Guardrails (Mandatory)

1. **Strict Prohibition of Takfīr (*Lā Takfīr*):**
   * Never declare an artist, writer, or listener to be an apostate, disbeliever (*kāfir*), or hypocrite.
   * Evaluate **the words and themes**, never the human being's inward creed or eternal fate (*"Whoever calls a man a disbeliever or enemy of Allah, when he is not so, it returns upon him"* — Ṣaḥīḥ al-Bukhārī 6104).
   * Phrasing standard: *"This lyric contains language that, if intended literally, conflicts with Tawḥīd / constitutes a form of blasphemous speech."*

2. **Pre-Frozen Scoring Matrix:**
   * The 8-dimensional scoring rubric must be frozen **before** evaluating any songs to prevent retrospective bias.
   * Do not invent ad-hoc penalties or tailor matrices to penalize specific artists.

3. **No Arithmetic Dilution of Theological Content:**
   * Never compute a composite mathematical average that obscures severe theological violations.
   * Theological concerns (Dimension A) must be reported separately and given primacy over moral or behavioral sins.

4. **Metaphor vs. Literalism:**
   * Distinguish between literal theological claims vs. romantic hyperbole (*"I worship you"*, *"You're my salvation"*, *"You gave me life"*).
   * Do not excuse problematic language merely because it is culturally common, but explicitly document:
     > *"Interpretation-dependent: figurative romantic expression, yet spiritually inappropriate under strict Tawḥīd-conscious discipline."*

5. **Description vs. Glorification:**
   * Distinguish whether a lyric:
     (a) condemns sin, (b) describes it neutrally, (c) laments/regrets it, or (d) celebrates, encourages, and glamorizes it (*Mujāharah*).

---

## The 8 Evaluated Dimensions (0 to 5 Scale)

| Code | Dimension | Core Concept | References |
| :---: | :--- | :--- | :--- |
| **A** | **Theological Severity** | Ascription of divine attributes (Alpha/Omega, sole survival, omnipotence) or eschatology mockery. | Surah al-Ikhlāṣ; Qur'an 57:3; 4:48. |
| **B** | **Major / Minor Sins** | Reference to *Kabāʾir* (Zinā, Khamr, murder, armed robbery, slander) vs. *Ṣaghāʾir*. | Imām al-Dhahabī (*Kitāb al-Kabāʾir*). |
| **C** | **Taqwā & Pious Discipline** | Deviation from *Waraʿ* (caution), modest deportment, and spiritual vigilance. | Sunan al-Tirmidhī 1205. |
| **D** | **Glorification of Sin** | Celebration and publicizing of transgression (*Mujāharah*) vs. neutral lamentation. | Ṣaḥīḥ al-Bukhārī 6069; Qur'an 24:19. |
| **E** | **Faḥsh & Lewdness** | Obscenity, sexual vulgarity, voyeurism, and bodily exhibition (*Tabarruj*). | Qur'an 17:32; Sunan al-Tirmidhī 1977. |
| **F** | **Laghw & Idle Speech** | Vain, spiritually void, or time-wasting speech diverting from Allah’s remembrance. | Qur'an 23:3; 28:55. |
| **G** | **Violence & Revenge** | Aggression, murder threats, assault, arson, and oppression (*Ẓulm*). | Qur'an 4:93; Ṣaḥīḥ Muslim 2577. |
| **H** | **Pride & Materialism** | Arrogance (*Kibr*), luxury flexing (*Fakhr*), and conspicuous consumerism. | Ṣaḥīḥ Muslim 91; Qur'an 102:1–2. |

---

## Workflow Protocol

### Step 1: Establish Dataset & Source Transparency
* For yearly or historical datasets, use authoritative global measurement bodies:
  * **IFPI Global Singles / Digital Single Reports** (paid sales + multi-platform streaming equivalents).
  * **Billboard Global 200** (digital sales and streaming across 200+ territories).
* For real-time snapshots (e.g. current month), use the consensus of Billboard Global 200 and global Spotify/Apple Music charts.
* Never silently substitute songs.

### Step 2: Song-by-Song Assessment
For each track, evaluate and record:
1. Title, Artist, Rank, Year/Date, and Source.
2. 8-dimensional scores (`[A, B, C, D, E, F, G, H]`).
3. Cited minimum necessary lyric fragment illustrating the issue.
4. Theological assessment (shirk-like wording, divine attributes, eschatology).
5. Sin assessment (major/minor sins, glorification).
6. Pious-discipline assessment (laghw, vulgarity, vanity).
7. Confidence rating: High, Medium, or Low (state if interpretation-dependent).

### Step 3: Compute Statistical Frequencies
Tabulate the occurrence across the dataset:
* Percentage with *Laghw* ($\ge 3$)
* Percentage with *Zinā* / *Faḥsh* ($\ge 4$)
* Percentage with *Khamr* / Intoxicants
* Percentage with *Kibr* / Materialism ($\ge 3$)
* Percentage with Severe Theological Risk ($\ge 3$)

### Step 4: Generate Interactive Deliverables
* Create a Markdown audit report saved in the brain/workspace.
* Use the bundled CLI helper (`scripts/audit_cli.py`) to generate a self-contained, interactive HTML dashboard:
  ```bash
  # Run directly from the skill directory or repo root:
  python3 scripts/audit_cli.py generate-html \
    --input <path_to_audit.json> \
    --output <path_to_report.html> \
    --title "Islamic Lyric Audit Report" \
    --subtitle "Systematic Sunni Jurisprudential Assessment"
  ```

---

## Detailed References

* Comprehensive jurisprudence and classical sources: see `references/jurisprudence_evidence.md`.
* Complete 8-dimensional scoring rules (0 to 5): see `references/scoring_rubric.md`.
