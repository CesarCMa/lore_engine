import clsx from 'clsx';
import { ChevronDown } from 'lucide-react';

export default function Select({
  value,
  onChange,
  options,
  placeholder,
  className,
  ...props
}) {
  return (
    <div className="relative w-full">
      <select
        value={value}
        onChange={onChange}
        className={clsx(
          'w-full bg-parchment-50 border-2 border-gold-400 rounded-lg px-4 py-2 font-body',
          'focus:ring-2 focus:ring-arcane-500 focus:border-arcane-500 focus:outline-none',
          'appearance-none cursor-pointer transition-colors duration-200',
          'pr-10',
          className
        )}
        {...props}
      >
        {placeholder && (
          <option value="" disabled>
            {placeholder}
          </option>
        )}
        {options.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      <ChevronDown
        className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gold-600 pointer-events-none"
        size={20}
      />
    </div>
  );
}
