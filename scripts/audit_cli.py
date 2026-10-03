#!/usr/bin/env python3
"""
CLI Helper for Islamic Lyric Audit Skill.
Provides commands to calculate statistics, format audited datasets, and render interactive HTML dashboards.
"""

import argparse
import json
import sys
from pathlib import Path

def calculate_stats(songs):
    total = len(songs)
    if total == 0:
        return {}
    
    stats = {
        "total_songs": total,
        "laghw_count": sum(1 for s in songs if s.get("scores", [0]*8)[5] >= 3),
        "major_sin_count": sum(1 for s in songs if s.get("scores", [0]*8)[1] >= 4),
        "fahsh_count": sum(1 for s in songs if s.get("scores", [0]*8)[4] >= 4),
        "glorif_sin_count": sum(1 for s in songs if s.get("scores", [0]*8)[3] >= 4),
        "theol_risk_count": sum(1 for s in songs if s.get("scores", [0]*8)[0] >= 3),
        "kibr_count": sum(1 for s in songs if s.get("scores", [0]*8)[7] >= 3),
        "violence_count": sum(1 for s in songs if s.get("scores", [0]*8)[6] >= 3),
    }

    stats["laghw_pct"] = round((stats["laghw_count"] / total) * 100, 1)
    stats["major_sin_pct"] = round((stats["major_sin_count"] / total) * 100, 1)
    stats["fahsh_pct"] = round((stats["fahsh_count"] / total) * 100, 1)
    stats["glorif_sin_pct"] = round((stats["glorif_sin_count"] / total) * 100, 1)
    stats["theol_risk_pct"] = round((stats["theol_risk_count"] / total) * 100, 1)
    stats["kibr_pct"] = round((stats["kibr_count"] / total) * 100, 1)
    stats["violence_pct"] = round((stats["violence_count"] / total) * 100, 1)

    return stats

def render_html_dashboard(songs, title, subtitle, output_path):
    stats = calculate_stats(songs)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
    ::-webkit-scrollbar-track {{ background: rgba(0,0,0,0.05); }}
    ::-webkit-scrollbar-thumb {{ background: rgba(100,116,139,0.3); border-radius: 4px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: rgba(100,116,139,0.5); }}
    .badge {{ font-size: 0.72rem; padding: 0.15rem 0.45rem; border-radius: 9999px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center; }}
    .bar-transition {{ transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1); }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 antialiased font-sans min-h-screen p-4 md:p-8">

  <!-- Header -->
  <header class="max-w-7xl mx-auto mb-10 text-center md:text-left border-b border-slate-800 pb-8">
    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950/80 border border-emerald-700/60 text-emerald-400 text-xs font-semibold mb-4 tracking-wider uppercase">
      <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
      Orthodox Sunni Jurisprudence Audit
    </div>
    <h1 class="text-3xl md:text-5xl font-extrabold tracking-tight bg-gradient-to-r from-emerald-400 via-teal-200 to-cyan-400 bg-clip-text text-transparent">
      {title}
    </h1>
    <p class="text-lg md:text-xl text-slate-400 mt-2 font-medium">
      {subtitle}
    </p>
    <div class="mt-4 flex flex-wrap gap-4 text-xs md:text-sm text-slate-400 justify-center md:justify-start">
      <span class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span> Grounded in Qur’an & Authentic Sunnah</span>
      <span class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span> Utterance-Only Evaluation (No Takfīr)</span>
      <span class="flex items-center gap-1.5"><span class="text-emerald-400">✓</span> 8-Dimensional Pre-Frozen Rubric</span>
    </div>
  </header>

  <main class="max-w-7xl mx-auto space-y-12">

    <!-- KPI Summary Grid -->
    <section class="grid grid-cols-2 md:grid-cols-4 gap-4">
      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl shadow-sm">
        <div class="text-slate-400 text-xs font-medium uppercase tracking-wider">Total Audited Songs</div>
        <div class="text-3xl md:text-4xl font-black text-white mt-1">{stats.get('total_songs', 0)}</div>
        <div class="text-xs text-emerald-400 mt-1">Verified Dataset</div>
      </div>
      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl shadow-sm">
        <div class="text-slate-400 text-xs font-medium uppercase tracking-wider">Idle Speech (Laghw)</div>
        <div class="text-3xl md:text-4xl font-black text-amber-400 mt-1">{stats.get('laghw_pct', 0)}%</div>
        <div class="text-xs text-slate-400 mt-1">{stats.get('laghw_count', 0)} of {stats.get('total_songs', 0)} songs</div>
      </div>
      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl shadow-sm">
        <div class="text-slate-400 text-xs font-medium uppercase tracking-wider">Zinā / Lewdness (Faḥsh)</div>
        <div class="text-3xl md:text-4xl font-black text-rose-400 mt-1">{stats.get('fahsh_pct', 0)}%</div>
        <div class="text-xs text-rose-400/80 mt-1">{stats.get('fahsh_count', 0)} of {stats.get('total_songs', 0)} songs</div>
      </div>
      <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl shadow-sm">
        <div class="text-slate-400 text-xs font-medium uppercase tracking-wider">Theological Red Flags</div>
        <div class="text-3xl md:text-4xl font-black text-purple-400 mt-1">{stats.get('theol_risk_pct', 0)}%</div>
        <div class="text-xs text-purple-400/80 mt-1">{stats.get('theol_risk_count', 0)} of {stats.get('total_songs', 0)} songs</div>
      </div>
    </section>

    <!-- Visual Graphs & Chart Section -->
    <section class="bg-slate-900/80 border border-slate-800 p-6 md:p-8 rounded-3xl space-y-8 shadow-lg">
      <div>
        <h2 class="text-2xl font-bold text-white flex items-center gap-2">
          <svg class="w-6 h-6 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
          Thematic Frequency Distribution
        </h2>
        <p class="text-sm text-slate-400 mt-1">Empirical audit of moral, behavioral, and theological categories across the audited corpus.</p>
      </div>

      <div class="space-y-4">
        <!-- Laghw -->
        <div>
          <div class="flex justify-between text-sm font-semibold mb-1">
            <span class="text-amber-300">Idle / Unbeneficial Speech (Laghw)</span>
            <span class="text-slate-300">{stats.get('laghw_pct', 0)}% ({stats.get('laghw_count', 0)} songs)</span>
          </div>
          <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden p-0.5">
            <div class="bg-gradient-to-r from-amber-500 to-yellow-400 h-3 rounded-full bar-transition" style="width: {stats.get('laghw_pct', 0)}%;"></div>
          </div>
        </div>

        <!-- Zina / Fahsh -->
        <div>
          <div class="flex justify-between text-sm font-semibold mb-1">
            <span class="text-rose-400">Sexual Immorality / Fornication (Zinā / Faḥsh)</span>
            <span class="text-slate-300">{stats.get('fahsh_pct', 0)}% ({stats.get('fahsh_count', 0)} songs)</span>
          </div>
          <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden p-0.5">
            <div class="bg-gradient-to-r from-rose-600 to-pink-500 h-3 rounded-full bar-transition" style="width: {stats.get('fahsh_pct', 0)}%;"></div>
          </div>
        </div>

        <!-- Materialism / Arrogance -->
        <div>
          <div class="flex justify-between text-sm font-semibold mb-1">
            <span class="text-cyan-400">Materialism, Vanity & Boasting (Kibr / Fakhr)</span>
            <span class="text-slate-300">{stats.get('kibr_pct', 0)}% ({stats.get('kibr_count', 0)} songs)</span>
          </div>
          <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden p-0.5">
            <div class="bg-gradient-to-r from-cyan-600 to-blue-500 h-3 rounded-full bar-transition" style="width: {stats.get('kibr_pct', 0)}%;"></div>
          </div>
        </div>

        <!-- Glorification -->
        <div>
          <div class="flex justify-between text-sm font-semibold mb-1">
            <span class="text-orange-400">Active Glorification of Sins (Mujāharah)</span>
            <span class="text-slate-300">{stats.get('glorif_sin_pct', 0)}% ({stats.get('glorif_sin_count', 0)} songs)</span>
          </div>
          <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden p-0.5">
            <div class="bg-gradient-to-r from-orange-600 to-amber-500 h-3 rounded-full bar-transition" style="width: {stats.get('glorif_sin_pct', 0)}%;"></div>
          </div>
        </div>

        <!-- Theological Risk -->
        <div>
          <div class="flex justify-between text-sm font-semibold mb-1">
            <span class="text-purple-400">Theological Red Flags (Shirk / Kufr Wording / Blasphemy)</span>
            <span class="text-slate-300">{stats.get('theol_risk_pct', 0)}% ({stats.get('theol_risk_count', 0)} songs)</span>
          </div>
          <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden p-0.5">
            <div class="bg-gradient-to-r from-purple-600 to-fuchsia-600 h-3 rounded-full bar-transition" style="width: {stats.get('theol_risk_pct', 0)}%;"></div>
          </div>
        </div>

        <!-- Violence -->
        <div>
          <div class="flex justify-between text-sm font-semibold mb-1">
            <span class="text-red-400">Violence, Injustice & Revenge (Ẓulm / Qatl)</span>
            <span class="text-slate-300">{stats.get('violence_pct', 0)}% ({stats.get('violence_count', 0)} songs)</span>
          </div>
          <div class="w-full bg-slate-800 rounded-full h-4 overflow-hidden p-0.5">
            <div class="bg-gradient-to-r from-red-700 to-red-500 h-3 rounded-full bar-transition" style="width: {stats.get('violence_pct', 0)}%;"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Table Section -->
    <section class="space-y-4">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-4">
        <div>
          <h2 class="text-2xl font-bold text-white">Audited Songs Catalog</h2>
          <p class="text-sm text-slate-400">Live search and severity filtering.</p>
        </div>
        <div class="flex items-center gap-3">
          <input id="searchInput" type="text" placeholder="Search song or artist..." class="bg-slate-900 border border-slate-700 text-sm rounded-xl px-4 py-2 text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 w-64">
          <select id="severityFilter" class="bg-slate-900 border border-slate-700 text-sm rounded-xl px-3 py-2 text-white focus:outline-none focus:border-emerald-500">
            <option value="all">All Songs ({len(songs)})</option>
            <option value="theol">Theological Risk (>=3)</option>
            <option value="sin">Major Sin Content (>=4)</option>
            <option value="clean">Low Concern (<=1)</option>
          </select>
        </div>
      </div>

      <div class="overflow-x-auto rounded-2xl border border-slate-800 shadow-xl">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-slate-900/90 text-xs uppercase font-semibold text-slate-400 border-b border-slate-800 tracking-wider">
            <tr>
              <th class="py-3.5 px-3 text-center">Rank</th>
              <th class="py-3.5 px-4">Song Title</th>
              <th class="py-3.5 px-4">Artist</th>
              <th class="py-3.5 px-2 text-center" title="Theological">Theol</th>
              <th class="py-3.5 px-2 text-center" title="Sin">Sin</th>
              <th class="py-3.5 px-2 text-center" title="Taqwa">Taqwā</th>
              <th class="py-3.5 px-2 text-center" title="Glorification">Glorif</th>
              <th class="py-3.5 px-2 text-center" title="Fahsh">Faḥsh</th>
              <th class="py-3.5 px-2 text-center" title="Laghw">Laghw</th>
              <th class="py-3.5 px-4">Core Islamic Notes</th>
            </tr>
          </thead>
          <tbody id="tableBody" class="divide-y divide-slate-800/60 bg-slate-950/60">
          </tbody>
        </table>
      </div>
      <div id="noResults" class="hidden text-center py-8 text-slate-500 text-sm">No matching songs found.</div>
    </section>

  </main>

  <script>
    const songsData = {json.dumps(songs)};
    const tableBody = document.getElementById('tableBody');
    const searchInput = document.getElementById('searchInput');
    const severityFilter = document.getElementById('severityFilter');
    const noResults = document.getElementById('noResults');

    function renderScoreBadge(val) {{
      if (val === 0) return `<span class="badge bg-slate-800 text-slate-400">0</span>`;
      if (val === 1) return `<span class="badge bg-slate-800 text-slate-300">1</span>`;
      if (val === 2) return `<span class="badge bg-amber-950/60 text-amber-300 border border-amber-800/40">2</span>`;
      if (val === 3) return `<span class="badge bg-orange-950/60 text-orange-300 border border-orange-800/40">3</span>`;
      if (val === 4) return `<span class="badge bg-rose-950/80 text-rose-300 border border-rose-700/60">4</span>`;
      return `<span class="badge bg-purple-950 text-purple-300 border border-purple-500 animate-pulse font-bold">5</span>`;
    }}

    function renderTable(data) {{
      tableBody.innerHTML = '';
      if (data.length === 0) {{
        noResults.classList.remove('hidden');
        return;
      }}
      noResults.classList.add('hidden');

      data.forEach((item, idx) => {{
        const tr = document.createElement('tr');
        tr.className = "hover:bg-slate-900/60 transition";
        const rank = item.rank || (idx + 1);
        const scores = item.scores || [0,0,0,0,0,0,0,0];
        const notes = item.theol_notes || item.notes || item.sin_notes || 'No issues identified.';

        tr.innerHTML = `
          <td class="py-3 px-3 text-center font-bold text-slate-300">#${{rank}}</td>
          <td class="py-3 px-4 font-semibold text-white">${{item.song}}</td>
          <td class="py-3 px-4 text-slate-300">${{item.artist}}</td>
          <td class="py-3 px-2 text-center">${{renderScoreBadge(scores[0])}}</td>
          <td class="py-3 px-2 text-center">${{renderScoreBadge(scores[1])}}</td>
          <td class="py-3 px-2 text-center">${{renderScoreBadge(scores[2])}}</td>
          <td class="py-3 px-2 text-center">${{renderScoreBadge(scores[3])}}</td>
          <td class="py-3 px-2 text-center">${{renderScoreBadge(scores[4])}}</td>
          <td class="py-3 px-2 text-center">${{renderScoreBadge(scores[5])}}</td>
          <td class="py-3 px-4 text-xs text-slate-400 leading-relaxed max-w-md">${{notes}}</td>
        `;
        tableBody.appendChild(tr);
      }});
    }}

    function filterData() {{
      const query = searchInput.value.toLowerCase().trim();
      const filterType = severityFilter.value;

      const filtered = songsData.filter(item => {{
        const matchesQuery = item.song.toLowerCase().includes(query) || 
                             item.artist.toLowerCase().includes(query);
        
        const scores = item.scores || [0,0,0,0,0,0,0,0];
        let matchesFilter = true;
        if (filterType === 'theol') matchesFilter = scores[0] >= 3;
        else if (filterType === 'sin') matchesFilter = scores[1] >= 4;
        else if (filterType === 'clean') matchesFilter = scores[0] <= 1 && scores[1] <= 1 && scores[4] <= 1;

        return matchesQuery && matchesFilter;
      }});

      renderTable(filtered);
    }}

    searchInput.addEventListener('input', filterData);
    severityFilter.addEventListener('change', filterData);
    renderTable(songsData);
  </script>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated HTML dashboard at: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Islamic Lyric Audit Skill CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: stats
    stats_parser = subparsers.add_parser("stats", help="Compute statistics from a JSON audit file")
    stats_parser.add_argument("--input", required=True, help="Path to input JSON file containing songs")
    stats_parser.add_argument("--output", help="Optional path to output stats JSON")

    # Subcommand: generate-html
    html_parser = subparsers.add_parser("generate-html", help="Generate an interactive HTML dashboard from audit JSON")
    html_parser.add_argument("--input", required=True, help="Path to input JSON file containing songs")
    html_parser.add_argument("--output", required=True, help="Path to output HTML file")
    html_parser.add_argument("--title", default="Islamic Lyric Audit Report", help="Report Title")
    html_parser.add_argument("--subtitle", default="Audited under Orthodox Sunni Jurisprudence", help="Report Subtitle")

    args = parser.parse_args()

    if args.command == "stats":
        with open(args.input, "r", encoding="utf-8") as f:
            songs = json.load(f)
        stats = calculate_stats(songs)
        output_data = json.dumps(stats, indent=2)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output_data)
            print(f"Saved stats to: {args.output}")
        else:
            print(output_data)

    elif args.command == "generate-html":
        with open(args.input, "r", encoding="utf-8") as f:
            songs = json.load(f)
        render_html_dashboard(songs, args.title, args.subtitle, args.output)

if __name__ == "__main__":
    main()
