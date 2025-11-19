import { Plus, Minus, Sparkles } from 'lucide-react';
import Button from './ui/Button';

export default function GeneratorControls({ count, setCount, onGenerate, isLoading }) {
  const incrementCount = () => {
    if (count < 10) setCount(count + 1);
  };

  const decrementCount = () => {
    if (count > 1) setCount(count - 1);
  };

  const handleInputChange = (e) => {
    const value = parseInt(e.target.value, 10);
    if (!isNaN(value) && value >= 1 && value <= 10) {
      setCount(value);
    }
  };

  return (
    <div className="flex flex-col items-center gap-6 mb-8">
      {/* Count selector */}
      <div className="flex items-center gap-4">
        <Button
          variant="secondary"
          size="sm"
          onClick={decrementCount}
          disabled={count <= 1 || isLoading}
          aria-label="Decrease count"
        >
          <Minus className="w-4 h-4" />
        </Button>

        <div className="flex flex-col items-center gap-1">
          <label htmlFor="count" className="font-body text-sm text-parchment-700">
            Number to Generate
          </label>
          <input
            id="count"
            type="number"
            min="1"
            max="10"
            value={count}
            onChange={handleInputChange}
            disabled={isLoading}
            className="w-20 text-center bg-parchment-50 border-2 border-gold-400 rounded-lg px-3 py-2 font-heading text-xl text-arcane-700 focus:ring-2 focus:ring-arcane-500 focus:border-arcane-500 focus:outline-none"
          />
        </div>

        <Button
          variant="secondary"
          size="sm"
          onClick={incrementCount}
          disabled={count >= 10 || isLoading}
          aria-label="Increase count"
        >
          <Plus className="w-4 h-4" />
        </Button>
      </div>

      {/* Generate button */}
      <Button
        variant="primary"
        size="lg"
        onClick={onGenerate}
        isLoading={isLoading}
        disabled={isLoading}
      >
        <Sparkles className="inline w-5 h-5 mr-2" />
        Generate
      </Button>
    </div>
  );
}
