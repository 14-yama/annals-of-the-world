Annals UI (Vite + React + TypeScript + Chakra UI v3)

Quickstart

1. Install dependencies

```bash
cd ui
npm install
```

2. Run dev server

```bash
npm run dev
```

Notes about the orphan CSV

The triage page fetches the orphan CSV from the URL configured by the Vite env var `VITE_ORPHAN_CSV_URL`. By default it attempts to fetch `/data/orphan_nodes.csv` relative to the UI server root. Two recommended approaches:

- Serve the repository `data/` dir on a simple static server and point the UI to it:

```bash
# serve data/ on port 8000
python3 -m http.server --directory ../data 8000

# then run the UI dev server from ui/ (it will fetch http://localhost:8000/orphan_nodes.csv)
VITE_ORPHAN_CSV_URL=http://localhost:8000/orphan_nodes.csv npm run dev
```

- Or copy `data/orphan_nodes.csv` into `ui/public/data/orphan_nodes.csv` so Vite will serve it directly.

What I added

- `ui/` folder with a Vite + React + TypeScript scaffold
- Chakra UI v3 wiring and a small `Triage` page that fetches the CSV and allows decisions

Chakra CLI
------------

I added a minimal Chakra CLI setup so you can manage design tokens and generate theme helpers.

- `ui/.chakra/config.json` — minimal config that points tokens output to `src/tokens` and theme path to `src/theme.ts`.
- `package.json` scripts:
	- `npm run chakra:init` — runs `npx @chakra-ui/cli init` to scaffold tokens/theme helpers interactively.
	- `npm run chakra:tokens` — runs `npx @chakra-ui/cli tokens --out src/tokens` to extract tokens (or re-run after edits).
	- `npm run chakra:generate` — placeholder for `npx @chakra-ui/cli generate` if you use generation features.

Usage notes
-----------

1. Install dev deps in the UI folder:

```bash
cd ui
npm install
```

2. Run the init helper (interactive):

```bash
npm run chakra:init
```

3. Re-generate tokens after editing theme/styles:

```bash
npm run chakra:tokens
```

If you prefer yarn or pnpm, replace `npm run` accordingly (e.g., `pnpm dlx @chakra-ui/cli init`).

Next steps

- Run the UI locally and verify the triage workflow. If you want, I can add a button to automatically apply approved decisions by calling a script that appends relationships.
