import { Scroll, Music, Copy } from 'lucide-react';
import Button from './ui/Button';

export default function FactionCard({ faction, onCopy }) {
  return (
    <div className="bg-parchment-100 border-2 border-gold-500 rounded-lg p-6 shadow-parchment hover:scale-105 hover:shadow-gold transition-all duration-200 ornate-card animate-fadeIn">
      {/* Header with faction name */}
      <div className="flex items-center gap-3 mb-4">
        <Scroll className="text-gold-500 w-6 h-6 flex-shrink-0" />
        <h3 className="font-heading text-2xl text-arcane-700 break-words">
          {faction.name}
        </h3>
      </div>

      <div className="scroll-divider"></div>

      {/* Faction details */}
      <div className="space-y-3 mb-4">
        {/* Symbol */}
        <div>
          <p className="font-body text-sm text-parchment-600 mb-1">Symbol</p>
          <p className="font-body text-parchment-900 italic">
            {faction.symbol}
          </p>
        </div>

        {/* Values */}
        <div>
          <p className="font-body text-sm text-parchment-600 mb-1">Values</p>
          <p className="font-body text-parchment-900">
            {faction.values}
          </p>
        </div>

        {/* Soundtrack vibe */}
        {faction.soundtrack_vibe && (
          <div className="flex items-start gap-2">
            <Music className="text-arcane-600 w-5 h-5 flex-shrink-0 mt-0.5" />
            <div className="flex-1">
              <p className="font-body text-sm text-parchment-600 mb-1">Soundtrack Vibe</p>
              <p className="font-body text-parchment-900">
                {faction.soundtrack_vibe}
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Copy button */}
      <Button
        variant="outline"
        size="sm"
        onClick={() => onCopy(faction)}
        className="w-full"
      >
        <Copy className="inline w-4 h-4 mr-2" />
        Copy to Clipboard
      </Button>
    </div>
  );
}
