import { ALL_CATALOG_ENTITIES } from '../src/data/catalog/index.ts';
import { DIVISIONS } from '../src/constants/callNumbers.ts';

const allDivCodes = new Set(DIVISIONS.map(d => d.code));
const coveredDivs = new Map<string, number>();

ALL_CATALOG_ENTITIES.forEach(e => {
  const cn = e.callNumber || '';
  const m = cn.match(/^(\d{3})\./);
  if (m) coveredDivs.set(m[1], (coveredDivs.get(m[1]) || 0) + 1);
});

// Empty divisions
const empty: string[] = [];
allDivCodes.forEach(code => {
  if (!coveredDivs.has(code)) empty.push(code);
});
empty.sort();

// Sparse divisions (1-2 entities)
const sparse: { code: string; count: number }[] = [];
coveredDivs.forEach((count, code) => {
  if (count <= 2 && allDivCodes.has(code)) sparse.push({ code, count });
});
sparse.sort((a, b) => a.code.localeCompare(b.code));

// Orphan division codes
const orphanDivs = new Set<string>();
ALL_CATALOG_ENTITIES.forEach(e => {
  const cn = e.callNumber || '';
  const m = cn.match(/^(\d{3})\./);
  if (m && !allDivCodes.has(m[1])) orphanDivs.add(m[1]);
});

// Entities without callNumber
let noCN = 0;
ALL_CATALOG_ENTITIES.forEach(e => {
  if (!e.callNumber) noCN++;
});

console.log('=== DIVISION AUDIT ===');
console.log('Total entities:', ALL_CATALOG_ENTITIES.length);
console.log('Total divisions defined:', allDivCodes.size);
console.log('Divisions covered:', coveredDivs.size);
console.log('Empty divisions:', empty.length);
console.log('Sparse divisions (1-2):', sparse.length);
console.log('Orphan division codes:', orphanDivs.size);
console.log('Entities without callNumber:', noCN);

if (empty.length > 0) {
  console.log('\n--- EMPTY DIVISIONS ---');
  empty.forEach(code => {
    const div = DIVISIONS.find(d => d.code === code);
    console.log(code, '|', div?.heading);
  });
}

if (sparse.length > 0) {
  console.log('\n--- SPARSE DIVISIONS (1-2 entities) ---');
  sparse.forEach(s => {
    const div = DIVISIONS.find(d => d.code === s.code);
    console.log(s.code, '|', div?.heading, '|', s.count);
  });
}

if (orphanDivs.size > 0) {
  console.log('\n--- ORPHAN DIVISION CODES ---');
  [...orphanDivs].sort().forEach(code => {
    const count = coveredDivs.get(code) || 0;
    console.log(code, '| count:', count);
  });
}

// Duplicate slugs check
const slugMap = new Map<string, string[]>();
ALL_CATALOG_ENTITIES.forEach(e => {
  const arr = slugMap.get(e.slug) || [];
  arr.push(e.callNumber || 'no-cn');
  slugMap.set(e.slug, arr);
});
const dupes = [...slugMap.entries()].filter(([_, v]) => v.length > 1);
console.log('\n--- DUPLICATE SLUGS ---');
console.log('Count:', dupes.length);
dupes.forEach(([slug, cns]) => console.log('  DUP:', slug, cns));
