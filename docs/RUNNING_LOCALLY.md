# Running the Annals UI Locally

## Quick Start

```bash
cd ui
npm run dev
```

The app will be available at **http://localhost:5173/**

## Prerequisites

- **Node.js** ≥ 18 (recommended: 20.x)
- **npm** ≥ 9

## Install Dependencies

```bash
cd ui
npm install
```

## Development Server

```bash
cd ui
npm run dev
```

This starts the Vite dev server with hot module replacement (HMR). Changes to source files
are reflected immediately in the browser.

### Expose to Network

To access the dev server from other devices on your local network:

```bash
cd ui
npx vite --host
```

This binds to `0.0.0.0` and shows both `localhost` and your LAN IP address.

## Production Build

```bash
cd ui
npm run build
```

Output is written to `ui/dist/`. To preview the production build locally:

```bash
cd ui
npm run preview
```

Preview runs on the same port (5173) serving the built `dist/` folder.

## Environment Variables

The app uses Vite's `import.meta.env` for configuration. Variables must be prefixed
with `VITE_` to be exposed to the browser client.

| Variable | Purpose | Example |
|----------|---------|---------|
| `VITE_APPWRITE_ENDPOINT` | Appwrite Cloud endpoint | `https://fra.cloud.appwrite.io/v1` |
| `VITE_APPWRITE_PROJECT_ID` | Appwrite project ID | `69cc45e3000d587ea5e6` |
| `VITE_APPWRITE_DATABASE_ID` | Appwrite database ID | `annals_db` |

These are stored in `ui/.env` (gitignored).

## Appwrite Migration

To seed entities into Appwrite Cloud (requires an API key):

```bash
# Dry run (no writes):
DRY_RUN=1 npx tsx scripts/migrate_to_appwrite.ts

# Full migration:
APPWRITE_API_KEY=<your-key> npx tsx scripts/migrate_to_appwrite.ts
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `npm run dev` → "Missing script: dev" | Make sure you're in the `ui/` directory |
| Blank page at localhost:5173 | Ensure Vite runs from `ui/` (not project root) |
| Port 5173 already in use | Kill the other process: `lsof -ti:5173 \| xargs kill` |
| Chakra v3 type errors in Triage.tsx | Known pre-existing issue — does not affect app runtime |
