import { ALL_CATALOG_ENTITIES } from '../src/data/catalog/index.ts';
import { DIVISIONS } from '../src/constants/callNumbers.ts';

function getDivision(cn: string): string | null {
  const m = cn.match(/^(\d{3})\./);
  return m ? m[1] : null;
}

const allDivCodes = new Set(DIVISIONS.map(d => d.code));
const coveredDivs = new Set<string>();
const divCounts: Record<string, number> = {};
const slugSet = new Set<string>();
const dupes: string[] = [];

for (const e of ALL_CATALOG_ENTITIES) {
  if (slugSet.has(e.slug)) {
    dupes.push(e.slug);
  }
  slugSet.add(e.slug);
  const div = getDivision(e.callNumber || '');
  if (div) {
    coveredDivs.add(div);
    divCounts[div] = (divCounts[div] || 0) + 1;
  }
}

const divMap = Object.fromEntries(DIVISIONS.map(d => [d.code, d]));
const missingDivs = [...allDivCodes].filter(d => !coveredDivs.has(d)).sort();

console.log('=== CATALOG AUDIT ===');
console.log('Total entities:', ALL_CATALOG_ENTITIES.length);
console.log('Unique slugs:', slugSet.size);
console.log('Duplicate slugs found:', dupes.length);
console.log('Total divisions defined:', allDivCodes.size);
console.log('Divisions covered:', coveredDivs.size);
console.log('Divisions MISSING:', missingDivs.length);
console.log('');

if (dupes.length > 0) {
  console.log('=== DUPLICATE SLUGS ===');
  for (const s of dupes.slice(0, 30)) {
    console.log('  DUP:', s);
  }
  console.log('');
}

console.log('=== MISSING DIVISIONS ===');
for (const code of missingDivs) {
  const d = divMap[code];
  console.log(`${code} | Class ${d.parentClass} | ${d.heading}`);
}

console.log('');
console.log('=== SPARSE DIVISIONS (1-2 entities only) ===');
const sparse = [...coveredDivs]
  .filter(d => divCounts[d] <= 2)
  .sort();
for (const code of sparse) {
  const d = divMap[code];
  if (d) {
    console.log(`${code} | ${divCounts[code]} entity | ${d.heading}`);
  }
}
