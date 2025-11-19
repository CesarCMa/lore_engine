import { Swords, MapPin, Users, Copy } from 'lucide-react';
import Button from './ui/Button';

export default function QuestCard({ quest, onCopy }) {
  // Parse NPCs if it's a string
  const npcs = Array.isArray(quest.npcs)
    ? quest.npcs
    : typeof quest.npcs === 'string'
      ? quest.npcs.split(',').map(n => n.trim())
      : [];

  return (
    <div className="bg-parchment-100 border-2 border-gold-500 rounded-lg p-8 shadow-parchment hover:shadow-gold transition-all duration-200 ornate-card animate-fadeIn">
      {/* Quest title */}
      <h2 className="font-heading text-3xl text-arcane-700 mb-6 text-center">
        {quest.title}
      </h2>

      <div className="scroll-divider mb-6"></div>

      {/* Brief */}
      <div className="mb-6">
        <p className="font-body text-lg italic text-parchment-800 leading-relaxed">
          {quest.brief}
        </p>
      </div>

      {/* Conflict */}
      <div className="mb-6 p-4 bg-parchment-50 border-l-4 border-crimson-500 rounded">
        <div className="flex items-start gap-3">
          <Swords className="text-crimson-600 w-6 h-6 flex-shrink-0 mt-1" />
          <div className="flex-1">
            <p className="font-body text-sm font-semibold text-crimson-700 mb-2">
              Conflict
            </p>
            <p className="font-body text-parchment-900">
              {quest.conflict}
            </p>
          </div>
        </div>
      </div>

      {/* Location */}
      <div className="mb-6 flex items-start gap-3">
        <MapPin className="text-gold-600 w-5 h-5 flex-shrink-0 mt-1" />
        <div className="flex-1">
          <p className="font-body text-sm font-semibold text-parchment-700 mb-1">
            Location
          </p>
          <p className="font-body text-parchment-900">
            {quest.location}
          </p>
        </div>
      </div>

      {/* NPCs */}
      {npcs.length > 0 && (
        <div className="mb-6 flex items-start gap-3">
          <Users className="text-arcane-600 w-5 h-5 flex-shrink-0 mt-1" />
          <div className="flex-1">
            <p className="font-body text-sm font-semibold text-parchment-700 mb-2">
              Notable Characters
            </p>
            <div className="flex flex-wrap gap-2">
              {npcs.map((npc, index) => (
                <span
                  key={index}
                  className="inline-block bg-arcane-100 text-arcane-800 px-3 py-1 rounded-full text-sm font-body"
                >
                  {npc}
                </span>
              ))}
            </div>
          </div>
        </div>
      )}

      <div className="scroll-divider mb-6"></div>

      {/* Actions */}
      <div className="flex gap-3 justify-center">
        <Button
          variant="outline"
          onClick={() => onCopy(quest)}
        >
          <Copy className="inline w-4 h-4 mr-2" />
          Copy Quest
        </Button>
      </div>
    </div>
  );
}
