import QuestCard from './QuestCard';

export default function QuestDisplay({ quest, onCopy }) {
  if (!quest) {
    return null;
  }

  return (
    <div className="max-w-4xl mx-auto">
      <QuestCard quest={quest} onCopy={onCopy} />
    </div>
  );
}
