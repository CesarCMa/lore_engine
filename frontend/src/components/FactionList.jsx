import { Scroll } from 'lucide-react';
import FactionCard from './FactionCard';

export default function FactionList({ factions, onCopyFaction, onSelectFaction, selectedFactions = [] }) {
  if (factions.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-16 text-center">
        <Scroll className="text-parchment-400 w-16 h-16 mb-4" />
        <p className="font-body text-xl text-parchment-600">
          No factions yet. Generate some to get started!
        </p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {factions.map((faction, index) => (
        <div
          key={faction.name || index}
          style={{ animationDelay: `${index * 0.1}s` }}
          className="animate-slideUp"
        >
          <FactionCard
            faction={faction}
            onCopy={onCopyFaction}
            onSelect={onSelectFaction}
            isSelected={selectedFactions.some(f => f.name === faction.name)}
          />
        </div>
      ))}
    </div>
  );
}
