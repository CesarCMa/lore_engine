export const exportToJSON = (data) => {
  return JSON.stringify(data, null, 2);
};

export const exportToMarkdown = (items, type) => {
  if (type === 'faction') {
    return items.map(f => `
## ${f.name}

**Symbol:** ${f.symbol}

**Values:** ${f.values}

**Soundtrack:** ${f.soundtrack_vibe}

---
    `).join('\n');
  }

  if (type === 'quest') {
    return `
# ${items.title}

## Brief
${items.brief}

## Conflict
${items.conflict}

## Location
${items.location}

## NPCs
${Array.isArray(items.npcs) ? items.npcs.join(', ') : items.npcs}

---
    `;
  }

  return JSON.stringify(items, null, 2);
};
